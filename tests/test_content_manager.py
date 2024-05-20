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
        expected_path = 'https://github.com/Dmitrii-Zavalin-Deployments/ePublisher/blob/main/content/images/1.png?raw=true'
        self.assertEqual(self.content_manager.get_project_image_path(), expected_path)
        
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

    @patch('app.content_manager.ContentManager.read_project_content')
    def test_select_sentence(self, mock_read_content):
        mock_read_content.return_value = "First sentence. Second sentence! \"Third sentence,\" he said?"
        self.content_manager.run_number = 5  # This will set get_run_division() to 2
        expected_sentence = "\"Third sentence,\" he said?"
        self.assertEqual(self.content_manager.select_sentence(), expected_sentence)

    @patch('app.content_manager.ContentManager.read_project_content')
    def test_select_sentence_no_sentences(self, mock_read_content):
        mock_read_content.return_value = ""
        self.assertIsNone(self.content_manager.select_sentence())

    def test_get_hashtagged_words(self):
        sentence = "This is a test sentence with some longwords."
        expected_result = ['#This', '#test', '#sentence', '#with', '#some', '#longwords']
        self.assertEqual(self.content_manager.get_hashtagged_words(sentence), expected_result)

    def test_get_hashtagged_words_no_long_words(self):
        sentence = "It is an."
        expected_result = []
        self.assertEqual(self.content_manager.get_hashtagged_words(sentence), expected_result)

    def test_get_hashtagged_words_mixed_length_words(self):
        sentence = "Short and lengthy words mixed."
        expected_result = ['#Short', '#lengthy', '#words', '#mixed']
        self.assertEqual(self.content_manager.get_hashtagged_words(sentence), expected_result)

    def test_get_hashtagged_words_removes_punctuation(self):
        content_manager = ContentManager(number_of_projects=1)
        sentence = "Hello, world! This is a test-sentence with some longwords."
        expected_result = ['#Hello', '#world', '#This', '#test-sentence', '#with', '#some', '#longwords']
        self.assertEqual(content_manager.get_hashtagged_words(sentence), expected_result)

    def test_prepare_post_message_with_additional_hashtags(self):
        with patch('content_manager.ContentManager.read_project_content', return_value='Content'):
            with patch('content_manager.ContentManager.read_project_hashtags', return_value='#original #hashtags'):
                post_message = self.content_manager.prepare_post_message(['#additional', '#hashtags'])
                expected_message = 'Content\n#original #hashtags #additional #hashtags'
                self.assertEqual(post_message, expected_message)

    def test_prepare_post_message_with_no_additional_hashtags(self):
        with patch('content_manager.ContentManager.read_project_content', return_value='Content'):
            with patch('content_manager.ContentManager.read_project_hashtags', return_value='#original #hashtags'):
                post_message = self.content_manager.prepare_post_message([])
                expected_message = 'Content\n#original #hashtags'
                self.assertEqual(post_message, expected_message)

    def test_prepare_post_message_with_no_original_hashtags(self):
        with patch('content_manager.ContentManager.read_project_content', return_value='Content'):
            with patch('content_manager.ContentManager.read_project_hashtags', return_value=''):
                post_message = self.content_manager.prepare_post_message(['#additional', '#hashtags'])
                expected_message = 'Content\n #additional #hashtags'
                self.assertEqual(post_message, expected_message)

    def test_create_post_data(self):
        # Test the create_post_data method with sample data
        project_image_path = 'content/images/sample.png'
        post_message = 'Sample post message with #hashtags'
        expected_result = {
            'project_image_path': project_image_path,
            'post_message': post_message
        }
        result = self.content_manager.create_post_data(project_image_path, post_message)
        self.assertEqual(result, expected_result)

    def test_with_hashtag(self):
        self.assertEqual(get_text_before_hashtag("Hello #World"), "Hello")

    def test_without_hashtag(self):
        self.assertEqual(get_text_before_hashtag("Hello World"), "Hello World")

    def test_hashtag_at_start(self):
        self.assertEqual(get_text_before_hashtag("#Hello World"), "")

    def test_hashtag_at_end(self):
        self.assertEqual(get_text_before_hashtag("Hello World#"), "Hello World")

    def test_multiple_hashtags(self):
        self.assertEqual(get_text_before_hashtag("Hello #World #Python"), "Hello")

    def test_only_hashtag(self):
        self.assertEqual(get_text_before_hashtag("#"), "")

    def test_empty_string(self):
        self.assertEqual(get_text_before_hashtag(""), "")

    def test_hashtag_with_spaces(self):
        self.assertEqual(get_text_before_hashtag("Hello # World"), "Hello")

    def test_multiple_hashtags_with_spaces(self):
        self.assertEqual(get_text_before_hashtag("Hello # World # Python"), "Hello")

if __name__ == '__main__':
    unittest.main()
