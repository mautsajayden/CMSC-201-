""" 
    File : Optimisim_print.py
    Author : Jayden Mautsa 
    Date : 9/11/2025
    Section : Lab
    E-mail : jmautsa1@umbc.edu
    Description : This is an example file for learning 
    """

sup = input("Are you a hero or villain? ").lower()

if(sup == "villain"):
    vil = input("What’s your name? ")
    print(f"{vil} sounds pretty evil! ")
    
elif(sup == "hero"):
    hero = int(input("How many people have you saved? "))
    
    if(hero <= 10):
        print("Go on more patrols! ")
    elif((hero > 10) and (hero < 100)) :
        print("Sounds like you’re making a difference! ")
    elif(hero >= 100):
        print("Wow, great job saving the city! ")
    