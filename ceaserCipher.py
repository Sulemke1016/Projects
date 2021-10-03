# import argv
from sys import argv

# global constants
NO_CMD_ARG1 = "no value"
NO_CMD_ARG2 = "no value"
ALPHA_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMBER_LIST = "0123456789"
SYMBOL_LIST = "!@#$%^&*()_-+={|[}];:,<.>/?~`"

# declare input as empty
inputString = NO_CMD_ARG1
code_value = NO_CMD_ARG2

# test to see if there is an input
try:
	with open(argv[1], "r") as file:
		inputString = file.read()

		code_value = argv[2]

except IndexError:
	print("""\nThis is a program that runs the Ceaser cipher. 
If you did not enter the correct number of command line 
argurments, please enter two; a file and code number.""")


# declare variable for the encoded message
encodedMessage = ""

# if there are two cmd arguments
if inputString != NO_CMD_ARG1 and code_value != NO_CMD_ARG2:

	# convert to the encoded message
	for char in inputString:

		# if number
		if char in NUMBER_LIST:

			index = NUMBER_LIST.index(char)

			if index + int(code_value) < len(NUMBER_LIST):
				encodedMessage += NUMBER_LIST[index + int(code_value)]
			else:
				index -= (len(NUMBER_LIST) + 1)
				encodedMessage += NUMBER_LIST[index + int(code_value)]

		# if letter
		elif char in ALPHA_LIST:

			index = ALPHA_LIST.index(char)

			if index + int(code_value) < len(ALPHA_LIST):
				encodedMessage += ALPHA_LIST[index + int(code_value)]
			else:
				index -= (len(ALPHA_LIST) + 1)
				encodedMessage += ALPHA_LIST[index + int(code_value)]

		# if symbol
		elif char in SYMBOL_LIST:
			index = SYMBOL_LIST.index(char)

			if index + int(code_value) < len(SYMBOL_LIST):
				encodedMessage += SYMBOL_LIST[index + int(code_value)]
			else:
				index -= (len(SYMBOL_LIST) + 1)
				encodedMessage += SYMBOL_LIST[index + int(code_value)]
		
		else:
			encodedMessage += char

	# create a file containing the encoded message
	newFile = open("ceaserCipher.txt", "w+")
	newFile.write(encodedMessage)

	# print out the encoded message on the screen
	print(f"\nThe new encoded message is: {encodedMessage}")






