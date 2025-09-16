"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/16/2025
    Section : Homework 2
    E-mail : jmautsa1@umbc.edu
    Description : This is about a game of power
    """

#first creature 
nCreature = str(input("What is the name of the first creature? "))
pCreature = int(input("What is the power of the first creature? "))
tCreature = int(input("What is the toughness of the first creature? "))

#second creature
n2Creature = str(input("What is the name of the second creature? "))
p2Creature = int(input("What is the power of the second creature? "))
t2Creature = int(input("What is the toughness of the second creature? "))

#the fight between the 2 creatures 
tot  = tCreature- p2Creature 
tot2 = t2Creature- pCreature

#the display for the creatures 
print(
    f"The first creature now has ({pCreature}, {tot2})"
    f"The second creature now has ({p2Creature}, {tot2})"
)

#boolean for check if toughness is still 1 
isCheck = bool(((tot >=1) and (tot2>=1)))

#will dispay depending on result
if((tot < tot2) and (isCheck)):
    print(f"{nCreature} has died, {n2Creature} wins")
    
elif((tot > tot2) and (isCheck)):
    print(f"{n2Creature} has died, {nCreature} wins")
    
elif(tot >=1 and tot2>=1):
    print("Both creatures live to fight another day.")
    
elif not(isCheck) :
    print("Both creatures die in mutual combat.")