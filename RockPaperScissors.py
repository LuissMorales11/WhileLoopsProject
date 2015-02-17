# RockPaperScissors.py

# By Luis Morales

# Import statements
import random
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog as simpledialog

# Create a Window
root = Tk()
w = Label(root, text= "Rock Paper Siccors ")
w.pack()

# Welcome the User
messagebox.showinfo("Information", "Hello, Let's play a game! :)")
messagebox.showinfo("Information", "We will play Rock Paper Scissors")
messagebox.showinfo("Information", "May the odds be ever in your favor")
# Constant: a variable that doesn't change its value
# A list of card SUITS
SUITS = ["Rock",
         "Paper",
         "Scissors"]

# Pick a random index position
pick = random.randrange( len(SUITS) )

# Use pick to select the suit
suit = SUITS[pick]

input("\nPress enter to see a list of your options.")

count = 1 # initialize count to 1 (to use for the loop)
# Loop through SUITS
for suit in SUITS:
    print(" " + str(count) + " -> " + suit)
    count += 1

userPick = input("\nSelect the item you want "
                 "by entering a number (1-3): ")
userPick = int(userPick) - 1
# NOTE: we had to subtract 1 for 0-based indexing
userSuit = SUITS[userPick]
print( "You picked {} for your option.".format(userSuit) )
                
