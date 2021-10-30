# import necessary modules
from ctypes import c_uint8 as uint8
from struct import pack
from struct import unpack
from textwrap import wrap

# take an input from the user
text = input( "\nEnter an input string into this program: " )

# print a underline
print( "========================================\n" )

# create a list of potential ASCII numbers and binary numbers
asciiList = []
binaryList = []

# create int list for later use
intList = []

# iterate through the characters in the input
for char in text:

    # find the decimal ASCII code for the given character
    asciiVal = ord( char )

    # turn that decimal value into hex
    asciiHexVal = hex( asciiVal ).split( 'x' )[-1]

    # find the binary version of the corresponding ASCII code
    binaryLetter = bin( asciiVal )[2:].zfill( 8 )

    # add that hex value to a list
    asciiList.append( asciiHexVal )

    # add the binary values to a list
    binaryList.append( binaryLetter )

    # add int values to a list
    intList.append( asciiVal )

# print the original data entry
print( f"Original data:  {text}" )

# add a space
print()

# print the ASCII code of each character in the input
print( f"ASCII codes:    ", end = "" )

for char in range( len( text ) ):
    
    print( f"{text[char]} = ${asciiList[char]}", end = "   " ) 

# move to next line
print()

# print the binary value of each character in the input
print( f"In binary:      ", end = "" )

for char in range( len( text ) ):

    print( f"{binaryList[char]}", end = "  " ) 

# move to next line
print( "\n" )

# print the groups of 8
print( f"Groups of 8:    ", end = "" )

for char in range( len( text ) ):

    print( f"{binaryList[char]}", end = "  " ) 

print("\n")

#--------------------#
# CREATE GROUPS OF 6 #
#--------------------#

# separate groups of 8 into three byte chunks

# declare a list to store the 6 bit segments into
sixBitBinList = []

# once broken into 3 byte segments, check to see if the input string is a multiple of 3 in length
# if it is:
if len( intList ) % 3 == 0:
    wholeChunks = len( intList ) / 3

    print( "Groups of 6:    ", end = "" )
    # perform the shifting operations to translate a byte to 6 bits
    for i in range( int( wholeChunks ) ):
        grpSixFirst = intList[0] >> 2
        grpSixSecond = ( ( ( intList[0] << 6 ) & uint8( -1 ).value ) >> 2 ) + ( intList[1] >> 4 )
        grpSixThird = ( ( ( intList[1] << 4 ) & uint8( -1 ).value ) >> 2 ) + ( intList[2] >> 6 )
        grpSixFourth = ( ( ( intList[2] << 2 ) & uint8( -1 ).value ) >> 2 ) 

        # convert the integer, shifted values to binary
        binGrpSixFirst = bin( grpSixFirst )[2:].zfill( 6 )
        binGrpSixSecond = bin( grpSixSecond )[2:].zfill( 6 )
        binGrpSixThird = bin( grpSixThird )[2:].zfill( 6 )
        binGrpSixFourth = bin( grpSixFourth )[2:].zfill( 6 )

        # del those tested values from the list that way it is possible to run the shifts on new numbers
        del intList[0:3]

        # store the 6 bit segments in a list for later use
        sixBitBinList.append( binGrpSixFirst )
        sixBitBinList.append( binGrpSixSecond )
        sixBitBinList.append( binGrpSixThird )
        sixBitBinList.append( binGrpSixFourth )
        
        # print the 6 bit segments
        if i == 0:
            print( f"{binGrpSixFirst} {binGrpSixSecond} {binGrpSixThird} {binGrpSixFourth}" )
        else:
            print( f"                {binGrpSixFirst} {binGrpSixSecond} {binGrpSixThird} {binGrpSixFourth}" )

