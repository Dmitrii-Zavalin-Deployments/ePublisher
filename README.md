Content description / Requirements to the tweets length::

1. content/hashtags/<file.txt> - contains hashtags that are added to each post for the project with the number in name <file.txt>. Keep each hashtag from the new line. Keep only key hashtags here. The smaller number of chracters altogether for all the text in content/hashtags/<file.txt>, the better.

2. content/images/<file.txt> - contains images tht are added to posts for the project with the number in name <file.txt>.

3. content/links/<file.txt> - contains the part of the post with links to the project with the number in name <file.txt> and some advertising text for the project with the number in name <file.txt> (are added to each post for the project with the number in name <file.txt>). The length of the links posts (content/links/<file.txt>) should be no more than 120 characters. Put the text for the post in 1 line in each file: content/links/<file.txt>. Keep the links posts (content/links/<file.txt>) in short sentences.

4. content/text/<file.txt> - contains the key phrases/words/sentences for the project with the number in name <file.txt>. The AI-generated parts of posts are created from this information. Each new key phrase/word/sentence should be added from the new line.

Reminder to update FACEBOOK_LONG_LIVED_ACCESS_TOKEN:

FACEBOOK_LONG_LIVED_ACCESS_TOKEN needs to be regenerated each 3 months and extended to FACEBOOK_LONG_LIVED_ACCESS_TOKEN

1. Use this link to generate token: https://developers.facebook.com/tools/explorer/
2. Copy the token from the previous link (step 1), and use this link to extend access token: https://developers.facebook.com/tools/debug/accesstoken/
3. Add the new environment secret FACEBOOK_LONG_LIVED_ACCESS_TOKEN for Github Actions

Adding content to publish:

1. Post image should be in .png format (/content/images/<file.png>)
2. Same file names for image, text, link, hashtag for each post (for example, /content/images/0.png, /content/text/0.txt, /content/links/0.txt, /content/hashtags/0.txt)
3. Name files for image, text,link, hashtag in a number (maximum number in file names in the folder +1)
