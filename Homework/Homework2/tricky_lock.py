"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/16/2025
    Section : Homework 2
    E-mail : jmautsa1@umbc.edu
    Description : This is about a leap year 
    """
    
#user input 
fNum = int(input("What is the first number in the combination lock? "))
sNum = int(input("What is the first number in the combination lock? "))

#gets the switch user input
fSwitch = str(input("What is the position of the first switch (up/down)? ")).strip().lower()
sSwitch = str(input("What is the position of the second switch (up/down)? ")).strip().lower()
thrdSwitch = str(input("What is the position of the third switch (up/down)? ")).strip().lower()

#checks if the numbers are between 1 and 25 
isCheckNum = bool((fNum >= 1 and fNum <= 25) and (sNum >=1 and sNum <= 25))

#checks if the sum is 36
is36 = bool((fNum + sNum) == 36)

#checks if there is 2 consective ups from the user and 1 down
isUp2Down1 = bool( 
                    ((fSwitch == "up" and sSwitch == "up") and thrdSwitch == "down") or
                    ((fSwitch == "up" and sSwitch == "down") and thrdSwitch == "up") or
                    ((fSwitch == "down" and sSwitch == "up") and thrdSwitch == "up") 
                       )


if(is36 and isUp2Down1):
    print("The lock opens, you gain access to the treasure.")
elif( (is36 and (not(isUp2Down1))) or ((not(is36)) and isUp2Down1) ):
    print("The lock clanks but does not open.")
elif((not(is36)) and (not(isUp2Down1))):
    print(" The lock does not even budge, try again.")