import unittest
from jmps_and_hlts import generate_random_map, instructions, roll_dice

class TestJumpsAndHlts(unittest.TestCase):

    def test_map_10_17(self):
        seed = 17
        size = 10
        game_map = generate_random_map(size, seed)
        
        # Simulate game manually
        position = 0
        score = 0
        finished = False

        while not finished:
            command = game_map[position]
            position, score, roll, finished = instructions(command, position, score, 0, size)
        
        self.assertEqual(position, 9)
        self.assertEqual(score, 0)
    
    def test_map_31_15(self):
        seed = 15
        size = 31
        game_map = generate_random_map(size, seed)
        
        position = 0
        score = 0
        finished = False

        while not finished:
            command = game_map[position]
            position, score, roll, finished = instructions(command, position, score, 0, size)

        self.assertEqual(position, 16)
        self.assertEqual(score, 145)

    def test_map_40_229900(self):
        seed = 229900
        size = 40
        game_map = generate_random_map(size, seed)
        
        position = 0
        score = 0
        finished = False

        while not finished:
            command = game_map[position]
            position, score, roll, finished = instructions(command, position, score, 0, size)

        self.assertEqual(position, 34)
        self.assertEqual(score, 1941)

if __name__ == "__main__":
    unittest.main()
