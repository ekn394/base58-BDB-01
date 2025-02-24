# Raw Tx Parser 
# Feb 24, 2025
# DIY study tool for going through Base58 course on Bitcoin Developer Basics o1

import hashlib

raw_transaction_hex = "01000000038b9896d07dd8f694b72e750a69105e0f134837500a020ebb8fc77380973075bc000000008a47304402206213230eddf32c60167e654e3934602c0e46308932ea344a0e242699c1818f51022044895b0fc7adef9e551777d0de789d508fb56785ca80fbbfeec01b9d07b4fb7901410450128ec8ff327d0cd782702a32f51b14149d8a19b89075a56ead462363fa29ae9b35ca4f71ae8d5cd78803d835d05451ebb3ee861c80746f0e4fd5316ec306a7ffffffff92491ce956f3a52074ee8ab024069bc14c8396c33d8bb43de1ef1cc7f9f01a46000000008b48304502207fec947609bd275a32cfd058c76678fe868c12b681c9ab0c31f716a92ba5fed0022100cd95a9ff2036a7ee0babe268ac64b425b4490be36609452ec01c11b8eaf14665014104b5a08389cbbf01178c5451f9e1c09265e73ef7bc4a1bc6761143593134e5c6460ab31ae2d5f09140a5e95a58538fd4651cb966a86de41c1a6a79b6045ecc0312ffffffff3ca3845de7916e872570ce1676dedc3151717b7d345affa188eaa7baad3bd1a1000000006b483045022100a53211eed0e857dfab414f106190780c3791797b81aaf5a8a8f997681f6ea660022030a00ef0733bafa5f05026e027ac6f230c3929f9c766ef31edeabf2bcaed81740121036ec01e60571b5050bafb2d77063061a487228da342e996003e35ac7b5519e2e7ffffffff048e2e1601000000001976a9142b18e0074aad70661b6fecf742cbefab4a145d1188ac40420f00000000001976a914a229e570ef0c11b6a20451d65047b0fbe2c96a2f88ac40420f00000000001976a91408536923b85945c704b47bb2657294757bc417dc88ac40420f00000000001976a91415c307a88533528de8414fc2fc96b4e67ac0e0ef88ac00000000"
#raw_transaction_hex = "0100000001c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704000000004847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901ffffffff0200ca9a3b00000000434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000"

def double_sha256(data):
    #Perform double SHA-256 hashing.
    first_hash=hashlib.sha256(data).digest()
    second_hash=hashlib.sha256(first_hash).digest()
    return second_hash

def raw_tx_hex_to_txid(raw_transaction_hex):
    # Convert the hex string to bytes 
    raw_transaction_bytes = bytes.fromhex(raw_transaction_hex)
    # Perform the sha256 hashing algorithm (twice) 
    txid = double_sha256(raw_transaction_bytes)
    # Reverse the order of the bites and convert back out of bytes into a long hex string of a properly formated txid
    txid_hex = txid[::-1].hex() 
    return txid_hex

def getVersion(raw_transaction_hex):
    sliced_version = raw_transaction_hex[:2]
    tx_version = int(sliced_version, 16)
    return tx_version

def getNumInputs(raw_transaction_hex):
    num_inputs = raw_transaction_hex[2:10]
    num_inputs = int(num_inputs, 16)
    return num_inputs

def getInput1Tx(raw_transaction_hex):
    input_1_txid = raw_transaction_hex[10:74]
    input_1_txid = bytes.fromhex(input_1_txid)
    input_1_txid = input_1_txid[::-1].hex()
    return input_1_txid

def getInput1Vout(raw_transaction_hex):
    input_1_vout = raw_transaction_hex[74:82]
    input_1_vout = bytes.fromhex(input_1_vout)
    input_1_vout = input_1_vout[::-1].hex()
    return input_1_vout 

def getInput1ScriptSigLen(raw_transaction_hex):
    input_1_ScriptSigLen = bytes.fromhex(raw_transaction_hex[82:84]).hex()
    #input_1_ScriptSigLen = bytes.fromhex(input_1_ScriptSigLen)
    #input_1_ScriptSigLen = input_1_ScriptSigLen[::-1].hex()
    input_1_ScriptSigLen = int(input_1_ScriptSigLen, 16)
    return input_1_ScriptSigLen  

