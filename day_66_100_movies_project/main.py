from bs4 import BeautifulSoup
import requests

URL="https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empireonline_website = response.text

soup = BeautifulSoup(empireonline_website, "html.parser")
# print(soup)

# # First step, try to scrape one movie title:
# movie = soup.find(name="h3", class_="title")
# movie_title = movie.getText()
# print(movie_title)

# If first step is successful, find all movie titles:
all_movies = soup.find_all(name="h3", class_="title")

# # Option 1: Use a for loop
# movie_titles = []
# for movie_title in all_movies:
#     title = movie_title.getText()
#     movie_titles.append(title)

# Alternatively, use list comprehension:
movie_titles = [movie.getText() for movie in all_movies]

# Next, reverse the order in the list
# # Option 1: Use a for loop
# reorder_movie_titles = []
# for n in range(len(movie_titles) - 1, -1, -1):
#     reorder_movie_titles.append(movie_titles[n])

# Alternatively, use python slice operator: a[start:stop:step]
reorder_movie_titles = movie_titles[::-1]
print(reorder_movie_titles)

# Next, save the movie titles in movies.txt
with open("movies.txt", mode="w", encoding="utf-8") as movies_file:
    for movie in reorder_movie_titles:
        movies_file.write(f"{movie}\n")