# Import the BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
# Import the requests module for making HTTP requests
import requests

# URL of the website to scrape
url = "https://www.empireonline.com/movies/features/best-movies-2023/"

# Send an HTTP GET request to the URL and store the response
response = requests.get(url)
# Get the HTML content of the response
html_content = response.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all HTML elements with the tag name "h2" (movie titles)
all_movies = soup.find_all(name="h2")

# Extract the text content of each movie title and store in a list
movie_titles = [movie.getText() for movie in all_movies]

# Reverse the order of the movie titles list
reorder_movie_titles = movie_titles[::-1]

# Print the reversed list of movie titles
print(reorder_movie_titles)

# Open a text file in write mode to store the movie titles
with open("best-movies-2023.txt", mode="w", encoding="utf-8") as file:
    # Write each movie title to the file, followed by a new line
    for movie in reorder_movie_titles:
        file.write(f"{movie}\n")


# from bs4 import BeautifulSoup
# import requests

# # url="https://web.archive.org/web/20231229183922/https://www.empireonline.com/movies/features/best-movies-2023/"
# url="https://www.empireonline.com/movies/features/best-movies-2023/"

# response = requests.get(url)
# html_content = response.text

# # soup = BeautifulSoup(html_content, "html.parser")
# soup = BeautifulSoup(html_content, "lxml")
# # print(soup.prettify())

# # # First step, try to scrape one movie title:
# # movie = soup.find(name="h2")
# # movie_title = movie.getText()
# # print(movie_title)

# # If first step is successful, find all movie titles:
# all_movies = soup.find_all(name="h2")

# # # # Option 1: Use a for loop
# # # movie_titles = []
# # # for movie_title in all_movies:
# # #     title = movie_title.getText()
# # #     movie_titles.append(title)

# # Option 2: Use list comprehension:
# movie_titles = [movie.getText() for movie in all_movies]

# # # Next, reverse the order in the list
# # # # Option 1: Use a for loop
# # # reorder_movie_titles = []
# # # for n in range(len(movie_titles) - 1, -1, -1):
# # #     reorder_movie_titles.append(movie_titles[n])

# # Alternatively, use python slice operator: a[start:stop:step]
# reorder_movie_titles = movie_titles[::-1]
# print(reorder_movie_titles)

# # Next, save the movie titles in movies.txt
# with open("best-movies-2023.txt", mode="w", encoding="utf-8") as file:
#     for movie in reorder_movie_titles:
#         file.write(f"{movie}\n")
