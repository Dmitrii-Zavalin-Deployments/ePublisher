const { TwitterApi } = require('twitter-api-v2');

const twitterClient = new TwitterApi({
  appKey: process.env.TWITTER_API_KEY,
  appSecret: process.env.TWITTER_API_SECRET_KEY,
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

// Function to create a tweet with text only
async function tweetWithText(text) {
  try {
    // Create a tweet with the text
    await twitterClient.v2.tweet(text);
    console.log('Tweeted successfully!');
  } catch (error) {
    console.error('Error:', error);
  }
}

// Function to get the recent tweets of a user by user ID
async function getRecentTweetsByUserId(userId) {
  try {
    // Retrieve the user's recent tweets
    const userTweets = await twitterClient.v2.get(`users/${userId}/tweets`, {
      max_results: 5,
      'tweet.fields': 'created_at', // Include additional fields if needed
    });

    // Log the results
    console.log('Recent tweets:', userTweets);

    // Return the recent tweets
    return userTweets;
  } catch (error) {
    console.error('Error:', error);
  }
}

// Get the text content from command line arguments
const textContent = process.argv[3];
const userId = process.env.TWITTER_USER_ID; // Read the user ID from the environment variable

// Call the function with the provided arguments
tweetWithText(textContent)
  .catch(console.error);

// Call the function to get recent tweets by user ID
getRecentTweetsByUserId(userId)
  .then((tweets) => console.log('Found tweets:', tweets))
  .catch(console.error);
