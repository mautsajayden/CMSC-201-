import random

#def play_game(game_map):

"""_summary_
    A function to handle the math commands
A function to handle jump commands
A function to display the grid using the other two functions given.  
You can make other functions than these as well.  

    """

def mathComm(addx,sumx,mulx,score,x):
    addx = score + x 
    subx = score - x 
    mulx = score * x 
    
def jumpComm(jx,score,x):
    jmpx = score = x
    
def displayGrid():
    x = 0

def generate_random_map(length, the_seed):
    ranMap = []
    for i in range(length - 2):
    
    
def roll_dice():
    return random.randint(1,7)

def make_grid(table_size):
    
def fill_grid_square(display_grid, size, index, message):



def main():
    
    #1# user input 
    sizeSeed = input("Board Size and Seed")
    size = " "
    seed = " "
    n = 0
    
    #have tested this its good 
    for i in sizeSeed.split():
        n+=1
        if n == 1:
            size = i
        elif n == 2:
            seed = i 
    #2#There is only one player for this game, with an integer score
    score = 0
    
    #3#decide the numbers of moves 
    diMovement = random.randrange(1,7)
    
    #3# check length 
    if(score + diMovement > size):
        score = (score + diMovement) % size
    
    #4# 
    
    #you stay 
    nop = " "
    
    #
    x = 0
    
    hlt  = "quit" 
    nop = 
    if()
    
    
    
    
if __name__ == "__main__":
    main()