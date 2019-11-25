import unittest
import boggle

# This class inherrits from the unittest class testcase
class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """

    def test_can_create_an_empty_grid(self):
        # Test to see if we can create an empty grid
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)


# class test_boggle(unittest.TestCase):
#    def test_is_this_thing_on(self):
#        self.assertEqual(1, 1)