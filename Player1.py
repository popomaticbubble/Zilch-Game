import random
from Score import Score

class Player:
	
	def __init__(self, name, order):
		self.name = name	
		self.order = order
		"""There are two type of turns, open and closed
			You start closed, once you score 1000 in a turn
			You become open, meaning you can score less 
			that 1000 points"""
		self.open_turn = False
		self.remaining_dice = 6
		self.points = 0
		self.roll_number = 0
		self.dice_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
		self.round_points = 0

		
	def change_turn_style(self, style):
		"""There are two types of turns in the game:
		open and closed. It stars closed. After scoring 
		750 in one round, it becomes open."""
		self.open_turn = True
		return self.open_turn

	def roll(self):	
		remaining_dice = self.remaining_dice
		"""Generates a random number from 1 - 6 based on the
		number of dice left and puts them in a sorted list."""
		dice_roll = sorted([random.randint(1,6)
		for i in range(1, remaining_dice+1)])
		self.roll_number +=1
		print(self.roll_number)
		return dice_roll, self.roll_number

	@staticmethod
	def DiceDisplayer(dice_roll):
		for i in range(len(dice_roll)):
			print(f"Dice {i+1}: {dice_roll[i]}")

	def update_dice_count(self, kept_dice):
		self.remaining_dice = self.remaining_dice - len(kept_dice)

	def hold(self, dice_roll):
		while True:	#start loop for AreYouSure function
			while True: #setting up for invalid inputs
				Player.DiceDisplayer(dice_roll)
				try:
					kept_dice = input("""
Which dice would you like to keep? 
Enter the dice number (not the value),
separated by commas. 
Press enter to keep everything.
> """).split(',')
				except IndexError:
					print("That is not an available die.")
				else:
					break
			if kept_dice == ['']: #keeps all the dice if nothing is entered above
				kept_dice = [i for i in range(len(dice_roll))]
			"""Using the kept_dice to create a list
			of all the dice values that are saved without overwriting
			the original roll, in case they change their mind."""
			kept_dice = list(map(int, kept_dice))
			dice_bank = [dice_roll[i-1] for i in kept_dice]
			print(f"You've chosen {sorted(dice_bank)}")
			msg = "Is this correct (y/n)? "
			if self.AreYouSure(msg) == True:
				break
		dice_roll = list(map(int, dice_bank)) #overwrites oringal roll with save dice
		self.update_dice_count(kept_dice)
		self.DiceCounter(dice_roll)
		return self.dice_dict

	def KeepPoints(self):
		"""Saves the points from the round to the player and
		clears the round points."""
		self.points += self.round_points
		self.round_points = 0
		return self.points, self.round_points

	def DiceCounter(self, dice_roll):
		"""Converts a list of dice into a dictionary that
		counts all the dice vales, which can be read
		by our scorer"""
		self.ResetDice()
		for i in dice_roll:
			if i in self.dice_dict:
				self.dice_dict[i] +=1
		return self.dice_dict

	def AreYouSure(self, msg):
		"""Player gets to chooose yes or no."""
		while True:
			roll_again = input(msg)
			if roll_again == "n":
				return False
			elif roll_again == "y":
				return True
			else: 
				print("Please enter y or n ")

	def ResetDice(self):
		self.dice_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
		return self.dice_dict

	def Turn(self):
		"""The general sequence for a player's turn. The
		turn end when the player either: chooses to stop rolling,
		has a roll with no points, or reaches three rolls without
		a bonus. The points from the round are added to the player."""
		while self.roll_number <=3:
			dice_roll, self.roll_number = self.roll()
			"""We need to check if the intial roll is zilched.
			if so, there is no point asking if they want to
			save any dice, because their turn is over."""
			dice = self.DiceCounter(dice_roll)
			score = Score(dice)
			score.MasterScorer()
			if score.zilched == True:
				self.round_points = 0
				break
			dice = self.hold(dice_roll)
			score = Score(dice)
			score.MasterScorer()
			print(f"You scored {score.roll_points}! Great job!")
			self.round_points += score.roll_points
			print(score.bonus_round)
			self.ResetDice()
			msg = "Would you like to roll again (y/n)? "
			#if score.bonus_round == True:
				#self.roll_number = 0
			if self.remaining_dice == 0:
				self.roll_number = 0
			elif self.AreYouSure(msg) == False:
				break
		self.KeepPoints()





player1 = Player("player1", 1)
dice_roll = player1.Turn()

"""

player1.hold(r1_t1)
r1_r2 = player1.roll2()
player1.hold(r1_r2)
r1_r3 = player1.roll3()
"""