def getInput1ScriptSig(raw_transaction_hex):
    
    input_1_ScriptSig = bytes.fromhex(raw_transaction_hex[84:84+(input_1_scriptSigLen*2)]).hex()
    #input_1_ScriptSig = bytes.fromhex(raw_transaction_hex[84:84+276]).hex()
    return input_1_ScriptSig

def getInput1Sequence(raw_transaction_hex):
    # Note, I don't know if these are little endian or big endian but they are typically FFFFFFFFFF
    endPosScriptSig1 = 84+(input_1_scriptSigLen*2)
    input_1_Sequence = bytes.fromhex(raw_transaction_hex[endPosScriptSig1: endPosScriptSig1+8]).hex()
    #input_1_ScriptSig = bytes.fromhex(raw_transaction_hex[84:84+276]).hex()
    return int(input_1_Sequence, 16)

def inputNParser(data):
    input_N_txid = data[0:64]
    input_N_txid = bytes.fromhex(input_N_txid)
    input_N_txid = input_N_txid[::-1].hex()
    input_N_vout = data[64:72]
    input_N_vout = bytes.fromhex(input_N_vout)
    input_N_vout = input_N_vout[::-1].hex() 
    input_N_ScriptSigLen = bytes.fromhex(data[72:72+2]).hex()
    input_N_ScriptSigLenDec = int(input_N_ScriptSigLen, 16)
    input_N_ScriptSig = bytes.fromhex(data[74:74+(input_N_ScriptSigLenDec*2)]).hex()
    endPosScriptSigN = 74+(input_N_ScriptSigLenDec*2)
    input_N_Sequence = bytes.fromhex(data[endPosScriptSigN: endPosScriptSigN+8]).hex()
    return input_N_txid, input_N_vout, input_N_ScriptSigLenDec, input_N_ScriptSig, int(input_N_Sequence,16)

def getNumOutputs(raw_transaction_output_hex):
    num_outputs = raw_transaction_output_hex[:2]
    num_outputs = int(num_outputs, 16)
    return num_outputs

def getOutputNScriptSigLen(raw_transaction_hex):
    input_1_ScriptSigLen = bytes.fromhex(raw_transaction_hex[82:84]).hex()
    input_1_ScriptSigLen = int(input_1_ScriptSigLen, 16)
    return input_1_ScriptSigLen  

def output_N_Parser(data):
    output_N_amount = data[0:16]
    output_N_amount = bytes.fromhex(output_N_amount)
    output_N_amount = output_N_amount[::-1].hex()
    output_N_amount = int(output_N_amount, 16)
    output_N_PubKey_len = bytes.fromhex(data[16:18])[::-1].hex()
    output_N_PubKey_len = int(output_N_PubKey_len, 16)
    output_N_PubKey = bytes.fromhex(data[18:]).hex()
    return output_N_amount, output_N_PubKey_len, output_N_PubKey

###############################
########### INPUTS ############
###############################

txid_hex = raw_tx_hex_to_txid(raw_transaction_hex)
tx_version = getVersion(raw_transaction_hex)
num_inputs = getNumInputs(raw_transaction_hex)
input_1_txid = getInput1Tx(raw_transaction_hex)
input_1_vout = getInput1Vout(raw_transaction_hex)
input_1_scriptSigLen = getInput1ScriptSigLen(raw_transaction_hex)
input_1_scriptSig = getInput1ScriptSig(raw_transaction_hex)
input_1_sequence = getInput1Sequence(raw_transaction_hex)

print("\nRaw transaction hex:\n", raw_transaction_hex, "\n")
print("txid:", txid_hex)
print("Version:", tx_version)
print("\n******** Inputs ********")
print("Input count:", num_inputs )
print("\n******** Input 1 ********")
print("Input 1 txid:", input_1_txid)
print("Input 1 Vout:", input_1_vout)
print("Input 1 Script Sig Length (decimal):", input_1_scriptSigLen)
print("Input 1 Script Sig:", input_1_scriptSig)
print("Input 1 Sequence:", input_1_sequence)

