"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/26/2025
    Section : Homework 3
    E-mail : jmautsa1@umbc.edu
    Description : 
    """
height = int(input("What is the height of the rectangle? "))
width = int(input("What is the width of the rectangle? "))

for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()