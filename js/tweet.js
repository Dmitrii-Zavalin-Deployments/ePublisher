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

// Function to search for tweets containing specific words
async function searchTweetsWithWords(words) {
  try {
    // Replace 'words' with the actual words you want to search for
    const searchResults = await twitterClient.v2.search(words, { max_results: 10 });

    // Log the results
    console.log('Search results:', searchResults);

    // Return the search results
    return searchResults;
  } catch (error) {
    console.error('Error:', error);
  }
}

// Get the text content from command line arguments
const textContent = process.argv[2];

// Call the function with the provided arguments
tweetWithText(textContent)
  .catch(console.error);

// Example usage of searchTweetsWithWords:
// Replace 'your-search-words' with the words you're looking for in your tweets
searchTweetsWithWords('your-search-words')
  .then((tweets) => console.log('Found tweets:', tweets))
  .catch(console.error);
