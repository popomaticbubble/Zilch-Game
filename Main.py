import tkinter as tk
import random
import sys
import setup
from player import Player
from information import Information
from score import Score


window = tk.Tk()
window.rowconfigure(5, minsize=50, weight=1)
window.columnconfigure(8, minsize=50, weight=1)
btn_keep_dice = tk.Button(master=window, text="Keep These Dice")

btn_keep_dice.grid(row=5, column=3, sticky="nsew")
window.mainloop()
"""
Information.intro_message()
setup.first_time()
setup.instruction_query()
while True:
	players = setup.player_setup()
	while True:	
		setup.game(players)
		if not setup.yes_or_no("Would you like to play again (y/n)?"): 
			print("\n\nThanks for playing!")
			sys.exit()
		elif setup.yes_or_no("Would you like new players?"):
			break
"""