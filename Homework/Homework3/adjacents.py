"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/26/2025
    Section : Homework 3
    E-mail : jmautsa1@umbc.edu
    Description : 
    """

word = input("Enter a string to check for k-adjacents: ")
num = int(input("What is the jump distance k? "))

count = 0
for i in range(len(word) - num):
    if word[i] == word[i + num]:
        count += 1

print(f"The number of {num}-adjacents is {count}")