#Optional Additional Inputs
input2_raw="92491ce956f3a52074ee8ab024069bc14c8396c33d8bb43de1ef1cc7f9f01a46000000008b48304502207fec947609bd275a32cfd058c76678fe868c12b681c9ab0c31f716a92ba5fed0022100cd95a9ff2036a7ee0babe268ac64b425b4490be36609452ec01c11b8eaf14665014104b5a08389cbbf01178c5451f9e1c09265e73ef7bc4a1bc6761143593134e5c6460ab31ae2d5f09140a5e95a58538fd4651cb966a86de41c1a6a79b6045ecc0312ffffffff"
input_2_txid, input_2_vout, input_2_scriptSigLen, input_2_scriptSig, input_2_sequence = inputNParser(input2_raw)

print("\n******** Input 2 ********")
print("Input 2 txid:", input_2_txid)
print("Input 2 Vout:", input_2_vout)
print("Input 2 Script Sig Length (decimal):", input_2_scriptSigLen)
print("Input 2 Script Sig:", input_2_scriptSig)
print("Input 2 Sequence:", input_2_sequence)

input3_raw = "3ca3845de7916e872570ce1676dedc3151717b7d345affa188eaa7baad3bd1a1000000006b483045022100a53211eed0e857dfab414f106190780c3791797b81aaf5a8a8f997681f6ea660022030a00ef0733bafa5f05026e027ac6f230c3929f9c766ef31edeabf2bcaed81740121036ec01e60571b5050bafb2d77063061a487228da342e996003e35ac7b5519e2e7ffffffff"
input_3_txid, input_3_vout, input_3_scriptSigLen, input_3_scriptSig, input_3_sequence = inputNParser(input3_raw)

print("\n******** Input 3 ********")
print("Input 3 txid:", input_3_txid)
print("Input 3 Vout:", input_3_vout)
print("Input 3 Script Sig Length (decimal):", input_3_scriptSigLen)
print("Input 3 Script Sig:", input_3_scriptSig)
print("Input 3 Sequence:", input_3_sequence)

###############################
########### OUTPUTS ###########
###############################

raw_transaction_output_hex = "048e2e1601000000001976a9142b18e0074aad70661b6fecf742cbefab4a145d1188ac40420f00000000001976a914a229e570ef0c11b6a20451d65047b0fbe2c96a2f88ac40420f00000000001976a91408536923b85945c704b47bb2657294757bc417dc88ac40420f00000000001976a91415c307a88533528de8414fc2fc96b4e67ac0e0ef88ac00000000"

raw_tx_out_1 = "8e2e1601000000001976a9142b18e0074aad70661b6fecf742cbefab4a145d1188ac"
raw_tx_out_2 = "40420f00000000001976a914a229e570ef0c11b6a20451d65047b0fbe2c96a2f88ac"
raw_tx_out_3 = "40420f00000000001976a91408536923b85945c704b47bb2657294757bc417dc88ac"
raw_tx_out_4 = "40420f00000000001976a91415c307a88533528de8414fc2fc96b4e67ac0e0ef88ac"

num_outputs = getNumOutputs(raw_transaction_output_hex)

output_1_amount, output_1_PubKey_len, output_1_PubKey = output_N_Parser(raw_tx_out_1)
output_2_amount, output_2_PubKey_len, output_2_PubKey = output_N_Parser(raw_tx_out_2)
output_3_amount, output_3_PubKey_len, output_3_PubKey = output_N_Parser(raw_tx_out_3)
output_4_amount, output_4_PubKey_len, output_4_PubKey = output_N_Parser(raw_tx_out_4)

# Output count: 1 byte

print("\n******** Outputs ********")
print("Number of outputs: ", num_outputs)

print("\n******** Output 1 ********")
print("Amount 1:", output_1_amount)
print("PubKey_len:", output_1_PubKey_len)
print("PubKey: ", output_1_PubKey)

print("\n******** Output 2 ********")
print("Amount 2:", output_2_amount)
print("PubKey_len:", output_2_PubKey_len)
print("PubKey: ", output_2_PubKey)

print("\n******** Output 3 ********")
print("Amount 3:", output_3_amount)
print("PubKey_len:", output_3_PubKey_len)
print("PubKey: ", output_3_PubKey)

print("\n******** Output 4 ********")
print("Amount 4:", output_4_amount)
print("PubKey_len:", output_4_PubKey_len)
print("PubKey: ", output_4_PubKey)

# Locktime 4 bytes
print("\n******** Output 2 ********")
print("Locktime:", raw_transaction_output_hex[-8:])