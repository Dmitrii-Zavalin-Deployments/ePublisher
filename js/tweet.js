const { TwitterApi } = require('twitter-api-v2');

const twitterClient = new TwitterApi({
  appKey: process.env.TWITTER_API_KEY,
  appSecret: process.env.TWITTER_API_SECRET_KEY,
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

// Function to convert the GitHub URL to a local path
function convertUrlToLocalPath(url) {
  const githubContentUrl = 'https://github.com/Dmitrii-Zavalin-Deployments/ePublisher/blob/main/';
  const localBasePath = 'content/images/'; // Adjust this to the local path where images are stored
  if (url.startsWith(githubContentUrl)) {
    // Extract the path after 'main/' and before '?raw=true'
    const imagePath = url.split('main/')[1].split('?')[0];
    return imagePath; // Construct the local path
  }
  return url; // Return the original URL if it's not a GitHub URL
}

// Function to create a tweet with text and a local image path
async function tweetWithTextAndImage(text, imagePath) {
  try {
    // Convert the GitHub URL to a local path
    // const localImagePath = convertUrlToLocalPath(imagePath);

    // Upload the image to Twitter and get the media ID
    // const mediaId = await twitterClient.v1.uploadMedia(localImagePath);
    
    // Create a tweet with the text and the media ID
    await twitterClient.v2.tweet(text);

    const jsTweets = await twitterClient.v2.searchAll('Land your dream job with AI! No ads, no fees, just success. Start now:');
    // Consume fetched tweet from first page of jsTweets
    for (const tweet of jsTweets) {
      console.log(tweet);
    }
    
  } catch (error) {
    console.error('Error:', error);
  }
}

// Get the image URL and text content from command line arguments
const imageUrl = process.argv[2];
const textContent = process.argv[3];

// Call the function with the provided arguments
tweetWithTextAndImage(textContent, imageUrl)
  .then(() => console.log('Tweeted successfully!'))
  .catch(console.error);
