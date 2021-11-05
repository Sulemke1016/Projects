def main():

    # initialize program	
    lives = 11
    wordList = []

    # take in user input	
    word = input( "Please enter a word to use for the game: " )

    # add items to word list
    for letter in word:

        # add letter to word list
        wordList.append( letter )

    # peform process stage
    while lives > 1:

        # check if wordlist length is zero
        if len( wordList ) == 0:
            break

        # print the hangman
        printHangMan( lives )
        
        # ask for a letter to use
        item = input( "What letter do you want to choose: " )

        # test to see if item in word
        if item in wordList:

            # if so remove letter from word list
            wordList.remove( item )
    
        # if not lower lives by 1
        else:

            # lower by 1
            lives -= 1

    # if length of word list is zero display win screen
    if len( wordList ) == 0:

        # print winscreen
        print( """

  <^^^^^^^^^>
  < YOU WIN >             
  <vvvvvvvvv> 
  
Congratulations
""" )
    
    else:
        
        # if they loose, print full dead man and loss winscreen
        printHangMan( 0 )

def printHangMan( lives ):

    # display the hangman box
    if lives == 11:
        print( """
  ______
  |     |
  |     
  |
  |
  |
__|______
You have 11 lives
""" )

    if lives == 10:
        print( """
  ______
  |     |
  |     O
  |
  |
  |
__|______
You have 10 lives
""" )
	 
    if lives == 9:
        print( """
  ______
  |     |
  |     O
  |     |
  |
  |
__|______
You have 9 lives
""" )
		
    if lives == 8:
        print( """
  ______
  |     |
  |     O
  |     |/
  |
  |
__|______
You have 8 lives
""" )

    if lives == 7:
        print( """
  ______
  |     |
  |     O
  |   \\|/
  |
  |
__|______
You have 7 lives
""" )

    if lives == 6:
        print( """
  ______
  |     |
  |     O
  |   \\|/
  |     |
  |
__|______
You have 6 lives
""" )

    if lives == 5:
        print( """
  ______
  |     |
  |     O
  |   \\|/
  |     |
  |    /
__|______
You have 5 lives
""" )

    if lives == 4:
        print( """
  ______
  |     |
  |     O
  |   \\|/
  |     |
  |    /\\ 
__|______
You have 4 lives
""" )
    
    if lives == 3:
        print( """
  ______
  |     |
  |   o O 
  |   \\|/
  |     |
  |    /\\ 
__|______
You have 3 lives
""" )

    if lives == 2:
        print( """
  ______
  |     |
  |   o O o
  |   \\|/
  |     |
  |    /\\ 
__|______
You have two lives
""" )

    if lives == 1:
        print( """
  ______
  |     |
  |   o O o
  |   \\|/
  |     |
  |   o/\\ 
__|______
You have 1 life
""" )

 
    if lives == 0:
        print( """
  ______
  |     |
  |   o O o   <^^^^^^^^^^>
  |   \\|/    < YOU LOSE >  
  |     |     <vvvvvvvvvv>
  |   o/\\o  
__|______
""" )

main()