import unittest
from app.content_manager import ContentManager

class TestContentManager(unittest.TestCase):
    def setUp(self):
        # Setup before each test
        self.content_manager = ContentManager()

    def test_run_number(self):
        # Test that the run number is not None
        self.assertIsNotNone(self.content_manager.get_run_number())
        
    def test_get_project_index(self):
        # Assuming there are 2 projects
        content_manager = ContentManager(number_of_projects=2)
        # Mocking run_number to be 5
        content_manager.run_number = 5
        # The remainder of 5 divided by 2 is 1
        self.assertEqual(content_manager.get_project_index(), 1)
        
    @patch('builtins.open', new_callable=mock_open, read_data='Project content')
    def test_read_project_content(self, mock_file):
        content_manager = ContentManager(number_of_projects=2)
        content_manager.run_number = 0  # Mocking run_number to be 0
        self.assertEqual(content_manager.read_project_content(), 'Project content')

if __name__ == '__main__':
    unittest.main()
