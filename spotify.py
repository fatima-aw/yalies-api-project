import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Declare CLIENT_ID and CLIENT_SECRET as strings
CLIENT_ID = "6b6c7a583625420184e0b3f37ef7f80c"
CLIENT_SECRET = "43a28faf01344c4da98a64605e38c9cb"

# Spotify Auth URL
AUTH_URL = 'https://accounts.spotify.com/api/token'

# Authentication
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# Convert response to JSON
auth_response_data = auth_response.json()

# Save the access token
access_token = auth_response_data['access_token']

# Set up headers
headers = {'Authorization': f'Bearer {access_token}'}

# Spotify API base URL
BASE_URL = 'https://api.spotify.com/v1/'

# Get track ID from user input
track_id = input('Enter track id: ')

# Make a request to the Spotify API
response = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response in JSON format
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code}")

