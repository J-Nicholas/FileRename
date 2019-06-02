import unittest
from src.menu.menu import Menu

class MenuTest(unittest.TestCase):

    def test_empty_options(self):
        """Make sure that constructor with no arguments has no options"""
        test_menu = Menu()

        self.assertEqual(test_menu.options, [])

    def test_valid_options(self):
        """Verify that list of options provided works correctly"""
        options = ["A",
                   "B",
                   "C"]
        test_menu = Menu(options)
        
        self.assertEqual(test_menu.options[0], "A")
        self.assertEqual(test_menu.options[1], "B")
        self.assertEqual(test_menu.options[2], "C")

    def test_single_option(self):
        test_menu = Menu("single")

        self.assertEqual(test_menu.options[0], "single")

    def test_bad_input(self):
        test_menu = Menu([1,2])
        

if __name__ == "__main__":
    unittest.main()
