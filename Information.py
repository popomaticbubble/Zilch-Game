"""
This just contains various bundles of information for the players, including
rules, scoring, and introduction to the game. This is basically text.
"""

class Information:

	@staticmethod
	def instructions():
		print("""
			This is a dice game where you get to bet your 
			points to maximize your score, but if you get too
			greedy, you might lose it all!

			The game has two main phases. In the first phase, your goal
			is to get 750 or more points in a single round. If you get less
			you can't save any of the points from the round. Once you reach
			750 points, you enter the next phase.

			In the second phase you can stop at any point total about 0. 

			Every round begins with six dice. After rolling, you get to choose
			which dice you want to keep, then roll the remaining dice. You can only
			save dice if they score you points. If in any roll, you fail to score any
			points, you get "zilched" this means you lose all the points for that round
			(but NOT for the whole game.) and the next player's turn begins. You get three
			rolls in each turn maximum, but you don't have to roll three times.

			Here's where it's get interesting. If every single dice scores you points, then you get
			a bonus round. But don't forget, you might get zilched. So do your aim for the stars, for
			the big money, or do you play it safe. That, my friend, is up to you.""")

	@staticmethod	
	def intro_message():
		print("""
	Welcome to Zilch! The extreme dice betting game.
	Will you get all the points? Or will you lose all your
	stinking denero?
	""")

	@staticmethod
	def make_scoring_file():
		"""
		This makes a txt file that players can look at to play the game.
		"""
		scoring = open("Scorechart.txt", "w+")
		scoring.write("Scoring Chart\n")
		scoring.write("\n")
		scoring.write("A straight of six dice:\t1000 points\n\n")
		scoring.write("Three Pairs:\t750	points\n\n")
		scoring.write("Ones: \n")
		scoring.write(" 1x\t100 points\n")
		scoring.write(" 2x\t200 points\n")
		scoring.write(" 3x\t1000 points\n")
		scoring.write(" 4x\t2000 points\n")
		scoring.write(" 5x\t3000 points\n")
		scoring.write(" 6x\t4000 points\n\n")
		scoring.write("Fives:\n")
		scoring.write(" 1x\t50 points\n")
		scoring.write(" 2x\t100 points\n")
		scoring.write(" 3x\t500 points\n")
		scoring.write(" 4x\t1000 points\n")
		scoring.write(" 5x\t1500 points\n")
		scoring.write(" 6x\t2000 points\n\n")
		scoring.write("Other dice values:\n")
		scoring.write(" 1-2x dice values \t0 points\n")
		scoring.write(" 3x \tdice value x 100 points\n")
		scoring.write(" 4x \tdice value x 200 points\n")
		scoring.write(" 5x \tdice value x 300 points\n")
		scoring.write(" 6x \tdice value x 400 points\n\n\n")
		scoring.write("You get three rolls for each round.\n")
		scoring.write("Remember that you need to score 750 points in one round\n")
		scoring.write("to unlock open scoring. That mean you can stop rolling\n")	
		scoring.write("as soon as you've scored any points for the round.\n ")
		scoring.write("Once you unlock open scoring, it is active for the rest of the game.\n")
		scoring.write("Just remember, if in any of your rolls, you score no points,\n")
		scoring.write("you get ZILCHED! and lose all of your points for the round.\n")
		scoring.write("If you manage to score all of your dice, you get a bonus round\n")
		scoring.write("with three rolls of all six dice again. Zilch rules still apply.\n")
		scoring.write("So if you get zilched in the bonus rounds, you still lose all the points\n")
		scoring.write("for the whole round. Good luck.\n")
		scoring.close()
