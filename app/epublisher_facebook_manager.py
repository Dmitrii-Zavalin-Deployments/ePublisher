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
    print(f'New long-lived Access Token: {new_long_lived_token}')
    return new_long_lived_token

class EPublisherFacebookManager:
    def __init__(self):
        self.app_id = os.environ.get('FACEBOOK_APP_ID')
        self.app_secret = os.environ.get('FACEBOOK_APP_SECRET')
        self.long_lived_token = os.environ.get('FACEBOOK_LONG_LIVED_ACCESS_TOKEN')
        self.page_access_token = refresh_token(self.app_id, self.app_secret, self.long_lived_token)
