"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/16/2025
    Section : Homework 2
    E-mail : jmautsa1@umbc.edu
    Description : This is about a game Lord of rings 
    """
    
#user input of what race they are 
race = input("Which race are you? (human/dwarf/elf/maiar/hobbit) ").strip().lower()

#boolean checks of race
isHuman = bool( race == "human")
isElf = bool(race == "elf") 
isMaiar = bool(race == "maiar")
isHobbit = bool(race == "hobbit")
isDwarf = bool(race == "dwarf")

#human 
if(isHuman):
    check = input("Are you the true and rightful King of Gondor? ").strip().lower()
    if(check == "yes"):
        print("You are Aragorn son of Arathorn")
    elif(check == "no"):
        check = input("Did you take the ring from Frodo? ").strip().lower()
        if(check == "yes"):
            print("You are Boromir")
        elif(check == "no"):
            print("You are Theoden, probably")

#elf  
elif(isElf):
    check = input("Are you in the matrix. ").strip().lower()
    if(check == "yes"):
        print("You are Elrond.")
    elif(check == "no"):
        print("You are Logolas.")

#Maiar     
elif(isMaiar):
    check = input("Are you good or evil ").strip().lower()
    if(check == "good"):
        print("You are Gandalf")
    elif(check == "evil"):
        check = input("Did you forge the One Ring ").strip().lower()
        if(check == "yes"):
            print("You are Sauron")
        elif(check == "no"):
            print("You are Saruman")

#hobbit      
elif(isHobbit):
    check = input("Do you carry the One Ring ").strip().lower()
    if(check == "yes"):
        print("You are Frodo Baggins")
    elif(check == "no"):
        check = input("Are you a gardener. ").strip().lower()
        if(check == "yes"):
            print("You are Samwise")
        elif(check == "no"):
            print("Then you are either Merry or Pippin.")

#dwarf         
elif(isDwarf):
    print("You are Gimli son of Gloin.")

#if dont have a race  
else:
    print("You are an Orc, sorry about that.")
    

        
    