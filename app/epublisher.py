import requests
from config import FACEBOOK_API_KEY, FACEBOOK_PAGE_ID

class EPublisherManager:
    def __init__(self):
        self.page_access_token = FACEBOOK_API_KEY
        self.page_id = FACEBOOK_PAGE_ID

    def delete_previous_post(self):
        # Logic to delete the previous day's post
        pass

    def post_new_content(self, image_path, text_content):
        # Logic to post new content
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
