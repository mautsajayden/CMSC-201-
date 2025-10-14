"""
    File : pascal.py
    Author : Jayden Mautsa 
    Date : 10/10/2025
    Section : Homework 5
    E-mail : jmautsa1@umbc.edu
    Description : the pascal
    """

numValues = input("What values do you want to run next_level on? ")

ogValues = []

for i in numValues.split() :
    ogValues.append(int(i))

newNextLevelValues = [1]

#addition of the next up values 
for i in range(len(ogValues)-1) :
    newNextLevelValues.append(ogValues[i]+ogValues[i+1])

#value for the end of the array
newNextLevelValues.append(1)

print("What values do you want to run next_level on?  ",newNextLevelValues)


