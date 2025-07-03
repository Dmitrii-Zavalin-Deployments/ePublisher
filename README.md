# Content Description and Requirements for Tweets Length

## File Structure

- **`content/hashtags/<file.txt>`**  
  Contains hashtags that are added to each post for the project with the number in the name `<file.txt>`.  
  - Keep each hashtag on a new line.  
  - Only include key hashtags.  
  - Minimize the number of characters in total for all hashtags in `content/hashtags/<file.txt>`.

- **`content/images/<file.png>`**  
  Contains images that are added to posts for the project with the number in the name `<file.png>`.  
  - Images should be in `.png` format.

- **`content/links/<file.txt>`**  
  Contains the part of the post with links to the project (with the number in the name `<file.txt>`) and some advertising text for the project.  
  - Length of links posts should not exceed **120 characters**.  
  - Keep the text for posts as **short sentences**.  
  - Text for posts must be written in **1 line** in each file: `content/links/<file.txt>`.

- **`content/text/<file.txt>`**  
  Contains the key phrases, words, or sentences for the project with the number in the name `<file.txt>`.  
  - The AI-generated parts of posts are based on this information.  
  - Add each new key phrase, word, or sentence on a new line.

---

## Reminder to Update Access Tokens

- **FACEBOOK_LONG_LIVED_ACCESS_TOKEN**  
  - Needs to be regenerated **every 2 months** and extended.  
  - Steps:  
    1. Use this link to generate the token: [https://developers.facebook.com/tools/explorer/](https://developers.facebook.com/tools/).  
    2. Copy the token from step 1, then use this link to extend the access token: [https://developers.facebook.com/tools/debug/accesstoken/](https://developers.facebook.com/tools/debug/accesstoken/).  
    3. Add the new token as the environment secret `FACEBOOK_LONG_LIVED_ACCESS_TOKEN` for GitHub Actions.

- **INSTAGRAM_ACCESS_TOKEN**  
  - Needs to be updated **every 2 months**.  
  - Steps:  
    1. Open the [Meta for Developers](https://developers.facebook.com/apps/) page: [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/).  
    2. Select the application and click on it.  
    3. On the left-hand menu, select **Instagram**, then click **API Setup with Instagram Login**.  
    4. Follow the steps to generate a new token (step 1).  
    5. Add the new token as the environment secret `INSTAGRAM_ACCESS_TOKEN` for GitHub Actions.

---

## Guidelines for Adding Content to Publish

- Post images should be in `.png` format: `/content/images/<file.png>`.  
- Use the **same file names** for image, text, link, and hashtag for each post. Example:  
  - `/content/images/0.png`  
  - `/content/text/0.txt`  
  - `/content/links/0.txt`  
  - `/content/hashtags/0.txt`  
- Name the files with numbers (e.g., `0`, `1`, `2`). Use the **maximum number in the folder + 1** for naming new files.



