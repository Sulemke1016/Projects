# take in inputs for the two variables, a and b 

aValue = int(input("Please enter an integer, we will call this 'Input A': "))
bValue = int(input("Please enter an integer, we will call this 'Input B': "))

# create functions that convert from one type to another

def binaryToDecimal(inputVal):
	decVal = int(str(inputVal), 2)

	return(decVal)

def binaryToHex(inputVal):
	decVal = int(str(inputVal), 2)
	hexVal = hex(decVal)[2:]

	return(hexVal)

def decimalToBinary(inputVal):
	binaryVal = bin(inputVal)[2:].zfill(8)

	return(binaryVal)

def decimalToHex(inputVal):
	hexVal = hex(inputVal)[2:]

	return(hexVal)

def hexToBinary(inputVal):
	decVal = int(str(inputVal), 16)
	binaryVal = bin(decVal)[2:].zfill(8)

	return(binaryVal)

def hexToDecimal(input):
	decVal = int(str(inputVal), 16)

	return(decVal)

# create functions that perform the bitwise operations

def ANDbitwiseOperation(a, b):
	aDecimal = decimalToBinary(a)
	bDecimal = decimalToBinary(b)
	finalString = ""
	for i in range (8):
		if aDecimal[i] == "1" and bDecimal[i] == "1":
			finalString += "1"
		else:
			finalString += "0"
	return finalString

def ORbitwiseOperation(a, b):
	aDecimal = decimalToBinary(a)
	bDecimal = decimalToBinary(b)
	finalString = ""
	for i in range (8):
		if aDecimal[i] == "1" or bDecimal[i] == "1":
			finalString += "1" 
		else:
			finalString += "0"
	return finalString

def XORbitwiseOperation(a, b):
	aDecimal = decimalToBinary(a)
	bDecimal = decimalToBinary(b)
	finalString = ""
	for i in range (8):
		if aDecimal[i] == "1" and bDecimal[i] == "1":
			finalString += "0"
		elif aDecimal[i] == "0" and bDecimal[i] == "0":
			finalString += "0"
		else:
			finalString += "1"
	return finalString

def complementBitwiseOperation(a):
	aDecimal = decimalToBinary(a)
	finalString = ""
	for i in range (8):
		if aDecimal[i] == "1":
			finalString += "0"
		else:
			finalString += "1"
	return finalString

def shiftLeftBitwiseOperation(a, b):
	shiftedValue = a << b
	binaryValue = decimalToBinary(shiftedValue)
	if len(binaryValue) > 8:
		for i in range(len(binaryValue) - 8):
			binaryValue = binaryValue[1:] 
	return binaryValue


def shiftRightBitwiseOperation(a, b):
	shiftedValue = a >> b
	binaryValue = decimalToBinary(shiftedValue)
	if len(binaryValue) > 8:
		for i in range(len(binaryValue) - 8):
			binaryValue = binaryValue[:-1] 
	return binaryValue

# print table that contains the bitwise function outputs

print("=" * 35)
print("The & of input A and input B is:")
print("Decimal: ")
print(binaryToDecimal(ANDbitwiseOperation(aValue, bValue)))
print("Binary: ")
print(ANDbitwiseOperation(aValue, bValue))
print("Hex: ")
print(binaryToHex(ANDbitwiseOperation(aValue, bValue)))

print("=" * 35)
print("The | of input A and input B is:")
print("Decimal: ")
print(binaryToDecimal(ORbitwiseOperation(aValue, bValue)))
print("Binary: ")
print(ORbitwiseOperation(aValue, bValue))
print("Hex: ")
print(binaryToHex(ORbitwiseOperation(aValue, bValue)))

print("=" * 35)
print("The ^ of input A and input B is:")
print("Decimal: ")
print(binaryToDecimal(XORbitwiseOperation(aValue, bValue)))
print("Binary: ")
print(XORbitwiseOperation(aValue,bValue))
print("Hex: ")
print(binaryToHex(XORbitwiseOperation(aValue, bValue)))

print("=" * 35)
print("The ~ of input A is:")
print("Decimal: ")
print(binaryToDecimal(complementBitwiseOperation(aValue)))
print("Binary: ")
print(complementBitwiseOperation(aValue))
print("Hex: ")
print(binaryToHex(complementBitwiseOperation(aValue)))

print("=" * 35)
print("The << of input A and input B is:")
print("Decimal: ")
print(binaryToDecimal(shiftLeftBitwiseOperation(aValue, bValue)))
print("Binary: ")
print(shiftLeftBitwiseOperation(aValue, bValue))
print("Hex: ")
print(binaryToHex(shiftLeftBitwiseOperation(aValue, bValue)))

print("=" * 35)
print("The >> of input A and input B is:")
print("Decimal: ")
print(binaryToDecimal(shiftRightBitwiseOperation(aValue, bValue)))
print("Binary: ")
print(shiftRightBitwiseOperation(aValue, bValue))
print("Hex: ")
print(binaryToHex(shiftRightBitwiseOperation(aValue, bValue)))











