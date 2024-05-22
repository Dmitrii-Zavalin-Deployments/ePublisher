const { TwitterApi } = require('twitter-api-v2');
const fs = require('fs');

const twitterClient = new TwitterApi({
  appKey: process.env.TWITTER_API_KEY,
  appSecret: process.env.TWITTER_API_SECRET_KEY,
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

// Function to create a tweet with text only
function tweetWithText(text) {
  twitterClient.v2.tweet(text)
    .then(response => {
      console.log('Tweeted successfully!');
      console.log('Tweet ID:', response.data.id);
      // Log the entire response object
      console.log('Full response data:', JSON.stringify(response, null, 2));

      // Read existing data from tweets.json (initialize with an empty array if file doesn't exist)
      let existingTweets = [];
      if (fs.existsSync('tweets.json')) {
        const existingData = fs.readFileSync('tweets.json', 'utf8');
        existingTweets = JSON.parse(existingData);
      }

      // Add the new tweet to the existing list
      existingTweets.push(response);

      // Write the updated list back to tweets.json
      fs.writeFileSync('tweets.json', JSON.stringify(existingTweets, null, 2));
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

// Get the text content from command line arguments
const textContent = process.argv[2]; // Corrected index to 2

// Call the function with the provided arguments
tweetWithText(textContent);
