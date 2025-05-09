const { TwitterApi } = require('twitter-api-v2');
const fs = require('fs');

const twitterClient = new TwitterApi({
  appKey: process.env.TWITTER_API_KEY,
  appSecret: process.env.TWITTER_API_SECRET_KEY,
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

// Function to filter out hashtags longer than 25 characters
function filterLongHashtags(textContent) {
  return textContent.split(' ').filter(word => {
    return !(word.startsWith('#') && word.length > 25);
  }).join(' ');
}

// Function to delete tweets with text matching the provided content
// async function deleteMatchingTweets(textContent) {
//   let existingTweets = [];
//   if (fs.existsSync('tweets.json')) {
//     const existingData = fs.readFileSync('tweets.json', 'utf8');
//     existingTweets = JSON.parse(existingData);
//   }

//   // Function to compare text content excluding links
//   function compareExcludingLinks(tweetText, inputText) {
//     const tweetWords = tweetText.split(' ').filter(word => !word.startsWith('http://') && !word.startsWith('https://'));
//     const inputWords = inputText.split(' ').filter(word => !word.startsWith('http://') && !word.startsWith('https://'));
//     return tweetWords.join(' ') === inputWords.join(' ');
//   }

//   // Filter out tweets with matching text content excluding links
//   const matchingTweetIds = existingTweets
//     .filter(tweet => compareExcludingLinks(tweet.data.text, textContent))
//     .map(tweet => tweet.data.id);

//   console.log('Matching tweet IDs:', matchingTweetIds);

//   // Delete matching tweets and update the tweets.json file
//   for (const tweetId of matchingTweetIds) {
//     try {
//       await twitterClient.v2.deleteTweet(tweetId);
//       console.log(`Deleted tweet ID: ${tweetId}`);
//     } catch (error) {
//       console.error(`Error deleting tweet ID ${tweetId}:`, error);
//     }
//   }

//   // Remove deleted tweets from the existingTweets array
//   const updatedTweets = existingTweets.filter(
//     tweet => !matchingTweetIds.includes(tweet.data.id)
//   );

//   // Write the updated list back to tweets.json
//   fs.writeFileSync('tweets.json', JSON.stringify(updatedTweets, null, 2));
// }

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
let textContent = process.argv[3];

// Filter out long hashtags from the text content
textContent = filterLongHashtags(textContent);
/*
// Add a unique hashtag based on the current date and time
const now = new Date();
const year = now.getFullYear();
const month = String(now.getMonth() + 1).padStart(2, '0');
const day = String(now.getDate()).padStart(2, '0');
const hour = String(now.getHours()).padStart(2, '0');
const minute = String(now.getMinutes()).padStart(2, '0');
const uniqueHashtag = `#${year}${month}${day}${hour}${minute}`;
textContent += ` ${uniqueHashtag}`;
*/
// First, delete matching tweets (commented out)
// deleteMatchingTweets(textContent)
//   .then(() => {
//     // Then, tweet the new content
//     tweetWithText(textContent);
//   })
//   .catch(console.error);

// Directly tweet the new content
tweetWithText(textContent);
