import requests
from config import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, FACEBOOK_PAGE_ID

def get_app_access_token(app_id, app_secret):
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
        self.page_id = FACEBOOK_PAGE_ID
        self.page_access_token = self.get_page_access_token()

    def get_page_access_token(self):
        # Use the App Access Token to get the Page Access Token
        app_access_token = get_app_access_token(self.app_id, self.app_secret)
        if app_access_token is None:
            print("Failed to get app access token.")
            return None
        url = f"https://graph.facebook.com/{self.page_id}?fields=access_token&access_token={app_access_token}"
        response = requests.get(url)
        data = response.json()
        if 'access_token' in data:
            return data['access_token']
        else:
            print(f"Error getting page access token: {data}")
            return None

    def delete_previous_post(self):
        # Logic to delete the previous day's post
        pass

    def post_new_content(self, image_path, text_content):
        # Logic to post new content
        if self.page_access_token is None:
            print("No page access token available. Cannot post content.")
            return
        url = f"https://graph.facebook.com/v19.0/{self.page_id}/photos"
        payload = {
            'message': text_content,
            'url': image_path,
            'access_token': self.page_access_token
        }
        response = requests.post(url, data=payload)
        if response.ok:
            print("Content posted successfully.")
        else:
            print(f"Failed to post content. Error: {response.text}")
