"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 10/03/2025
    Section : Homework 4
    E-mail : jmautsa1@umbc.edu
    Description : a rock paper scissor game
    """


primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

num = int(input("Enter a number to factor: "))

factors = []

for i in primes:
    
    while(num % i == 0):
        
        factors.append(i)
        
        num = num // i

if(len(factors) == 0): print("We didn't find any factors")

else:
    
    numF = ""
    
    for i in range(len(factors)):
        
        if(i == len(factors)-1): numF = numF + str(factors[i])
        
        else: numF = numF + str(factors[i]) + "*"
        
    print("The factors are: " + numF)

if(num != 1):
    print("This part of the number couldn't be factored with primes less than 50: ", num)
