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

if __name__ == '__main__':
    unittest.main()
