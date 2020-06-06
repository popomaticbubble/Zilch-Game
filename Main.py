import random, Information, Setup
from Player import Player
from Score import Score
print("""
Welcome to Zilch! The extreme dice betting game.
Will you get all the points? Or will you lose all your
stinking denero?
""")

while True:
	first_time = input("Is this your first time playing the game? (y/n): ")
	if first_time == "y":
		Information.Instructions()
		break
	elif first_time =="n":
		break	
	else: print("Please enter \"y\" or \"n\"")

players = Setup.GameStart()

While True:
for i in players:
	while 
	players[i].roll()

