"""
This is for all the scoring mechanisms. It returns the total points 
for every roll fed into it. It also returns if a bonus round is triggered
when every die get scored.
"""

class Score():
	def __init__(self, dice):
		self.dice = dice
		self.roll_points = 0
		self.zilched = False

	def straight_checker(self):
		if all(self.dice.values()) == 1:
			self.roll_points += 1000
			self.dice = {}
			return self.roll_points, self.dice
		pass

	def one_checker(self):
		"""For every 1, you get 100 points,
			Three 1's, you get 1000 points,
			for every 1 after that, there is an
			increasing bonus multiplier.
			This adds the points and deletes 
			all 1 from the dice list"""
		ones = self.dice.get(1)
		if ones:
			if ones <= 2:
				self.roll_points += ones*100
				self.dice.pop(1)
				return self.roll_points, self.dice
			self.roll_points += 1000
			if ones == 4: 
				self.roll_points *= 2
			elif ones == 5: 
				self.roll_points *= 3
			elif ones == 6: 
				self.roll_points *= 4
			self.dice.pop(1)
			return self.roll_points, self.dice
		pass

	def five_checker(self):
		"""For every 5, you get 50 points,
			Three 5's, you get 50 points,
			for every 5 after that, there is an
			increasing bonus multiplier.
			This adds the points and deletes 
			all 5 from the dice list"""

		fives = self.dice.get(5)
		if fives:
			if fives <= 2:
				self.roll_points += fives*50
				self.dice.pop(5)
				return self.roll_points, self.dice
			self.roll_points += 500
			if fives == 4: 
				self.roll_points *= 2
			elif fives == 5: 
				self.roll_points *= 3
			elif fives == 6: 
				self.roll_points *= 4
			self.dice.pop(5)
			return self.roll_points, self.dice
		pass

	def three_pair(self):
		counter = 0
		for i in self.dice:
			if self.dice.get(i) == 2: 
				counter += 1
		if counter == 3:
			self.roll_points += 750
			self.dice = {}
			return self.roll_points, self.dice
		pass

	def multiples(self):
		"""For every three of a kind, you get the value
		of the die*100. Then for every additional matching die,
		you get an increasing mulitplier that starts at 2."""
		self.dice
		function_points = 0
		for i in self.dice.keys():
			function_points += (i * 100)
			if self.dice.get(i) == 4: 
				function_points *= 2
			elif self.dice.get(1) == 5: 
				function_points *= 3
			elif self.dice.get(i) == 6: 
				function_points *= 4
		self.dice = {}
		self.roll_points += function_points
		return self.roll_points, self.dice

	def zilch(self):
		"""If players roll no points, they lose their points for the whole
		round and lose the turn."""
		print("\nZILCH! You've lost all your points. Round over. :(")
		self.zilched = True

	def master_scorer(self):	
		while self.dice:
			Score.straight_checker(self) 
			Score.three_pair(self) 
			Score.one_checker(self)
			Score.five_checker(self)
			"""Our scorer will stop when dice is empty.
			We've scored everything that has less than
			a pair. So we can just clean out anything less
			than three of kind. If all dice are used, it triggers
			a bonus round. So if this finds any unscorable dice,
			it'll shut off the bonus round. It deletes, the empty
			dice first."""
			for i in self.dice.copy():
				if self.dice.get(i) < 3:
					self.dice.pop(i)
			Score.multiples(self)
			if self.roll_points == 0: #check if there is a zilch
				self.zilch()
				break
		return self.roll_points


"""
dice1 = {1:0, 2:0, 3:0, "4":3, "5":1, 6:0}
testroll1 = Score(dice1)
print(testroll1.MasterScorer())



dice2 = {1:5, 2:0, 3:0, 4:0, 5:0, 6:0}
dice3 = {1:1, 2:0, 3:0, 4:0, 5:0, 6:0}
dice4 = {1:0, 2:0, 3:0, 4:0, 5:3, 6:0}
dice5 = {1:0, 2:0, 3:3, 4:0, 5:0, 6:0}
dice6 = {1:0, 2:4, 3:0, 4:0, 5:0, 6:0}

testroll2 = Score(dice2, roll_points)
print(testroll2.MasterScorer())

testroll3 = Score(dice3, roll_points)
print(testroll3.MasterScorer())

testroll4 = Score(dice4, roll_points)
print(testroll4.MasterScorer())

testroll5 = Score(dice5, roll_points)
print(testroll5.MasterScorer())

testroll6 = Score(dice6, roll_points)
print(testroll6.MasterScorer())

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(testroll1.MasterScorer(), 1000)
        self.assertEqual(testroll2.MasterScorer(), 4000)
        self.assertEqual(testroll3.MasterScorer(), 2000)
        self.assertEqual(testroll4.MasterScorer(), 100)
        self.assertEqual(testroll5.MasterScorer(), 750)
        self.assertEqual(testroll6.MasterScorer(), 1100)

if __name__ == '__main__': 
	unittest.main()
"""