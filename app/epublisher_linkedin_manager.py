import requests
import os

class EPublisherLinkedInManager:
    def __init__(self):
        self.access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')  # Get LinkedIn access token from environment variables
        self.person_id = os.getenv('LINKEDIN_PERSON_ID')  # Get LinkedIn person ID from environment variables

    def post_to_linkedin(self, text_content):
        if not self.person_id:
            print("Person ID is not available. Unable to post to LinkedIn.")
            return

        url = 'https://api.linkedin.com/v2/ugcPosts'

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0'
        }

        payload = {
            "author": f"urn:li:person:{self.person_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": text_content
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 201:
            print("Successfully posted on LinkedIn.")
        else:
            print("Failed to post on LinkedIn:", response.json())


