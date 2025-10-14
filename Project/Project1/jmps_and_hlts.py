

#def play_game(game_map):

#generate_random_map(length, the_seed):
    
#roll_dice()

##make_grid(table_size):
    
#fill_grid_square(display_grid, size, index, message):



def main():
    sizeSeed = input("Board Size and Seed")
    size = " "
    seed = " "
    n = 0
    for i in sizeSeed.split():
        n+=1
        if n == 1:
            size = i
        elif n == 2:
            seed = i 
            
    print(size, " Size ", seed, "seed")
    
    
if __name__ == "__main__":
    main()