import requests
import os

# Function to refresh the token
def refresh_token(app_id, app_secret, long_lived_token):
    # The URL to request the long-lived access token
    token_url = 'https://graph.facebook.com/oauth/access_token'
    
    # Parameters for the request
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': app_id,
        'client_secret': app_secret,
        'fb_exchange_token': long_lived_token
    }
    
    # Make the request
    response = requests.get(token_url, params=params)
    
    # Extract the long-lived access token from the response
    new_long_lived_token = response.json().get('access_token')
    
    # Log the new token
    print('New long-lived Access Token is generated')
    return new_long_lived_token

class EPublisherFacebookManager:
    def __init__(self):
        self.app_id = os.environ.get('FACEBOOK_APP_ID')
        self.app_secret = os.environ.get('FACEBOOK_APP_SECRET')
        self.long_lived_token = os.environ.get('FACEBOOK_LONG_LIVED_ACCESS_TOKEN')
        self.page_id = os.environ.get('FACEBOOK_PAGE_ID')
        self.page_access_token = refresh_token(self.app_id, self.app_secret, self.long_lived_token)

    def post_to_facebook(self, image_path, text_content):
        # The URL to make the post request
        post_url = f'https://graph.facebook.com/v19.0/{self.page_id}/feed'
        
        # Parameters for the post request
        data = {
            'message': text_content,
            'link': image_path,
            'published': 'true',
            'access_token': self.page_access_token
        }
        
        # Make the post request
        response = requests.post(post_url, data=data)
        
        # Check if the post was successful
        if response.status_code == 200:
            print('Post was successfully published on Facebook')
        else:
            print(f'Failed to publish post on Facebook: {response.content}')
        
        return response

    def get_facebook_posts(self):
        # The URL to get the posts
        get_url = f'https://graph.facebook.com/v19.0/{self.page_id}/feed?access_token={self.page_access_token}'
        
        # Make the get request
        response = requests.get(get_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print('Successfully retrieved posts from Facebook')
        else:
            print(f'Failed to retrieve posts from Facebook: {response.content}')
        
        return response.json()

    def print_message_before_hashtag(self, posts_json):
        messages_before_hashtag = []
        ids = []

        for post in posts_json['data']:
            # Split the message at the first hashtag
            message_parts = post['message'].split('#', 1)
            message_before_hashtag = message_parts[0].strip()
            print('Message before Hashtag: ')
            print(message_before_hashtag)
            
            # Collect the id
            ids.append(post['id'])

        return ids
