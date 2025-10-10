"""
    File : quasi palindrome
    Author : Jayden Mautsa 
    Date : 10/10/2025
    Section : Homework 5
    E-mail : jmautsa1@umbc.edu
    Description : the quasi palindromes game 
    """


def quasi_palindrome(word, errors):
    
    arr = []
    reversedWord = ""
    misMatcheLetters = 0
    
    for i in word:
        arr.append(i)
    
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    
    for j in arr:
        reversedWord += j
    
    for i in range(len(word)):
        if word[i] != reversedWord[i]:
            misMatcheLetters += 1
    
    misMatcheLetters //= 2
    
    return misMatcheLetters <= errors


userWord = input("What word do you want to check? ")
numErrors = int(input("How many errors do you want to allow? "))

if quasi_palindrome(userWord, numErrors):
    print(f"It was a {numErrors}-quasi-palindrome!")
else:
    print(f"It was not a {numErrors}-quasi-palindrome!")
