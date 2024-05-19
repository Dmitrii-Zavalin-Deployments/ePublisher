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
        
    def test_get_project_image_path(self):
        expected_path = 'content/images/1.png'
        self.assertEqual(self.content_manager.get_project_image_path(), expected_path)
        
    @patch('app.content_manager.ContentManager.read_project_content')
    @patch('app.content_manager.ContentManager.read_project_hashtags')
    def test_prepare_post_message(self, mock_read_hashtags, mock_read_content):
        mock_read_content.return_value = 'Project content'
        mock_read_hashtags.return_value = '#job #career #hiring'
        expected_message = 'Project content\n#job #career #hiring'
        self.assertEqual(self.content_manager.prepare_post_message(), expected_message)

    def test_get_run_division(self):
        # Assuming run_number is 5 and number_of_projects is 2
        self.content_manager.run_number = 5
        self.content_manager.number_of_projects = 2
        # The integer division of 5 by 2 is 2
        self.assertEqual(self.content_manager.get_run_division(), 2)

    def test_split_into_sentences(self):
        content = "This is a sentence. And this is another one! Is this the third sentence? \"Yes, it is,\" she said."
        expected_sentences = [
            "This is a sentence.",
            "And this is another one!",
            "Is this the third sentence?",
            "\"Yes, it is,\" she said."
        ]
        self.assertEqual(self.content_manager.split_into_sentences(content), expected_sentences)

    @patch('app.content_manager.ContentManager.read_project_content')
    def test_split_into_sentences_with_read_content(self, mock_read_content):
        mock_read_content.return_value = "First sentence. Second sentence! \"Third sentence,\" he said?"
        expected_sentences = [
            "First sentence.",
            "Second sentence!",
            "\"Third sentence,\" he said?"
        ]
        content = self.content_manager.read_project_content()
        self.assertEqual(self.content_manager.split_into_sentences(content), expected_sentences)

if __name__ == '__main__':
    unittest.main()
