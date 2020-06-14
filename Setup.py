import os
from information import Information
from player import Player
"""
These are the utility methods to get the game setup and other utilities for
running the game.
"""

def player_setup():
	"""
	This asks how many players there are and their names, then sets up
	a Player in the Player class for use in the game.
	"""
	while True:
		number_of_players = input("\n How many players do you have? ")
		if number_of_players.isdigit() and number_of_players != 0:
			number_of_players = int(number_of_players)
			break
		print("Please enter whole a number greater than 0.")
	if number_of_players >= 6:
		print("It's going to be a long game!")
	players = {}
	for i in range(1, number_of_players+1):
		name = input(f"\nWhat is the name of player {i}? ")
		print(f"\nWelcome to the game {name}! You are player {i}.\n")
		players[name] = players.get(name, Player(name=name, order=i))
	return players

def first_time():
	"""
	This asks players if they've played the game before. If they say yes
	it prints a short description of the game's rules.
	"""
	while True:
		first_time = input("Is this your first time playing the game? (y/n): ")
		if first_time == "y":
			Information.instructions()
			Information.make_scoring_file()
			break
		elif first_time =="n":
			break	
		else: print("Please enter 'y' or 'n'")

def yes_or_no(msg):
	"""
	Player gets to chooose yes or no. 
	****Make sure that your bools match!***
	"""
	while True:
		x = input(msg)
		if x == "n":
			return False
		elif x == "y":
			return True
		else: 
			print("Please enter 'y' or 'n'")

def game(players):
	"""
	This is the general function for the game.
	players argument is a dictionary with key=the order they'll be playing
	and value= the instatiated players from the Player class.
	"""
	while True:
		for i in players:
			print("*********************************************")
			print(f"\nOK, {players[i].name}, it's you're turn.\n")
			players[i].turn()
			if players[i].points > 10000:
				print(f"\nCongratulations {players[i].name}! You won!")

def instruction_query():
	"""
	Offers to open a file on their computer with rules and scoring.
	"""
	print("\nWould you like a score chart/list of rules")
	print("to look at while you play (y/n)?")
	if yes_or_no("Note: this will open a file on your computer. > "):
		try:
			os.startfile("Scorechart.txt")
		except FileNotFoundError:
			Information.make_scoring_file()
			os.startfile("Scorechart.txt")

def dice_displayer(dice_roll):
	"""
	This takes the dice from a dice roll list and returns their 
	values so a player can easily pick the dice they want.
	"""	
	for i in range(len(dice_roll)):
		print(f"Dice {i+1}: {dice_roll[i]}")			