# input length / 3 has a remainder of 1
elif len( intList ) % 3 == 1:
    wholeChunks = ( len( intList ) - 1 ) / 3

    print( "Groups of 6:    ", end = "" )
    # perform the shifting operations to translate a byte to 6 bits
    for i in range( int( wholeChunks ) ):
        grpSixFirst = intList[0] >> 2
        grpSixSecond = ( ( ( intList[0] << 6 ) & uint8( -1 ).value ) >> 2 ) + ( intList[1] >> 4 )
        grpSixThird = ( ( ( intList[1] << 4 ) & uint8( -1 ).value ) >> 2 ) + ( intList[2] >> 6 )
        grpSixFourth = ( ( ( intList[2] << 2 ) & uint8( -1 ).value ) >> 2 ) 
        
        # convert the integer, shifted values to binary
        binGrpSixFirst = bin( grpSixFirst )[2:].zfill( 6 )
        binGrpSixSecond = bin( grpSixSecond )[2:].zfill( 6 )
        binGrpSixThird = bin( grpSixThird )[2:].zfill( 6 )
        binGrpSixFourth = bin( grpSixFourth )[2:].zfill( 6 )

        # del those tested values from the list that way it is possible to run the shifts on new numbers
        del intList[0:3]

        # store the 6 bit segments in a list for later use
        sixBitBinList.append( binGrpSixFirst )
        sixBitBinList.append( binGrpSixSecond )
        sixBitBinList.append( binGrpSixThird )
        sixBitBinList.append( binGrpSixFourth )
        
        # print the 6 bit segments
        if i == 0:
            print( f"{binGrpSixFirst} {binGrpSixSecond} {binGrpSixThird} {binGrpSixFourth}" )
        else:
            print( f"                {binGrpSixFirst} {binGrpSixSecond} {binGrpSixThird} {binGrpSixFourth}" )

    # for the remaining bits store into 6 bit segments, if no bits left represent those spaces with 'x'
    leftoverOne = intList[0] >> 2
    leftoverTwo = ( ( ( intList[0] << 6 ) & uint8( -1 ).value ) >> 6 ) 
    
    leftoverGrpSixFirst = bin( leftoverOne )[2:].zfill( 6 )
    leftoverGrpSixSecond = bin( leftoverTwo )[2:].zfill( 2 ) + "xxxx"
    leftoverGrpSixThird = "xxxxxx"
    leftoverGrpSixFourth = "xxxxxx"

    # print the remaining 6 bit segments
    print( f"                {leftoverGrpSixFirst} {leftoverGrpSixSecond} {leftoverGrpSixThird} {leftoverGrpSixFourth}" )

    # store the remaining 6 bit segments in a list for later use
    sixBitBinList.append( leftoverGrpSixFirst )
    sixBitBinList.append( leftoverGrpSixSecond )
    sixBitBinList.append( leftoverGrpSixThird )
    sixBitBinList.append( leftoverGrpSixFourth )

# input length / 3 has a remainder of 2
else:
    wholeChunks = ( len( intList ) - 2 ) / 3

    print( "Groups of 6:    ", end = "" )
    # perform the shifting operations to translate a byte to 6 bits
    for i in range( int( wholeChunks ) ):
        grpSixFirst = intList[0] >> 2
        grpSixSecond = ( ( ( intList[0] << 6 ) & uint8( -1 ).value ) >> 2 ) + ( intList[1] >> 4 )
        grpSixThird = ( ( ( intList[1] << 4 ) & uint8( -1 ).value ) >> 2 ) + ( intList[2] >> 6 )
        grpSixFourth = ( ( ( intList[2] << 2 ) & uint8( -1 ).value ) >> 2 )
        
        # convert the integer, shifted values to binary
        binGrpSixFirst = bin( grpSixFirst )[2:].zfill( 6 )
        binGrpSixSecond = bin( grpSixSecond )[2:].zfill( 6 )
        binGrpSixThird = bin( grpSixThird )[2:].zfill( 6 )
        binGrpSixFourth = bin( grpSixFourth )[2:].zfill( 6 )

        # del those tested values from the list that way it is possible to run the shifts on new numbers
        del intList[0:3]

        # store the 6 bit segments in a list for later use
        sixBitBinList.append( binGrpSixFirst )
        sixBitBinList.append( binGrpSixSecond )
        sixBitBinList.append( binGrpSixThird )
        sixBitBinList.append( binGrpSixFourth )
        
        # print the 6 bit segments
        if i == 0:
            print( f"{binGrpSixFirst} {binGrpSixSecond} {binGrpSixThird} {binGrpSixFourth}" )
        else:
            print( f"                {binGrpSixFirst} {binGrpSixSecond} {binGrpSixThird} {binGrpSixFourth}" )


    # for the remaining bits store into 6 bit segments, if no bits left represent those spaces with 'x'
    leftoverOne = intList[0] >> 2
    leftoverTwo = ( ( ( intList[0] << 6 ) & uint8( -1 ).value ) >> 2 ) | ( intList[1] >> 4 )
    leftoverThree = ( ( ( intList[1] << 4 ) & uint8( -1 ).value ) >> 4 )
    
    leftoverGrpSixFirst = bin( leftoverOne )[2:].zfill( 6 )
    leftoverGrpSixSecond = bin( leftoverTwo )[2:].zfill( 6 ) 
    leftoverGrpSixThird = bin( leftoverThree )[2:].zfill( 4 ) + "xx"
    leftoverGrpSixFourth = "xxxxxx"

    # print the remaining 6 bit segments
    print( f"                {leftoverGrpSixFirst} {leftoverGrpSixSecond} {leftoverGrpSixThird} {leftoverGrpSixFourth}" )

    # store the remaining 6 bit segments in a list for later use
    sixBitBinList.append( leftoverGrpSixFirst )
    sixBitBinList.append( leftoverGrpSixSecond )
    sixBitBinList.append( leftoverGrpSixThird )
    sixBitBinList.append( leftoverGrpSixFourth )

