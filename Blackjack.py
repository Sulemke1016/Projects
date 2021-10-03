# ___        _       _          _ ___   _   _        _  #
#  |  |_| | |_    | |_    |\ | | | |   | \ | | |\ | |_  #
#  |  | | |  _|   |  _|   | \| |_| |   |_/ |_| | \| |_  #
#-------------------------------------------------------#

import random 

# declare the variables needed to run this program

# lists
deck = []
players_list = []

# integers
player_number = 0

# dictionaries
player_bet = {}
players = {}
player_hand = {}
dealer_hand = {}


# this function creates a deck of cards
# the cards do not have suits assigned to them, just number values
# the ace only works as one so far
def create_deck():
	
	count = 1
	suit = 0
	while count < 11:
		if suit == 0:
			deck.append(count)
			suit = suit + 1
		elif suit == 1:
			deck.append(count)
			suit = suit + 1
		elif suit == 2:
			deck.append(count)
			suit = suit + 1
		else:
			deck.append(count)
			suit = 0
			count = count + 1
	for i in range(1, 13):
		deck.append(10)
	return deck

# this function prints the number of cards in the deck
# this is made for testing purposes
def deck_count():
	count = 0
	for i in deck:
		count += 1
	print(count)

# this function asks the user how much they would like to bet
# if the user does not enter in a valid number, it prompts them again
def player_bet_func():
	for player in players:
		money = players[player]
		bet = float(input(f"How much would you like to bet {player}: "))
		if bet > money and bet > 0:
			second_bet = input("You do not have that much money, bet again: ")
			player_bet[player] = second_bet
		elif bet < 0:
			second_bet = input("Bet again, you cannot bet negative: ")
			player_bet[player] = second_bet
		elif type(bet) != float:
			second_bet = input("Please enters a number: ")
			player_bet[player] = second_bet
		elif bet == 0:
			second_bet = input("Bet again, you cannot bet nothing: ")
			player_bet[player] = second_bet
		else:
			player_bet[player] = bet

# function to add a player to the game
def add_player(player, money):
	players[player] = money

# function to create a players hand
def add_hand(player, hand):
	player_hand[player] = hand

# function that checks to see if a player has busted
def check_for_bust(player, hand, money, bet):
	hand_value = 0
	for card in hand:
		hand_value += card
		
		# you bust
		if hand_value > 21:
			print("You bust")
			players[player] = float(money) - float(bet)
			del player_hand[player]
			if players[player] == 0:
				print("You lost")
				print(players)
				break
			print(players)

		# you get blackjack
		elif hand_value == 21:
			print("BLACKJACK!")
			players[player] = money + bet * 2.5
			del player_hand[player]
			print(player_hand)
			print(players)
			
# function that defines what a hit and stay are
# if the user hits, the program runs fine
# if the user stays, code has not been written for them to compare to the dealer
def hit_conditions(player, hand, money, bet, prompt):
	if prompt == "hit" or prompt == "Hit":
		if len(deck) > 0:
			hand.append(deck[0])
			deck.pop(0)
		else:
			create_deck()
			hand.append(deck[0])
			deck.pop(0)
		add_hand(player, hand)
		print(player_hand)
		print(players)
		check_for_bust(player, hand, money, bet)			
		if player in player_hand:
			hit_or_stay(player, hand, money, bet)
	elif prompt == "stay" or prompt == "Stay":
		print("You stayed.")

# function to see if the user wants to hit or stay
def hit_or_stay(player, hand, money, bet):
	check_for_bust(player, hand, money, bet)
	if player in player_hand:
		prompt = input(f"{player}, would you like to hit or stay: ")
		hit_conditions(player, hand, money, bet, prompt)
	else:
		hit_conditions(player, hand, money, bet, prompt)

# this is a function that deals the cards to each player
# it removes cards from the deck as it deals
def deal():
	for player in players:
		hand = []
		money = players[player]
		bet = player_bet[player]
		if len(deck) > 0:
			hand.append(deck[0])
			deck.pop(0)
		else:
			create_deck()
			hand.append(deck[0])
			deck.pop(0)
		add_hand(player, hand)

		if len(deck) > 0:
			hand.append(deck[0])
			deck.pop(0)
		else:
			create_deck()
			hand.append(deck[0])
			deck.pop(0)
		add_hand(player, hand)
		print(player_hand)
		print(players)
		hit_or_stay(player, hand, money, bet)

# function that initializes the game
# it prompts the user for the number of players, their names, and their bet
# just like real blackjack	
def intinalize_game():
	numb_p = int(input("How many players are playing: "))
	player_number = numb_p
	count = 0
	while count < numb_p:
		name = input(f"What is your name, player {count + 1}: ")
		mula = float(input("How much money are you playing with: "))
		add_player(name, mula)
		players_list.append(name)
		count = count + 1

# if the user busts they can play again, if they have money
def play_again():
	again = input("Play another round: ")
	if again == "yes" or again == "Yes":
		print("Good luck!")
	elif again == "no" or again == "No":
		exit()
	else:
		again_again = input("Please enter yes or no: ")
		if again == "yes" or again == "Yes":
			print("Good luck!")
		elif again == "no" or again == "No":
			exit()
			
# main program
def main():
	create_deck()
	random.shuffle(deck)
	intinalize_game()
	
	while len(players) > 0:
		player_bet_func()	
		deal()
		if 0 in players.values():
			break
		play_again()

# call main
main()










	
		




				
		


