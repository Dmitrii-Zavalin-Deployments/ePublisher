import unittest
from app.content_manager import ContentManager

class TestContentManager(unittest.TestCase):
    def setUp(self):
        # Setup before each test
        self.content_manager = ContentManager()

    def test_run_number(self):
        # Test that the run number is not None
        self.assertIsNotNone(self.content_manager.get_run_number())

if __name__ == '__main__':
    unittest.main()
