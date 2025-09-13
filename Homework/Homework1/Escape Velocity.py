""" 
    File : Favorite Things
    Author : Jayden Mautsa 
    Date : 9/12/2025
    Section : Homework 
    E-mail : jmautsa1@umbc.edu
    Description : This is about velocity
    """

G = (6.67 * (10**-11))

# Ask user inputs
body = input("What body are we launching from? ")

massCoeff = float(input("Enter the mass of the planet in scientific notation with the floating number first: "))
massExp = int(input("What power of 10 is this? "))

mass = massCoeff * (10 ** massExp)

radiusCoeff = float(input(f"Enter the coefficient of the scientific notation of the radius from the center of {body}: "))
radiusExp = int(input("What power of 10 is this? "))
radius = radiusCoeff * (10 ** radiusExp)


velocity = ((2 * G * mass) / radius) ** 0.5

velocity = round(velocity, 3)

print(f"The escape velocity required for {body} is {velocity} m/s")

