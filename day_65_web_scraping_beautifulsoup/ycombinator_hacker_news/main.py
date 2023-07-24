from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
ycombinator_website = response.text

soup = BeautifulSoup(ycombinator_website, "html.parser")

# -------------------- find single items -------------------- #
# article_tag = soup.find(class_="titleline")
# print(article_tag)

# # get the article title: tr class="athing" > td class="title" > span class="titleline" > a
# article_title = article_tag.select_one(selector="a[href]").getText()
# print(article_title)

# # get the article link
# article_link = article_tag.select_one(selector="a[href]").get("href")
# print(article_link)

# # get the score: tr > td class="subtext" > span class="subline" > span class="score"
# article_score = soup.find(class_="score").getText()
# print(article_score.split(" ")[0])


# -------------------- find all items -------------------- #
article_titles = []
article_links = []

articles = soup.find_all(class_="titleline")
for article_tag in articles:
    title = article_tag.select_one(selector="a[href]").getText()
    article_titles.append(title)
    
    link = article_tag.select_one(selector="a[href]").get("href")
    article_links.append(link)

# article_scores = []
article_upvotes = soup.find_all(name="span", class_="score")
# for score in article_upvotes:
#     article_score = int(score.getText().split(" ")[0])
#     article_scores.append(article_score)
# convert the for loop to list comprehension: new_list = [new_item for item in list if test]
article_scores = [int(score.getText().split(" ")[0]) for score in article_upvotes]

# print(article_titles)
# print(article_links)
# print(article_scores)

highest_score = max(article_scores)
index_with_the_highest_score = article_scores.index(highest_score)
print(article_titles[index_with_the_highest_score])
print(article_links[index_with_the_highest_score])
print(highest_score)
