import unittest
import boggle
# These are the 26 ASCII uppercase characters A through Z
from string import ascii_uppercase

# This class inherrits from the unittest class testcase


class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """

    def test_can_create_an_empty_grid(self):
        # Test to see if we can create an empty grid
        grid = boggle.make_grid(0, 0)
        self.assertEqual(len(grid), 0)

    def test_grid_size_is_width_times_height(self):
        # Test is to ensure that the total size of the grid
        # is equal to the width * height
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)

    def test_grid_coordinates(self):
        # Test to ensure that all of the coordinates
        # inside of the grid can be accessed
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)

    def test_grid_is_filled_with_letters(self):
        # Ensure that each of the coordinates in the grid
        # contains a letter
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)

    def test_neighbours_of_a_position(self):
        # Ensure that a grid position has 8 neighbours
        coords = (1, 2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)

    def test_all_grid_neighbours(self):
        # Ensure that all of the grid positions have neighbors
        grid = boggle.make_grid(2, 2)
        neighbors = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbors), len(grid))
        for pos in grid:
            # Creates a new list from the dictionary's keys
            others = list(grid)
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))

    def test_converting_a_path_to_a_word(self):
        # Ensure that paths can be converted to words
        # The path to word function should return the same
        # strings that we manualy construct in the test
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid)

        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])

    def test_search_grid_for_words(self):
        # Esure that certain patterns can be found in a path_to_word
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = 'EEE'
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]

        foundWords = boggle.search(grid, dictionary)

        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)


# class test_boggle(unittest.TestCase):
#    def test_is_this_thing_on(self):
#        self.assertEqual(1, 1)
