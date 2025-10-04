"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 10/03/2025
    Section : Homework 4
    E-mail : jmautsa1@umbc.edu
    Description : the rock paper scissiors game 
    """
import sys
from random import choice, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

userChoice = ""

while userChoice != "stop":
    
    userChoice = input("Enter rock, paper, or scissors to play, stop to end.  ").lower()
    
    if userChoice == "stop": break
    
    if userChoice not in ["rock", "paper", "scissors"]:
        
        print("You need to select rock, paper or scissors.")
        continue

    pcChoice = choice(["rock", "paper", "scissors"])
    

    if userChoice == pcChoice:print(f"Both {userChoice}, there is a tie.")
    
    elif userChoice == "rock" and pcChoice == "scissors": print("Rock crushes scissors, you win.")
    
    elif userChoice == "rock" and pcChoice == "paper": print("Paper covers rock, you lose.")
    
    elif userChoice == "paper" and pcChoice == "rock": print("Paper covers rock, you win.")
    
    elif userChoice == "paper" and pcChoice == "scissors": print("Scissors cut paper, you lose.")
    
    elif userChoice == "scissors" and pcChoice == "paper": print("Scissors cut paper, you win.")
    
    elif userChoice == "scissors" and pcChoice == "rock": print("Rock crushes scissors, you lose.")
