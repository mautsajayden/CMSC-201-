"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 10/03/2025
    Section : Homework 4
    E-mail : jmautsa1@umbc.edu
    Description : 
    """

redTeam = []
blueTeam = []

redChoice = ""
blueChoice = ""

while redChoice != "begin the game" and blueChoice != "begin the game":

    redChoice = input("Who should we add to the Red team? ")
    if redChoice == "begin the game":
        break
    redTeam.append(redChoice)

    blueChoice = input("Who should we add to the Blue team? ")
    if blueChoice == "begin the game":
        break
    blueTeam.append(blueChoice)


turn = "Red"
gameOn = "yes"

while gameOn == "yes":

    if len(redTeam) == 1:
        
        print("The Blue Team has won")
        
        break

    if len(blueTeam) == 1:
        
        print("The Red Team has won")
        
        break


    if turn == "Red":

        userChoice = input("Who should Red team send over? ")

        if userChoice == "display":
            
            print("The Red Team is composed of:")
            
            for p in redTeam:
                print(p+",", end=" ")
                
            print()
            continue

        if userChoice not in redTeam:
            
            print(userChoice+" is not on the Red team")
            
            continue

        line = input("Did they make it through the line? ")

        if line == "yes":
            
            print(userChoice+" stays on the Red team")
            
        else:
            redTeam.remove(userChoice)
            
            blueTeam.append(userChoice)
            
            print(userChoice+" changes to the Blue team")

        turn = "Blue"


    else:

        userChoice = input("Who should Blue team send over? ")

        if userChoice == "display":
            
            print("The Blue Team is composed of:")
            
            for p in blueTeam:
                print(p+",", end=" ")
                
            print()
            
            continue

        if userChoice not in blueTeam:
            
            print(userChoice+" is not on the Blue team")
            
            
            continue

        line = input("Did they make it through the line? ")

        if line == "yes": print(userChoice+" stays on the Blue team")
        
        else:
            
            blueTeam.remove(userChoice)
            redTeam.append(userChoice)
            
            print(userChoice+" changes to the Red team")

        turn = "Red"
