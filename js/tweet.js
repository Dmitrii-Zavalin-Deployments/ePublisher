// tweet.js
const { TwitterApi } = require('twitter-api-v2');

const twitterClient = new TwitterApi({
  appKey: process.env.TWITTER_API_KEY,
  appSecret: process.env.TWITTER_API_SECRET_KEY,
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

const imagePath = process.argv[2];
const textContent = process.argv[3];
const contentBeforeHashtag = process.argv[4];

// Function to tweet with text and image
async function tweetWithTextAndImage(text, imagePath) {
  // Upload the image and get the media ID
  const mediaId = await twitterClient.v1.uploadMedia(imagePath);
  
  // Create a tweet with the text and the media ID
  await twitterClient.v2.tweet({
    text: text,
    media: { media_ids: [mediaId] }
  });
}

// Call the function with the provided arguments
tweetWithTextAndImage(textContent, imagePath)
  .then(() => console.log('Tweeted successfully!'))
  .catch(console.error);
