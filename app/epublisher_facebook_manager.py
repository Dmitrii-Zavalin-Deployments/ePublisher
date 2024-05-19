import requests
from config import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, FACEBOOK_PAGE_ID

class EPublisherFacebookManager:
    def __init__(self):
        self.app_id = FACEBOOK_APP_ID
        self.app_secret = FACEBOOK_APP_SECRET
        self.page_id = FACEBOOK_PAGE_ID
        self.page_access_token = self.get_page_access_token()

    def get_app_access_token(self):
        # Exchange your App Secret for an App Access Token
        url = f"https://graph.facebook.com/oauth/access_token?client_id={self.app_id}&client_secret={self.app_secret}&grant_type=client_credentials"
        response = requests.get(url)
        data = response.json()
        return data['access_token']

    def get_page_access_token(self):
        # Use the App Access Token to get the Page Access Token
        app_access_token = self.get_app_access_token()
        url = f"https://graph.facebook.com/{self.page_id}?fields=access_token&access_token={app_access_token}"
        response = requests.get(url)
        data = response.json()
        return data['access_token']

    def delete_previous_post(self):
        # Logic to delete the previous day's post
        pass

    def post_new_content(self, image_path, text_content):
        # Logic to post new content
        url = f"https://graph.facebook.com/v19.0/{self.page_id}/photos"
        payload = {
            'message': text_content,
            'url': image_path,
            'access_token': self.page_access_token  # This now uses the Page Access Token
        }
        response = requests.post(url, data=payload)
        if response.ok:
            print("Content posted successfully.")
        else:
            print(f"Failed to post content. Error: {response.text}")
