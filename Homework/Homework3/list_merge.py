"""
    File : MadPyLib
    Author : Jayden Mautsa 
    Date : 9/26/2025
    Section : Homework 3
    E-mail : jmautsa1@umbc.edu
    Description : 
    """

numElem = int(input("How  many elements do you want in each list? "))

list1 = []
list2 = []

for i in range(numElem):

    item = input("What do you want to put in the first list? ")

    list1.append(item)

for i in range(numElem):

    item = input("What do you want to put in the second list? ")

    list2.append(item)

merged = []

for i in range(numElem):

    merged.append(list1[i])
    merged.append(list2[i])


print(
"The first list is: ", list1,
"\nThe second list is: ", list2,
"\nThe merged list is: ", merged
 )