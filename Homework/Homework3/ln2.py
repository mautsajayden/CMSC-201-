"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/26/2025
    Section : Homework 3
    E-mail : jmautsa1@umbc.edu
    Description : 
    """

n = int(input("How many terms do you want to calculate? "))

total = 0

for i in range(1, n + 1):
    sign = (-1) ** (i + 1)   # alternates between +1 and -1
    total += sign * (1 / i)

print(f"The approximation of ln(2) for {n} terms is {total}")
