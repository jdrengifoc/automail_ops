import unittest
import os
from src import init

class TestInitMethods(unittest.TestCase):

    def test_initialize_folder(self):
        test_folder = './temp_folder'
        init.initialize_folder(test_folder)
        self.assertTrue(os.path.exists(test_folder),  f"{test_folder} does not exist.")
        os.rmdir(test_folder)


if __name__ == '__main__':
    unittest.main()