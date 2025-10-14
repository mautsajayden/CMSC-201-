"""
    File : checkerboard.py
    Author : Jayden Mautsa 
    Date : 10/10/2025
    Section : Homework 5
    E-mail : jmautsa1@umbc.edu
    Description : the checkerBoard
    """

def checkerboard(size, symbol_1, symbol_2):
    var1_2 = symbol_1 + symbol_2
    
    #makes the original of the symbol "ababa"
    for i in range((size-(len(var1_2)))):
        if not(i == (size-(len(var1_2)))):
            var1_2 += var1_2[i]
        else : 
            break
    
    var2_1 = symbol_2 + symbol_1
    
    #makes the reverse of the symbols  'babab'
    for i in range((size-(len(var2_1)))):
        if not(i == (size-(len(var2_1)))):
            var2_1 += var2_1[i]
        else : 
            break
        
    #print the reverse and correct word of the symbols 
    for i in range(size):
        if i % 2 == 0:
            print(var1_2[:size])
        else:
            print(var2_1[:size])

def main():
    
    numSize =int(input("What size do you want? "))
    varSymbols = input("What symbols do you want? ")
    
    symbol1 = varSymbols[0]
    symbol2 = varSymbols[2]

    checkerboard( numSize, symbol1 , symbol2)
 

if __name__ == "__main__":
    main()
    
