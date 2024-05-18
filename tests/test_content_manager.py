import unittest
from unittest.mock import patch, mock_open
from app.content_manager import ContentManager

class TestContentManager(unittest.TestCase):
    def setUp(self):
        # Setup before each test
        self.content_manager = ContentManager(number_of_projects=2)
        self.content_manager.run_number = 1  # Mocking run_number to be 1

    def test_run_number(self):
        # Test that the run number is not None
        self.assertIsNotNone(self.content_manager.get_run_number())
        
    def test_get_project_index(self):
        # The remainder of 1 divided by 2 is 1
        self.assertEqual(self.content_manager.get_project_index(), 1)
        
    @patch('builtins.open', new_callable=mock_open, read_data='Project content')
    def test_read_project_content(self, mock_file):
        # Mocking run_number to be 0
        self.content_manager.run_number = 0
        self.assertEqual(self.content_manager.read_project_content(), 'Project content')

    @patch('builtins.open', mock_open(read_data='#job #career\n#hiring'))
    def test_read_project_hashtags_file_exists(self, mock_file):
        hashtags = self.content_manager.read_project_hashtags()
        self.assertEqual(hashtags, '#job #career #hiring')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_project_hashtags_file_not_found(self, mock_file):
        hashtags = self.content_manager.read_project_hashtags()
        self.assertIsNone(hashtags)

    @patch('builtins.open', mock_open(read_data=''))
    def test_read_project_hashtags_empty_file(self, mock_file):
        hashtags = self.content_manager.read_project_hashtags()
        self.assertEqual(hashtags, '')

if __name__ == '__main__':
    unittest.main()
