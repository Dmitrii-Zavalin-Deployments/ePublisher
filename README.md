Requirements to the tweets length:

1. The length of the text posts (/content/text/<file.txt>) should be no more than 125 characters
2. The sum of the length of the text posts (/content/text/<file.txt>) and the hashtags (/content/hashtags/<file.txt>) should be no more than 220 characters
3. Keep the text posts (/content/text/<file.txt>) in short sentences

Reminder to update FACEBOOK_LONG_LIVED_ACCESS_TOKEN:

FACEBOOK_LONG_LIVED_ACCESS_TOKEN needs to be regenerated each 3 months and extended to FACEBOOK_LONG_LIVED_ACCESS_TOKEN

1. Use this link to generate token: https://developers.facebook.com/tools/explorer/
2. Copy the token from the previous link (step 1), and use this link to extend access token: https://developers.facebook.com/tools/debug/accesstoken/
3. Add the new environment secret FACEBOOK_LONG_LIVED_ACCESS_TOKEN for Github Actions