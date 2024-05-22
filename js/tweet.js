const { TwitterApi } = require('twitter-api-v2');
const fs = require('fs');

const twitterClient = new TwitterApi({
  appKey: process.env.TWITTER_API_KEY,
  appSecret: process.env.TWITTER_API_SECRET_KEY,
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

// Function to create a tweet with text only
async function tweetWithText(text) {
  try {
    const response = await twitterClient.v2.tweet(text);
    console.log('Tweeted successfully!');
    console.log('Tweet ID:', response.data.id);
    // Write the entire response object to tweets.json
    fs.writeFileSync('tweets.json', JSON.stringify(response, null, 2));
  } catch (error) {
    console.error('Error:', error);
  }
}

// Get the text content from command line arguments
const textContent = process.argv[3];

// Call the function with the provided arguments
tweetWithText(textContent)
  .catch(console.error);
