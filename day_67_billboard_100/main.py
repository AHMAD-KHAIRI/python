from bs4 import BeautifulSoup
import requests
from datetime import datetime


today = datetime.now()
date_today = today.strftime("%Y/%m/%d")

# prompt = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")


URL="https://www.billboard.com/charts/hot-100/2000-08-12"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
# print(soup.prettify)

first_song_title = []
first_title = soup.find(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")

for song_title in first_title:
    title = song_title.getText().replace("\n\n\t\n\t\n\t\t\n\t\t\t\t\t", "").replace("\t\t\n\t\n", "")
    first_song_title.append(title)
# print(first_song_title)

first_song_artist = []
first_artist = soup.find(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")
for song_artist in first_artist:
    artist = song_artist.getText().replace("\n\t\n\t", "").replace("\n", "")
    first_song_artist.append(artist)
# print(first_song_artist)

remaining_song_titles = []
remaining_titles = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

for song_title in remaining_titles:
    title = song_title.getText().replace("\n\n\t\n\t\n\t\t\n\t\t\t\t\t", "").replace("\t\t\n\t\n", "")
    remaining_song_titles.append(title)
# print(len(remaining_song_titles))

remaining_song_artists = []
remaining_artists = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")

for song_artist in remaining_artists:
    artist = song_artist.getText().replace("\n\t\n\t", "").replace("\n", "")
    remaining_song_artists.append(artist)
# print(len(remaining_song_artists))

top_100_song_titles = first_song_title + remaining_song_titles
top_100_song_artists = first_song_artist + remaining_song_artists


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
# my_playlist = spotify.user_playlist_create(user=f"{CURRENTUSER_ID}", name="New Playlist", description="Create new playlist with Python", public=False)


# TO-DO 3: Get the user playlist
# my_playlist = spotify.user_playlists(user=f"{CURRENTUSER_ID}", )
# print(my_playlist)


# TO-DO 4: Get the user id of the authenticated user (your Spotify username).
# Hint: Use this method: current_user()
user_id = spotify.current_user()
# print(user_id)


# TO-DO 5: create a list of Spotify song URIs for the list of song names you found from step 1 (scraping billboard 100).
all_song_uris = []
for every_track in top_100_song_titles:
    try:
        search_track = spotify.search(q=f"track:{every_track}", type="track", market="US", limit=1)
        song_uri = search_track["tracks"]["items"][0]["uri"]
        all_song_uris.append(song_uri)
    except IndexError:
        pass


# TO-DO 6: Add each of the song uri to the new playlist.
# def listToString(all_song_uris):
#     str1 = ","
#     return (str1.join(all_song_uris))
# print(listToString(all_song_uris))

playlist_id = os.environ.get("MY_PLAYLIST_ID")
# spotify.user_playlist_add_(user=user_id, playlist_id=playlist_id, tracks=listToString(all_song_uris), position=None)
spotify.playlist_add_items(playlist_id=playlist_id, items=all_song_uris)