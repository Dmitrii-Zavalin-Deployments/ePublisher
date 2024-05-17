import unittest
from unittest.mock import patch
from file_checker import get_max_file_number, check_sequential_files, calculate_remainder

class TestFileChecker(unittest.TestCase):
    @patch('os.listdir')
    def test_get_max_file_number(self, mock_listdir):
        mock_listdir.return_value = ['0.txt', '1.txt', '2.txt', 'not_a_number.txt']
        directory = 'some_directory'
        self.assertEqual(get_max_file_number(directory), 2)

    @patch('os.listdir')
    @patch('os.path.isfile')
    def test_check_sequential_files(self, mock_isfile, mock_listdir):
        mock_listdir.return_value = ['0.txt', '1.txt', '2.txt']
        mock_isfile.return_value = True
        directories = ['dir1', 'dir2']
        self.assertEqual(check_sequential_files(directories), {'dir1': [], 'dir2': []})

    def test_calculate_remainder(self):
        self.assertEqual(calculate_remainder(10, 3), 1)

if __name__ == '__main__':
    unittest.main()
