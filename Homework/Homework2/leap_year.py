"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/16/2025
    Section : Homework 2
    E-mail : jmautsa1@umbc.edu
    Description : This is about a leap year 
    """

year = int(input("Enter a year: "))

isLeapYear_4 = bool( ((year % 4)==0))
isLeapYear_400 = bool( ((year % 400)==0))
isNotLeapYear = bool(((year % 100)==0))


if( isLeapYear_4 and (not(isNotLeapYear))) or (isLeapYear_400):
    print("It is a leap year.")
elif( isNotLeapYear or (not(isLeapYear_4)) ):
    print("It is not a leap year.")
    