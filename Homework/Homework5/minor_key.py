"""
    File : minor_key.py
    Author : Jayden Mautsa 
    Date : 10/10/2025
    Section : Homework 5
    E-mail : jmautsa1@umbc.edu
    Description : find the keystrokes
    """
    

MUSICAL_NOTES = ['C', 'D\u266d', 'D', 'E\u266d', 'E', 'F', 'G\u266d', 'G', 'A\u266d', 'A', 'B\u266d', 'B']
musical_steps = [2, 1, 2, 2, 1, 3, 1]

def isCheck_Flat(userKey):
   
   #checks if flat in the user word 
    isCheckFlat = "flat" in userKey.lower()
    
    #checks if the word in musical remove flat and make a flat
    isFlat = userKey[0].upper() + "\u266d"
    
    return isFlat, isCheckFlat

def isIndex(userKey):
    
    isFlat, isCheckFlat = isCheck_Flat(userKey)
    
    numIndex = -1  
    
    #loop to find index so to make the movements for making the scale 
    for i in range(len(MUSICAL_NOTES)):
        
        if isCheckFlat:
            if isFlat == MUSICAL_NOTES[i]:
                numIndex = i
                break
        else:
            if userKey[0].upper() == MUSICAL_NOTES[i]:
                numIndex = i
                break

    return numIndex, isFlat 

def scaleMaker(numIndex):
    
    keyMusical = MUSICAL_NOTES[numIndex]
    
    for i in range(0, len(musical_steps)):
        
        numIndex += musical_steps[i]
        
        if numIndex >= 11:
            #formula to move around the arrray when i hit outbound it bounce back to 0 and done
            isOver12 = numIndex - 11
            numIndex = -1
            numIndex += isOver12
            
        #the scaled string of the key strokes     
        keyMusical += " " + MUSICAL_NOTES[numIndex]
        
    return keyMusical

def main():

    while True:
    
        userKey = input("Enter a starting note (C, D flat): ")
    
        if userKey.lower() == "quit":
            break

        numIndex, isFlat = isIndex(userKey)

        if numIndex == -1:
            print("There is no starting note", isFlat)
        else:
            keyMusical = scaleMaker(numIndex)
            print(keyMusical)

if __name__ == "__main__":
    main()