# declare a list to store the decimal forms of the 6 bit segments in for later use
decList = []

# for each item, covert to its decimal counterpart
for item in sixBitBinList:

    # in the case of "xxxxxx" convert to "N/A"
    if item == "xxxxxx":
        finalCode = "N/A"

    # with some 'x' values convert them to '0'
    elif 'x' in item and item != "xxxxxx":
        code = item.replace( 'x', '0' )
        finalCode = int( str( code ), 2 )

    # otherwise just convert to decimal
    else:
        code = item
        finalCode = int( str( code ), 2 )

    # store the converted values in a list
    decList.append( finalCode )

# print the base 10 values after they are converted
print( "\nIn Base 10:     ", end = "" )

for char in range( len( decList ) ):

    print( f"{decList[char]}", end = " " )

# declare a string of base64 as reference
base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# make a list to store the base64 values in
base64List = [] 

# covert to base 64
for item in decList:

    # if the value is a decimal integer covert to base 64
    if type(item) == int:
        base64List.append(base64[item])
    
    # if it is "N/A", covert to '='
    else:
        base64List.append('=')

# print the base64 code
print( "\nBase 64 Output: ", end = "" )

for char in range( len( base64List ) ):

    print( f"{base64List[char]}", end = "" )

# add some space for aesthetic purposes
print('\n')

####################################################
# NOW WE CONVERT BACK TO THE ORIGINAL INPUT STRING #
####################################################

# declare an input for base 64
base64input = input( "Please Enter the base64 value you entered w/out the '=':   ")
print( "========================================================" )


# declare a list for later use to store the decimal values in
decListConvertBack = []

# convert from base 64 to decimal
for item in base64input:

    # store decimal value in list
    decConvert = base64.index( item )
    decListConvertBack.append( decConvert )

# declare a list to store the 6 bit segments in
listofSixBitSegments = []

# convert to 6 bit segments 
for item in decListConvertBack:

    sixBitSegement = bin( item )[2:].zfill( 6 ) 
    listofSixBitSegments.append( sixBitSegement )

# declare empty string
fullStringOfSixBitSegments = ""

# add to string
for item in listofSixBitSegments:
    fullStringOfSixBitSegments += item

while len( fullStringOfSixBitSegments ) % 8 != 0:
    fullStringOfSixBitSegments = fullStringOfSixBitSegments[:-1]

while len( fullStringOfSixBitSegments ) % 24 != 0:
    fullStringOfSixBitSegments += 'x'

listofSixBitSegments = wrap( fullStringOfSixBitSegments, 6 )

# print the groups of 6
print( f"\nGroups of 6:    ", end = "" )

# print the 6 bit segments
for char in range( len( listofSixBitSegments ) ):
    
    if char != 0:
        if ( char + 1 ) % 4 != 0:
            print( f"{listofSixBitSegments[char]}", end = " " )
        else:
            print( f"{listofSixBitSegments[char]}" ) 
        if ( char + 1 ) % 4 == 0:
            print( "               ", end = " " )
    else:
        print( f"{listofSixBitSegments[char]}", end = " " )

# add a space for aesthetic purposes
print()

# declare a list to be used later to store bytes
eightBitBinList = []

# if there are a multiple of 4, 6 bit segments
if len( decListConvertBack ) % 4 == 0:
    wholeChunks = len( decListConvertBack ) / 4

    print( f"Groups of 8:    ", end = "")
    for i in range( int(wholeChunks) ):

        # shift from 6 bit to 8 bit
        grpEightFirst = ( ( decListConvertBack[0] << 2 ) & uint8( -1 ).value ) + ( decListConvertBack[1] >> 4 )
        grpEightSecond = ( ( decListConvertBack[1] << 4 ) & uint8( -1 ).value ) + ( decListConvertBack[2] >> 2 )
        grpEightThird = ( ( decListConvertBack[2] << 6 ) & uint8( -1 ).value ) + decListConvertBack[3]

        # convert the integer, shifted values to binary
        binGrpEightFirst = bin( grpEightFirst )[2:].zfill( 8 )
        binGrpEightSecond = bin( grpEightSecond )[2:].zfill( 8 )
        binGrpEightThird = bin( grpEightThird )[2:].zfill( 8 )

        # delete indexes so that way more can be iterated on
        del decListConvertBack[0:4]

        # add values to list
        eightBitBinList.append( binGrpEightFirst )
        eightBitBinList.append( binGrpEightSecond )
        eightBitBinList.append( binGrpEightThird )

        # print the 6 bit segments
        if i == 0:
            print( f"{binGrpEightFirst} {binGrpEightSecond} {binGrpEightThird}" )
        else:
            print( f"                {binGrpEightFirst} {binGrpEightSecond} {binGrpEightThird}" )

