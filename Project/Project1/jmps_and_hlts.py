"""
    Come up with a name for the game

    JMPs and HLTs
"""

import random

GRID_WIDTH = 8
GRID_HEIGHT = 3
DICE_SIDES = 6


def generate_random_map(length, the_seed=0):
    """
        :param length - the length of the map
        :param the_seed - the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    """
    if the_seed:
        random.seed(the_seed)
    map_list = []
    for _ in range(length - 2):
        random_points = random.randint(1, 100)
        random_position = random.randint(0, length - 1)
        map_list.append(random.choices(['nop', f'add {random_points}', f'sub {random_points}', f'mul {random_points}', f'jmp {random_position}', 'hlt'], weights=[5, 2, 2, 2, 3, 1], k=1)[0])

    return ['nop'] + map_list + ['hlt']


def make_grid(table_size):
    """
    :param table_size: this needs to be the length of the map
    :return: returns a display grid that you can then modify with fill_grid_square (it's a 2d-grid of characters)
    """
    floating_square_root = table_size ** (1 / 2)

    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_height = int_square_root
    if int_square_root * (int_square_root - 1) >= table_size:
        table_height -= 1

    the_display_grid = [[' ' if j % GRID_WIDTH else '*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        if i % GRID_HEIGHT else ['*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        for i in range(table_height * GRID_HEIGHT + 1)]
    return the_display_grid


def fill_grid_square(display_grid, size, index, message):
    """
    :param display_grid:  the grid that was made from make_grid
    :param size:  this needs to be the length of the total map, otherwise you may not be able to place things correctly.
    :param index: the index of the position where you want to display the message
    :param message: the message to display in the square at position index, separated by line returns.
    """
    floating_square_root = size ** (1 / 2)
    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_row = index // int_square_root
    table_col = index % int_square_root

    if table_row % 2 == 0:
        column_start = GRID_WIDTH * table_col
    else:
        column_start = GRID_WIDTH * (int_square_root - table_col - 1)

    for r, message_line in enumerate(message.split('\n')):
        for k, c in enumerate(message_line):
            display_grid[GRID_HEIGHT * table_row + 1 + r][column_start + 1 + k] = c


def roll_dice():
    """
        Call this function once per turn.

        :return: returns the dice roll
    """
    return random.randint(1, DICE_SIDES)


#my code starts here 

"""
File: game_logic.py
Author: Jayden Mautsa
Date: October 24, 2025
Email: jmautsa1@umbc.edu
Description: This program runs a dice-based instruction game.
"""

def ask_user():
    """
    Asks the user for the board size and seed.
    return:  seed, size
    """
    size_seed = input("Board Size and Seed: ")

    parts = size_seed.split()

    size = int(parts[0])
 
    seed = int(parts[1])

    return seed, size

def value(instr_word):
    """
    get the integer value from a string like.
    :param instr_word: str, containing a number
    :return: int, the extracted number
    """
    word = instr_word.split()

    num = int(word[1])

    return  num

def jump_instruction(position, message, map_size):
    """
    Handles the JMP command.
    :param position: int, current position
    :param message: str, the "jmp X" instruction
    :param map_size: int, total size of the board
    :return: int, new position after jump
    """
    position = value(message)  

    if position < map_size:
        return position
    else:
        # if jump target is larger than map jump back
        return (position + roll_dice()) % map_size

def instructions(message, position, score, roll, map_size):
    """
    Executes the command at the current position and returns updated state.
    :param message: str, current instruction
    :param position: int, current position
    :param score: int, current score
    :param map_size: int, board size
    :return: (position, score, finished)
    """

    roll = roll_dice() 

    if((position + roll)>map_size):position = (position + roll) % map_size
    else : position +=roll

    if "add" in message:
        score += value(message)

    elif "sub" in message:
        score -= value(message)

    elif "mul" in message:
        score *= value(message)

    elif "jmp" in message:
        position = jump_instruction(position, message, map_size)
        return position, score, roll, False

    elif "hlt" in message:
        print(f"Final Pos: {position} Final Score: {score}, Instruction {message}")
        return position, score, roll, True

    return position, score, roll, False



def display_grid(the_grid):
    """
    Displays the 2D game grid.
    :par
     Display grid
     """

    for row in the_grid:
        print(''.join(row))


def play_game(game_map):
    """
    Main game loop. Runs until the game ends via 'hlt'.
    :param game_map: list of str, instructions
    """
    seed_num, map_size = ask_user()

    game_map = generate_random_map(map_size, seed_num)

    # makes the grid 
    the_grid = make_grid(map_size)

    for index in range(map_size):
        fill_grid_square(the_grid, map_size, index, game_map[index])

    display_grid(the_grid)

    position = 0
    score = 0
    roll = 0
    finished = False

    while not finished:
        command = game_map[position]

        position, score, roll, finished = instructions(command, position, score, roll, map_size)
        print("Pos:", position, "Score:", score, ", Instruction:", command, "Rolled:", roll)

    if not finished:
        print(f"Final Pos: {position} Final Score: {score}, Instruction {game_map[position]}")


if __name__ == "__main__":
    
    message = []

    play_game(message)
