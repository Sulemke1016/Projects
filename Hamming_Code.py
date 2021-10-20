# take in a integer between 0 - 255 as an input
decimalInput = int(input("Please enter an integer between 0 and 255: "))

# convert the input to binary
binaryValue = bin(decimalInput)[2:].zfill(8) 

# print the 8 - bit binary number
print(binaryValue)

hammingCode = ""
finalHammingCode = ""
for bit in binaryValue:
	hammingCode += bit

# initialize variables needed for this program
eightBitValue = 0
fourBitValue = 0
twoBitValue = 0
oneBitValue = 0
finalEightBitValue = "0"
finalFourBitValue = "0"
finalTwoBitValue = "0"
finalOneBitValue = "0"

# perform the calculations to find Hamming code values
if binaryValue[0] == "1":
    eightBitValue += 1			
    fourBitValue += 1
if binaryValue[1] == "1":
    eightBitValue += 1			
    fourBitValue += 1
    oneBitValue += 1
if binaryValue[2] == "1":
    eightBitValue += 1			
    fourBitValue += 1
    twoBitValue += 1
if binaryValue[3] == "1":
    eightBitValue += 1			
    oneBitValue += 1
if binaryValue[4] == "1":			
    fourBitValue += 1
    twoBitValue += 1
    oneBitValue += 1
if binaryValue[5] == "1":			
    fourBitValue += 1
    twoBitValue += 1
if binaryValue[6] == "1":			
    fourBitValue += 1
    oneBitValue += 1
if binaryValue[7] == "1":
    twoBitValue += 1
    oneBitValue += 1

if eightBitValue % 2 == 1:
    finalEightBitValue = "1"
if fourBitValue % 2 == 1:
    finalFourBitValue = "1"
if twoBitValue % 2 == 1:
    finalTwoBitValue = "1"
if oneBitValue % 2 == 1:
    finalOneBitValue = "1"

# plug in Hamming code values
for bit in range(4):
    finalHammingCode += binaryValue[bit]
finalHammingCode += finalEightBitValue
for bit in range(4,7):
    finalHammingCode += binaryValue[bit]
finalHammingCode += finalFourBitValue + binaryValue[7] + finalTwoBitValue + finalOneBitValue 

# print final Hamming code
print(finalHammingCode)
