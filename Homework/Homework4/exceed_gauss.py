"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 10/03/2025
    Section : Homework 4
    E-mail : jmautsa1@umbc.edu
    Description : the exceed the gauss sum 
    """

num = int(input("What number do you want to test? "))

numT =0
numI =-1

for i in range(num):
    
    if(numT > num ): break

    numT += i    
    numI +=1
    
print(f"After {numI} iterations, the gauss sum is {numT} which exceeds (or is equal to) the number {num}")