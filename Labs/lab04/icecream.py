""" 
    File : Optimisim_print.py
    Author : Jayden Mautsa 
    Date : 9/25/2025
    Section : Lab
    E-mail : jmautsa1@umbc.edu
    Description : This is an example file for learning 
    """

iceCreamFlavors = ["vanilla", "strawberry", "chocolate"]
iceCreamToppings = ["caramel", "marshmallow", "gummi bears"]

for i in range(len(iceCreamFlavors)):
    if iceCreamFlavors[i] == "strawberry":
        print("strawberry is fine on its own!")
    else:
        for j in iceCreamToppings:
            print(f"{iceCreamFlavors[i]} is tasty with {j}")



