import requests
from config import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET

def get_user_access_token(app_id, app_secret):
    url = "https://graph.facebook.com/oauth/access_token"
    params = {
        'client_id': app_id,
        'client_secret': app_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('access_token', None)

class EPublisherFacebookManager:
    def __init__(self):
        self.app_id = FACEBOOK_APP_ID
        self.app_secret = FACEBOOK_APP_SECRET
        self.user_access_token = get_user_access_token(self.app_id, self.app_secret)

    def post_new_content(self, image_path, text_content):
        # Logic to post new content on the user's personal page
        if self.user_access_token is None:
            print("No user access token available. Cannot post content.")
            return
        url = f"https://graph.facebook.com/me/photos"
        payload = {
            'message': text_content,
            'url': image_path,
            'access_token': self.user_access_token
        }
        response = requests.post(url, data=payload)
        if response.ok:
            print("Content posted successfully.")
        else:
            print(f"Failed to post content. Error: {response.text}")
