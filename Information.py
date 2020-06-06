def Instructions():
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