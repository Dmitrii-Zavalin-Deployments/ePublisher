const { TwitterApi } = require('twitter-api-v2');
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const twitterClient = new TwitterApi({
  appKey: process.env.TWITTER_API_KEY,
  appSecret: process.env.TWITTER_API_SECRET_KEY,
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

const imageUrl = process.argv[2];
const textContent = process.argv[3];

async function downloadImage(imageUrl) {
  const response = await axios({
    url: imageUrl,
    responseType: 'stream',
  });
  
  const localPath = path.resolve(__dirname, 'temp', path.basename(imageUrl));
  const writer = fs.createWriteStream(localPath);

  response.data.pipe(writer);

  return new Promise((resolve, reject) => {
    writer.on('finish', () => resolve(localPath));
    writer.on('error', reject);
  });
}

async function tweetWithTextAndImage(text, imageUrl) {
  try {
    const localImagePath = await downloadImage(imageUrl);
    const mediaId = await twitterClient.v1.uploadMedia(localImagePath);
    await twitterClient.v2.tweet({
      text: text,
      media: { media_ids: [mediaId] }
    });
    console.log('Tweeted successfully!');
  } catch (error) {
    console.error('Error:', error);
  }
}

// Call the function with the provided arguments
tweetWithTextAndImage(textContent, imageUrl)
  .then(() => console.log('Tweeted successfully!'))
  .catch(console.error);
