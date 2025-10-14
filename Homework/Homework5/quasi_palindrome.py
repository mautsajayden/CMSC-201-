"""
    File : quasi palindrome
    Author : Jayden Mautsa 
    Date : 10/10/2025
    Section : Homework 5
    E-mail : jmautsa1@umbc.edu
    Description : the quasi palindromes game 
    """


def quasi_palindrome(word, errors):
    
    varWord = []
    reversedWord = ""
    wrongLetters = 0
    
    #puts the word into a list 
    for i in word:
        varWord.append(i)
    
    #reverse the word 
    for i in range(len(varWord)//2):
        varWord[i], varWord[len(varWord)-i-1] = varWord[len(varWord)-i-1], varWord[i]
    
    #concanates the reversed word from the list 
    for j in varWord:
        reversedWord += j
    
    #counts the number of erros 
    for i in range(len(word)):
        if word[i] != reversedWord[i]:
            wrongLetters += 1
    
    #un accounts for the double erros 
    wrongLetters //= 2
    
    #returns true or false 
    return wrongLetters <= errors

def main():
    userWord = " "
    numErrors = 0

    while (userWord != "quit"):
        #user input 
        userWord = input("What word do you want to check? ").lower()
        numErrors = int(input("How many errors do you want to allow? "))

        if quasi_palindrome(userWord, numErrors):
            print(f"It was a {numErrors}-quasi-palindrome!")
        else:
            print(f"It was not a {numErrors}-quasi-palindrome!")

if __name__ == "__main__":
    main()