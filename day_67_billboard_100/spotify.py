# Spotify for Developers
# App name: Billboard to Spotify
# Redirect URI: http://example.com
# spotipy 2.23.0 - A light weight Python library for the Spotify Web API
# pip install spotipy
import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CURRENTUSER_ID = os.environ.get("CURRENTUSER_ID")
CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
ACCESS_TOKEN = os.environ.get("access_token")
scope = "playlist-modify-private"


# TO-DO 1: figure out how to authenticate your Python project with Spotify using your unique Client ID/ Client Secret. 
spotify = spotipy.Spotify(oauth_manager=SpotifyOAuth(
    scope=scope,
    redirect_uri=REDIRECT_URI,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    cache_path="./__pycache__/.cache"))


# TO-DO 2: Create a private playlist using Spotify Api
my_playlist = spotify.user_playlist_create(user=f"{CURRENTUSER_ID}", name="New Playlist", description="Create new playlist with Python", public=False)


# TO-DO 3: Get the user playlist
my_playlist = spotify.user_playlists(user=f"{CURRENTUSER_ID}", )
print(my_playlist)


# TO-DO 4: Get the user id of the authenticated user (your Spotify username).
# Hint: Use this method: current_user()
user_id = spotify.current_user()
print(user_id)


# TO-DO 5: create a list of Spotify song URIs for the list of song names you found from step 1 (scraping billboard 100).
track_name = {"Incomplete"}
artist = "Sisqo"
year = "2000"
search_track = spotify.search(q=f"track:{track_name} artist:{artist}", type="track", market="US", limit=1)
print(search_track)
