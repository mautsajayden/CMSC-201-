"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/26/2025
    Section : Homework 3
    E-mail : jmautsa1@umbc.edu
    Description : 
    """


day = int(input("What day of September 2025 is it? "))


if not (1 <= day <= 30):
    print(f"That day {day} is out of range, you must enter a number between 1 and 30")
else:
    
    predictDate = (day - 1 + 1) % 7  

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    print(f"The {day} of September is a {weekdays[predictDate]}")
