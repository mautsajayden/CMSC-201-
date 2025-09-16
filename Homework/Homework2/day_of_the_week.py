"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/16/2025
    Section : Homework 2
    E-mail : jmautsa1@umbc.edu
    Description : This is about a the calender date 
    """

#user input for the sate 
day = int(input("What day of September 2023 is it? "))

#check if the user enter a coirrect day number 
if(not(day >= 1 and day <=30)): 
    print(f"That day {day} is out of range, you must enter a number between 1 and 30")
else:
    #formula to predict 
    predictDate = (day - 1 + 5) % 7

    if(predictDate == 0):
        date = "Sunday"
        
    elif predictDate == 1:
        date = "Monday"
        
    elif predictDate == 2:
        date = "Tuesday"
        
    elif predictDate == 3:
        date = "Wednesday"
        
    elif predictDate == 4:
        date = "Thursday"
        
    elif predictDate == 5:
         date = "Friday"
         
    elif predictDate == 6:
         date = "Sartuday" 

    print(f"September {day} is a {date} ")