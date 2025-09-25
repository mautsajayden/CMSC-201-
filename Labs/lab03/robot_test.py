""" 
    File : Optimisim_print.py
    Author : Jayden Mautsa 
    Date : 9/18/2025
    Section : Lab 3
    E-mail : jmautsa1@umbc.edu
    Description : This is an example file for learning 
    """
    
rQuestion = input("Be you robot, or human? ").lower()

isHuman = (rQuestion == "human")
isRobot = (rQuestion == "robot")

if(isHuman):
    print("Humans must be destroyed!")
    
elif(isRobot):
    typeTest = input(
        "Administer the test!"
        "\nWhich of the following would you prefer?"
             "\n\tA cute (puppy)"
             "\n\tA (flower) from your sweetie"
             "\n\tA large properly formatted (data file)."
             "\nChoose! "
    ).lower()
    
    #check for input type 
    isPuppy = bool(typeTest == "puppy")
    isFlower = bool(typeTest == "flower")
    isDF = bool(typeTest == "data file")
    
    #display detection on whether is human or robot
    if(isPuppy) : print("Get the intruder! Get the humanoid!")
    
    elif(isFlower) : print("That is acceptable, pass on mechanical friend.")
    
    elif(isDF) : print("Very good, you are a robot of some esteem.")
    
    

