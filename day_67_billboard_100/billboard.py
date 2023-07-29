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
print(first_song_title)

first_song_artist = []
first_artist = soup.find(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")
for song_artist in first_artist:
    artist = song_artist.getText().replace("\n\t\n\t", "").replace("\n", "")
    first_song_artist.append(artist)
print(first_song_artist)

remaining_song_titles = []
remaining_titles = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

for song_title in remaining_titles:
    title = song_title.getText().replace("\n\n\t\n\t\n\t\t\n\t\t\t\t\t", "").replace("\t\t\n\t\n", "")
    remaining_song_titles.append(title)
print(len(remaining_song_titles))

remaining_song_artists = []
remaining_artists = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")

for song_artist in remaining_artists:
    artist = song_artist.getText().replace("\n\t\n\t", "").replace("\n", "")
    remaining_song_artists.append(artist)
print(len(remaining_song_artists))