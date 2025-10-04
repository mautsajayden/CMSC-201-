"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 10/03/2025
    Section : Homework 4
    E-mail : jmautsa1@umbc.edu
    Description : the burger shop

    """

burger = "bottom bun"
n = 0
arrayBurg = []
arrayCondiments = []

while (burger != "top bun"):
    
    burger = input("What do you want to add? ").lower()
    
    arrayBurg.append(burger)

    if (burger == "burger") or (burger == "cheese"): n += 1

    if (burger not in ["top bun", "bottom bun", "burger", "cheese"]): arrayCondiments.append(burger)

    if "cheese" in arrayBurg : bur = "cheeseBurger"
    
    else : bur = "hamburger"

uCondiments = []

for i in arrayCondiments:
    
    if i not in uCondiments: uCondiments.append(i)

if uCondiments: condiments = ", ".join(uCondiments)
    
else: condiments = "No Condiments"

print(f"You have created a {n}-{bur} with the condiments: {condiments}")