#
if len( decListConvertBack ) % 4 == 2:
    wholeChunks = len( decListConvertBack ) / 4

    print( f"Groups of 8:    ", end = "")
    for i in range( int(wholeChunks) ):

        # shift from 6 bit to 8 bit
        grpEightFirst = ( ( decListConvertBack[0] << 2 ) & uint8( -1 ).value ) + ( decListConvertBack[1] >> 4 )
        grpEightSecond = ( ( decListConvertBack[1] << 4 ) & uint8( -1 ).value ) + ( decListConvertBack[2] >> 2 )
        grpEightThird = ( ( decListConvertBack[2] << 6 ) & uint8( -1 ).value ) + decListConvertBack[3]

        # convert the integer, shifted values to binary
        binGrpEightFirst = bin( grpEightFirst )[2:].zfill( 8 )
        binGrpEightSecond = bin( grpEightSecond )[2:].zfill( 8 )
        binGrpEightThird = bin( grpEightThird )[2:].zfill( 8 )

        # delete indexes so that way more can be iterated on
        del decListConvertBack[0:4]

        # add values to list
        eightBitBinList.append( binGrpEightFirst )
        eightBitBinList.append( binGrpEightSecond )
        eightBitBinList.append( binGrpEightThird )

        
        # print the 6 bit segments
        if i == 0:
            print( f"{binGrpEightFirst} {binGrpEightSecond} {binGrpEightThird}" )
        else:
            print( f"                {binGrpEightFirst} {binGrpEightSecond} {binGrpEightThird}" )

    # convert remaining 6 bit segments to bytes
    leftoverOne = ( ( decListConvertBack[0] << 2 ) & uint8( -1 ).value ) + ( decListConvertBack[1] >> 4 )
    
    leftoverGrpEightFirst = bin( leftoverOne )[2:].zfill( 8 )

    eightBitBinList.append( leftoverGrpEightFirst )
    
    # print out the final byte(s)
    print( f"                {leftoverGrpEightFirst}")

if len( decListConvertBack ) % 4 == 3:
    wholeChunks = len( decListConvertBack ) / 4

    print( f"Groups of 8:    ", end = "")
    for i in range( int(wholeChunks) ):

        # shift from 6 bit to 8 bit
        grpEightFirst = ( ( decListConvertBack[0] << 2 ) & uint8( -1 ).value ) + ( decListConvertBack[1] >> 4 )
        grpEightSecond = ( ( decListConvertBack[1] << 4 ) & uint8( -1 ).value ) + ( decListConvertBack[2] >> 2 )
        grpEightThird = ( ( decListConvertBack[2] << 6 ) & uint8( -1 ).value ) + decListConvertBack[3]

        # convert the integer, shifted values to binary
        binGrpEightFirst = bin( grpEightFirst )[2:].zfill( 8 )
        binGrpEightSecond = bin( grpEightSecond )[2:].zfill( 8 )
        binGrpEightThird = bin( grpEightThird )[2:].zfill( 8 )
        
        # delete indexes so that way more can be iterated on
        del decListConvertBack[0:4]

        # add values to list
        eightBitBinList.append( binGrpEightFirst )
        eightBitBinList.append( binGrpEightSecond )
        eightBitBinList.append( binGrpEightThird )

        # print the 6 bit segments
        if i == 0:
            print( f"{binGrpEightFirst} {binGrpEightSecond} {binGrpEightThird}" )
        else:
            print( f"                {binGrpEightFirst} {binGrpEightSecond} {binGrpEightThird}" )

    # convert remaining 6 bit segments to bytes
    leftoverOne = ( ( decListConvertBack[0] << 2 ) & uint8( -1 ).value ) + ( decListConvertBack[1] >> 4 )
    leftoverTwo = ( ( decListConvertBack[1] << 4 ) & uint8( -1 ).value ) + ( decListConvertBack[2] >> 2 )
    
    leftoverGrpEightFirst = bin( leftoverOne )[2:].zfill( 8 )
    leftoverGrpEightSecond = bin( leftoverTwo )[2:].zfill( 8 )

    eightBitBinList.append( leftoverGrpEightFirst )
    eightBitBinList.append( leftoverGrpEightSecond )
    
    # print out the final byte(s)
    print( f"                {leftoverGrpEightFirst} {leftoverGrpEightSecond}")

# declare a list to store decimal numbers
decimalList = []

# convert the 8 bit binary numbers into decimal
for item in eightBitBinList:
    decimalVal = int( str( item ), 2 )
    decimalList.append( decimalVal )

# declare list to store original data
origList = []

# convert to original data
for item in decimalList:
    origVal = chr( item )
    origList.append( origVal )

# declare string to store original value as the final solution
finalValue = ""
for item in origList:
    finalValue += item

# print out the original data
print( f"\nOriginal data:  {finalValue}")
