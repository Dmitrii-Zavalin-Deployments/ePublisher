#!/bin/bash

# Step 1: Provide instructions to the user
echo "To get your Client ID and Client Secret, visit the LinkedIn Developer Portal here:"
echo "https://www.linkedin.com/developers/apps/YOUR_APP_ID/auth"
echo "Copy the Client ID and Client Secret from your application's 'Auth' section."

# Step 2: Prompt the user to enter the Client ID and Client Secret
read -p "Enter your Client ID: " CLIENT_ID
read -p "Enter your Client Secret: " CLIENT_SECRET

# Using a fixed Redirect URI for localhost
REDIRECT_URI="http://localhost:8000/callback"

# Step 3: Direct the user to LinkedIn authorization endpoint
echo "Please open this URL in your browser and authorize the application:"
echo "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=$CLIENT_ID&redirect_uri=$REDIRECT_URI&state=UNIQUE_STATE_VALUE&scope=w_member_social"

# Step 4: Start a simple HTTP server to capture the authorization code
echo "Starting local server to capture authorization code..."
python3 -m http.server 8000 & SERVER_PID=$!

# Step 5: Wait for the user to authorize and capture the authorization code
echo "Once you authorize the application, LinkedIn will redirect you to http://localhost:8000/callback?code=AUTH_CODE"
echo "Please copy the 'code' parameter from the redirected URL and paste it below."

# Manually extract the code parameter
read -p "Enter the authorization code provided by LinkedIn: " AUTH_CODE

# Step 6: Exchange authorization code for access token
response=$(curl -X POST \
  https://www.linkedin.com/oauth/v2/accessToken \
  -d "grant_type=authorization_code" \
  -d "code=$AUTH_CODE" \
  -d "redirect_uri=$REDIRECT_URI" \
  -d "client_id=$CLIENT_ID" \
  -d "client_secret=$CLIENT_SECRET")

# Step 7: Extract the access token
ACCESS_TOKEN=$(echo $response | jq -r '.access_token')

# Step 8: Output the access token
echo "Your access token: $ACCESS_TOKEN"

# Cleanup: Kill the local server
kill $SERVER_PID


