import requests
import os

class EPublisherFacebookManager:
    def __init__(self):
        self.app_id = os.environ.get('FACEBOOK_APP_ID')
        self.app_secret = os.environ.get('FACEBOOK_APP_SECRET')
        self.long_lived_token = os.environ.get('FACEBOOK_LONG_LIVED_ACCESS_TOKEN')
        self.page_id = os.environ.get('FACEBOOK_PAGE_ID')
        self.page_access_token = os.environ.get('FACEBOOK_LONG_LIVED_ACCESS_TOKEN')
        self.instagram_access_token = os.environ.get('INSTAGRAM_ACCESS_TOKEN')

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

    def print_message_before_hashtag(self, posts_json, content_before_hashtag):
        ids = []
        for post in posts_json['data']:
            # Split the message at the first hashtag
            message_parts = post['message'].split('#', 1)
            message_before_hashtag = message_parts[0].strip()
            print('Message before Hashtag: ')
            print(message_before_hashtag)

            # Compare and collect the id if the text matches
            if message_before_hashtag == content_before_hashtag:
                ids.append(post['id'])
                print(f"Id is added to delete: {post['id']}")
        return ids

    def delete_facebook_posts(self, post_ids):
        deleted_ids = []
        for post_id in post_ids:
            # The URL to delete the post
            delete_url = f'https://graph.facebook.com/v19.0/{post_id}?access_token={self.page_access_token}'

            # Make the delete request
            response = requests.delete(delete_url)

            # Check if the delete was successful
            if response.status_code == 200:
                print(f'Post with ID {post_id} was successfully deleted from Facebook')
                deleted_ids.append(post_id)
            else:
                print(f'Failed to delete post with ID {post_id}: {response.content}')

        return deleted_ids

    def post_to_instagram(self, image_path, text_content):
        # Step 1: Upload the image to Instagram
        upload_url = 'https://graph.instagram.com/v19.0/me/media'
        upload_data = {
            'image_url': image_path,
            'caption': text_content,
            'access_token': self.instagram_access_token
        }
        upload_response = requests.post(upload_url, data=upload_data)
        if upload_response.status_code != 200:
            print(f'Failed to upload image to Instagram: {upload_response.content}')
            return upload_response

        # Step 2: Publish the uploaded image
        media_id = upload_response.json().get('id')
        publish_url = f'https://graph.instagram.com/v19.0/me/media_publish'
        publish_data = {
            'creation_id': media_id,
            'access_token': self.instagram_access_token
        }
        publish_response = requests.post(publish_url, data=publish_data)
        if publish_response.status_code == 200:
            print('Post was successfully published on Instagram')
        else:
            print(f'Failed to publish post on Instagram: {publish_response.content}')

        return publish_response