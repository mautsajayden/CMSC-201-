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
Lab Section: <YOUR LAB SECTION>
Email: mautsajayden11@gmail.com
Description: This program runs a dice-based instruction game.
It handles commands like add, sub, mul, nop, jmp, and hlt to modify
the player's position and score on a generated game board.
"""

# -------------------------------------------------------------
# Function Definitions
# -------------------------------------------------------------


def instructions(message, position, score, roll, size_num):
    """
    Handles the game's instruction commands and updates
    the position and score based on the message.

    :param message: str, the instruction (e.g., "add 5", "jmp 3")
    :param position: int, current player position
    :param score: int, current player score
    :param roll: int, last dice roll
    :param size_num: int, the size of the game board
    :return: tuple (position, score, roll, finished)
    """
    if "add" in message:
        score += extract_value(message)
        roll = control_position()
        position += roll

    elif "sub" in message:
        score -= extract_value(message)
        roll = control_position()
        position += roll

    elif "mul" in message:
        score *= extract_value(message)
        roll = control_position()
        position += roll

    elif "nop" in message:
        roll = control_position()
        position += roll

    elif "jmp" in message:
        roll = control_position()
        jump_to = extract_value(message)

        # Move directly to target if within bounds, otherwise roll forward
        if jump_to < size_num:
            position = jump_to
        else:
            position += roll

    elif "hlt" in message:
        roll = control_position()
        print(f"Final Pos: {position} Final Score: {score}, Instruction {message}")
        return position, score, roll, True

    return position, score, roll, False


def control_position():
    """
    Rolls the dice to determine player movement.
    :return: int, the result of a dice roll
    """
    return roll_dice()


def extract_value(command):
    """
    Extracts the integer value from a command string like "add 5".
    :param command: str, a command containing a number
    :return: int, the extracted number
    """
    parts = command.split()
    if len(parts) == 2:
        return int(parts[1])
    return 0


def nop_comms():
    """
    Executes a no-operation command by rolling the dice.
    :return: int, the result of a dice roll
    """
    return roll_dice()


def jump_comm():
    """
    Placeholder for jump command compatibility.
    :return: int, always returns 0
    """
    return 0


def display_grid(length_of_map):
    """
    Displays the game grid on the console.
    :param length_of_map: int, the length of the grid
    :return: None
    """
    print(make_grid(length_of_map))


def play_game(game_map, size_num):
    """
    Runs the main game loop until the player halts or finishes the map.

    :param game_map: list of str, the sequence of instructions
    :param size_num: int, total size of the game board
    :return: None
    """
    position = 0
    score = 0
    roll = 0
    finished = False

    # Main game loop
    while not finished and position < len(game_map):
        message = game_map[position]
        position, score, roll, finished = instructions(
            message, position, score, roll, size_num
        )
        print("Pos:", position, "Score:", score, ", instruction", message, "Rolled:", roll)

    # Prevent index errors if position goes off the map
    if position >= len(game_map):
        position = len(game_map) - 1

    # Game ends naturally (no halt instruction)
    if not finished:
        print(f"Final Pos: {position} Final Score: {score}, Instruction {game_map[position]}")


def ask_user():
    """
    Asks the user for the board size and seed.
    :return: tuple (seed, size)
    """
    size_seed = input("Board Size and Seed: ")
    size = 0
    seed = 0
    parts = size_seed.split()

    if len(parts) >= 1:
        size = int(parts[0])
    if len(parts) >= 2:
        seed = int(parts[1])

    return seed, size


# -------------------------------------------------------------
# Main Execution
# -------------------------------------------------------------
if __name__ == "__main__":
    seed_num, size_num = ask_user()

    # Generate game grid and map
    the_grid = make_grid(size_num)
    message = generate_random_map(size_num, seed_num)

    # Fill grid with commands
    for index in range(size_num):
        fill_grid_square(the_grid, size_num, index, message[index])

    # Display grid
    for row in the_grid:
        print(''.join(row))

    # Start the game
    play_game(message, size_num)
