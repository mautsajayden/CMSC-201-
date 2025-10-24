"""
File:         FILENAME.py
Author:       YOUR NAME
Date:         10/TODAY/2019
Section:      YOUR SECTION NUMBER
E-mail:       USERNAME@umbc.edu
Description:  YOUR DESCRIPTION GOES HERE AND HERE
              YOUR DESCRIPTION CONTINUED SOME MORE
"""


def sum_list(numbers):
    """
    Sums a list of integers
    :param numbers: a list of integers
    :return: the sum of the integers in numbers
    """
    sum = 0 
    for i in numbers :
        sum +=i
    
    return sum

def get_string_lengths(strings):
    """
    Given a list of strings, return a list of integers representing
    the lengths of the input strings
    :param strings: a list of strings
    :return: a list of integers representing the lengths of the input strings
    """
    numSum = []
    for i in range(len(strings)):
        numSum.append(len(strings[i]))

    return sum_list(numSum)

def get_names():
    """
    Asks the user for a list of names
    :return: a list of strings for the names the user entered
    """
    arrNames = []
    name = input("Enter a name, STOP to stop: ")
    while (name != "STOP") :
        arrNames.append(name)    
        name = input("Enter a name, STOP to stop: ")


    
    return get_string_lengths(arrNames)
    
        

if __name__ == '__main__':
    kitties = [
        "Jules",
        "Stubby",
        "Tybalt",
        "Scooter",
        "KC",
        "Garfield",
        "Bucky"
    ]

    # print the sum of the lengths of the strings in kitties
    print("There are ",get_string_lengths(kitties),"letters in the kitties")
    puppers = [
        "Charlie",
        "Chuck",
        "Chuckadero",
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]

    # prints the sum of the lengths of the strings in puppers
    print("There are ",get_string_lengths(puppers),"letters in the puppers")
    # gets names from the user and reports how many letters are in all the names
    print("There are ",get_names(),"letters in the names entyered by user")