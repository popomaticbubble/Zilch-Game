from Player import Player
def GameStart():
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
		name = input(f"What is the name of player {i}? ")
		print(f"Welcome to the game {name}! You are player {i}.")
		players[name] = players.get(name, Player(name=name, order=i))
	
	return players
