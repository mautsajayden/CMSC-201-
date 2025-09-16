""" 
    File : Optimisim_print.py
    Author : Jayden Mautsa 
    Date : 9/11/2025
    Section : Lab
    E-mail : jmautsa1@umbc.edu
    Description : This is an example file for learning 
    """
    
maj = input("What is your major: ")

maj = maj.upper()

if (maj == "CMSC") | (maj == "CMPE") :
    print("You need to earn at least a B for CMSC 201 to count.")
else:
    print("You need to earn at least a C for CMSC 201 to count.")
    