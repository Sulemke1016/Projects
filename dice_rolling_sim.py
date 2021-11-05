import random

# ask the user if they want to roll
inputPrompt = input( "Do you want to roll? (Y/n): " )

# repeatedly ask the user to put in an input
while inputPrompt == 'Y' or inputPrompt == 'y':

	# randomly select a value for the die
	randomVal = random.randint( 1, 6 )

	# print the dice value
	if randomVal == 1:
		print( """    
    _ _ _ _ _
  /         /|
 /         / |	
/_ _ _ _ _/  |
|         |  |
|         |  |
|    o    |  /
|         | /
|_ _ _ _ _|/
""" )
	
	if randomVal == 2:
		print( """    
    _ _ _ _ _
  /         /|
 /         / |	
/_ _ _ _ _/  |
|         |  |
|  o      |  |
|         |  /
|      o  | /
|_ _ _ _ _|/
""" )
	
	if randomVal == 3:
		print( """    
    _ _ _ _ _
  /         /|
 /         / |	
/_ _ _ _ _/  |
|         |  |
|  o      |  |
|    o    |  /
|      o  | /
|_ _ _ _ _|/
""" )
	
	if randomVal == 4:
		print( """    
    _ _ _ _ _
  /         /|
 /         / |	
/_ _ _ _ _/  |
|         |  |
|  o   o  |  |
|         |  /
|  o   o  | /
|_ _ _ _ _|/
""" )
	if randomVal == 5:
		print( """    
    _ _ _ _ _
  /         /|
 /         / |	
/_ _ _ _ _/  |
|         |  |
|  o   o  |  |
|    o    |  /
|  o   o  | /
|_ _ _ _ _|/
""" )
	
	if randomVal == 6:
		print( """    
    _ _ _ _ _
  /         /|
 /         / |	
/_ _ _ _ _/  |
|         |  |
|  o   o  |  |
|  o   o  |  /
|  o   o  | /
|_ _ _ _ _|/
""" )

	# display their roll value
	print( f"You rolled a { randomVal }." )

	# ask them if they want to roll again
	inputPrompt = input( "Do you want to roll? (Y/n): " )

# end program
print( "End program\nI hope you had fun." )

