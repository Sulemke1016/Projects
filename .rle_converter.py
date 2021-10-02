# import what is needed
from sys import argv

# if no command line argument is inputted, declare input 
# nothing so that way the program will not run


inputValue = "nothing"

# see if there is an command line argument

try:
   with open(argv[1], "r") as file:
      inputValue = file.read()
      my_file = argv[1]

      # test to see if the file is a .rle file
      
      if my_file[-1] == "e" and my_file[-2] == "l" and my_file[-3] == "r" and my_file[-4] == ".":
         
         # determine that the file is a .rle file

         file_type = ".rleFile"

      else:

         # determine that the file is not a .rle file
         
         file_type = "not_.rleFile"

# if there is not, print message

except IndexError:
   print("""Usage: rle filename (produces filename.rle) 
 rle filename.rle (produces filename.plain)""")

# if there is a command line argument and it
# IS NOT an .rle file, compress it to a .rle file

if inputValue != "nothing" and file_type != ".rleFile":
   
   # define variables

   encodedValue = ""
   previousCharacter = inputValue[0]
   count = 0
   i = 0

   # run through each letter in the input

   while i < len(inputValue):

      char = inputValue[i]

      # check to see if the letter 
      # is the same as the previous letter

      # if the letter is different

      if char != previousCharacter:

         # add count of previous letter to encoded message

         encodedValue += str(count)

         # add previous letter to encoded message

         encodedValue += previousCharacter

         # set previous character to new value

         previousCharacter = char

         # reset count

         count = 1

         i += 1

      # if the letter is the same

      else:

         # add one to count

         count += 1

         # this is for if the number of same characters 
         # is more than 9
         
         if count == 10:

            # reset the count and add '9' plus the 
            # current character

            count = 1
            encodedValue += "9"
            encodedValue += char

         i += 1

      # print the final value and count combination

      if i == len(inputValue):

         encodedValue += str(count)

         encodedValue += previousCharacter

   # create .rle file

   rleFile = open(str(my_file) + ".rle", "w+")
   rleFile.write(encodedValue)

   # print the encoded message

   print(f"\nthe rle encoding of this message is: {encodedValue}")
   print("The file has also been changed to a .rle file!")

# if there is a command line argument and it
# IS an .rle file, decompress the file to a .plain file

elif inputValue != "nothing" and file_type != "not_.rleFile":

   # declare the variables for the decoder

   decodedValue = ""
   number_value = ""
   
   # run the decoder

   for char in inputValue:

      # check to see the type of value in the string

      if char.isdigit():

         # stores the number value

         number_value += char 

      else:

         # forms decoded value

         decodedValue += int(number_value) * char 

         # allow for new grouping of the input string

         number_value = ""

   # create .plain file

   plainFile = open(my_file.replace(".rle", ".plain"), "w+")
   plainFile.write(decodedValue)
   
   # print the decoded message

   print(f"\nthe rle decoding of this message is: {decodedValue}")
   print("The file has also been changed to a .plain file!")
