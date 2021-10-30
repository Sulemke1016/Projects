from random import randint						#Import randint to help with the random board generation


WHITE = '\u25a0'								#Creates variables for the black and white squares
BLACK = '\u25a1'

def main():										#Creates a main() function

	board = [	
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
	]
	randomize_board(board)
	moves = 0
	while not is_solved(board):
		show(board)
		row = solicit_row_or_column('row')
		col = solicit_row_or_column('col')
		touch(board, row, col)
		moves += 1
	show(board)
	print(f"You won with {moves} moves!")

def change_square(board, row, column):			#Creates a change_square() function to shorten total code 

	if board[row][column] == WHITE:
		board[row][column] = BLACK
	else:
		board[row][column] = WHITE 

def randomize_board(board):						#Creates a randomize_board() function

	index_board = 0 
	index = 0
	while index_board < 5:
		while index < 5:
			board[index_board][index] = WHITE
			index += 1
		index_board += 1
		index = 0

	index = 0

	while index < 10:
		
		row = randint(0, 4)
		column = randint(0, 4)

		change_square(board, row, column)		#Uses the change_square() function 
		if row != 0:
			change_square(board, row - 1, column)
		if row != 4:
			change_square(board, row + 1, column)
		if column != 0:
			change_square(board, row, column - 1)
		if column != 4:
			change_square(board, row, column + 1)
	

		index += 1


def show(entry):								#Creates a show() function to show the current board
	string_1 = ' '.join(entry[0])
	string_2 = ' '.join(entry[1])
	string_3 = ' '.join(entry[2])
	string_4 = ' '.join(entry[3])
	string_5 = ' '.join(entry[4])
		
	print(string_1)
	print(string_2)
	print(string_3)
	print(string_4)
	print(string_5)

def is_solved(entry):							#Creates a function to check if the board is solved
	

	#These variables are used to make the code shorter
	replacement = BLACK
	i = replacement 

	if entry == [[i, i, i, i, i], [i, i, i, i, i], [i, i, i, i, i], [i, i, i, i, i], [i, i, i, i, i]]:
		return(True)
	else:
		return(False)

def solicit_row_or_column(entry):				#Creates a function that asks for either a row or column number
	if entry == 'row':
		row = int(input('Please enter a row (0 - 4): '))
		while row not in [0, 1, 2, 3, 4,]:
			print('That is not a valid option.')
			row = int(input('Please enter a row (0 - 4): '))
		return row
	else:
		column = int(input('Please enter a column (0 - 4): '))
		while column not in [0, 1, 2, 3, 4,]:
			print('That is not a valid option.')
			column = int(input('Please enter a column (0 - 4): '))
		return column

def touch(board, row, column):					#Creates a simplified touch function to change the square colors 
	change_square(board, row, column)
	if row != 0:
		change_square(board, row - 1, column)
	if row != 4:
		change_square(board, row + 1, column)
	if column != 0:
		change_square(board, row, column - 1)
	if column != 4:
		change_square(board, row, column + 1)
	
main()