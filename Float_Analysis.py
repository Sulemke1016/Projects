from ctypes import c_uint8 as uint8
from ctypes import c_uint32 as uint32
from struct import pack
from struct import unpack

inputValue = input("Enter real Number: ") # notice the input is a string

#####################################################
# START OF YOUR SKELETON
#####################################################
# getting representation of a float (double)
fpbytes = pack(">f", float(inputValue))
fpbytes
list(fpbytes)
fp = "".join([f"{b:08b}" for b in fpbytes])
fp

# repacking the bytes of the float (double) into 64-bit unsigned
fpbin = unpack(">L", fpbytes)
fpuint = uint32(fpbin[0]).value

# extracting the sign, exponent, and significand fields
if inputValue == "-0":
   signbit = 1
else:
   signbit = fpuint >> 31                          # I changed some of the bitwise operands 
exponent = (fpuint << 1) & uint32(-1).value
exponent = exponent >> 24                           # here as well
significand = (fpuint << 9) & uint32(-1).value      # here
significand = significand >> 9                      # and here

####################################################
# END OF YOUR SKELETON
####################################################

# print float analysis
print("Float Analysis")

# print the labels for the bit pattern
print(f"  Bit Pattern:     {signbit} {exponent:08b} {significand:023b}")
print( "                   S Exponent Significand/Mantissa")

# find the sign
if float(inputValue) > 0:
   sign = "positive"
elif inputValue == "0":
   sign = "positive"
elif inputValue == "-0":
   sign = "negative"
else:
   sign = "negative"

# print the sign
if inputValue != "0" and inputValue != "-0":
   print(f"\n  Sign:            {signbit} ({sign}) ")

# print the exponent and its bias
if inputValue != "0" and inputValue != "-0":	
   print(f"  Exponent:        {exponent:08b} = {exponent}; w/bias 127 -> ({exponent} - 127) = {exponent - 127}")

# print the significand
if inputValue != "0" and inputValue != "-0":
   print(f"  Significand:     {significand:023b}")
   print(f"     w/ implied:   1.{significand:023b}\n")

# print the comnbined value
if inputValue != "0" and inputValue != "-0":
   print(f"  Combined:        + [1.{significand:023b}] * 2 ^ {exponent - 127}")

# print its decimal breakdown
significand = f"{significand:023b}"

# determine the fraction breakdown, somewhat tedious process
fractionList = []
if significand[0] == "1":
   fractionList.append("1/2")
if significand[1] == "1":
   fractionList.append("1/4")
if significand[2] == "1":
   fractionList.append("1/8")
if significand[3] == "1":
   fractionList.append("1/16")
if significand[4] == "1":
   fractionList.append("1/32")
if significand[5] == "1":
   fractionList.append("1/64")
if significand[6] == "1":
   fractionList.append("1/128")
if significand[7] == "1":
   fractionList.append("1/256")
if significand[8] == "1":
   fractionList.append("1/512")
if significand[9] == "1":
   fractionList.append("1/1024")
if significand[10] == "1":
   fractionList.append("1/2048")
if significand[11] == "1":
   fractionList.append("1/4096")
if significand[12] == "1":
   fractionList.append("1/8192")
if significand[13] == "1":
   fractionList.append("1/2^14")
if significand[14] == "1":
   fractionList.append("1/2^15")
if significand[15] == "1":
   fractionList.append("1/2^16")
if significand[16] == "1":
   fractionList.append("1/2^17")
if significand[17] == "1":
   fractionList.append("1/2^18")
if significand[18] == "1":
   fractionList.append("1/2^19")
if significand[19] == "1":
   fractionList.append("1/2^20")
if significand[20] == "1":
   fractionList.append("1/2^21")
if significand[21] == "1":
   fractionList.append("1/2^22")
if significand[22] == "1":
   fractionList.append("1/2^23")

# writing the final fraction breakdown
if len(fractionList) == 0:
   if inputValue != "0" and inputValue != "-0":
      print(f"     or:           + [1] * 2 ^ {exponent - 127}")
else:
   print(f"     or:           + [1 + ({fractionList[0]})", end = "")
   for item in range(1, len(fractionList)):
      print(f" + ({fractionList[item]})", end = "")
   print("]")

# accounting for 0 and -0
if inputValue == "0" or inputValue == "-0":
   print(f"\n\t\t   This is a special case for {inputValue}")



