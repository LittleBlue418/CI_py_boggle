from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    # Creates a grid that will hold all the tiles
    # for a boggle game
    return {(row, col): choice(ascii_uppercase)
        for row in range(height)
        for col in range(width)
    }

def neighbours_of_position(coords):
    # Get neighbours of a given position
    row = coords[0]
    col = coords[1]

    # Assign each of the neighbours
    # Top-left to top-right
    top_left = (row -1, col -1)
    top_center = (row -1, col)
    top_right = (row -1, col +1)

    # Left to right
    left = (row, col -1)
    # The '(row, col)' coordinates padded to this
    # function are situated here
    right = (row, col +1)

    # Bottom left to right
    bottom_left = (row +1, col -1)
    bottom_center = (row +1, col)
    bottom_right = (row +1, col +1)

    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]

def all_grid_neighbours(grid):
    # Get all of the possible neighbours for each
    # position in the grid
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours

def path_to_word(grid, path):
    # Add all of the letters on the path to a string
    return ''.join([grid[p] for p in path])

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