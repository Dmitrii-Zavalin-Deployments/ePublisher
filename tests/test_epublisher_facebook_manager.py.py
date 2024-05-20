import unittest
from unittest.mock import patch
from epublisher_facebook_manager import EPublisherFacebookManager

class TestEPublisherFacebookManager(unittest.TestCase):
    def setUp(self):
        self.epublisher_facebook_manager = EPublisherFacebookManager()

    @patch('epublisher_facebook_manager.requests.post')
    def test_post_to_facebook(self, mock_post):
        # Mock the post request to return a successful response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'id': '12345'}
        
        # Test the post_to_facebook function
        response = self.epublisher_facebook_manager.post_to_facebook('image_path', 'text_content')
        self.assertEqual(response.status_code, 200)

    @patch('epublisher_facebook_manager.requests.get')
    def test_get_facebook_posts(self, mock_get):
        # Mock the get request to return a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'data': []}
        
        # Test the get_facebook_posts function
        response = self.epublisher_facebook_manager.get_facebook_posts()
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
