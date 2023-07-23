# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

with open("website.html", mode="r", encoding="utf-8") as html_file:
    html_doc = html_file.read()

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# The find_all() method scans the entire document looking for result
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# 
for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.get("class"))
# print(section_heading.getText())

# if we want to look for a specific anchortag, we could do it like this: soup.find_all(name="a")
# but in a website, there are thousands of anchortags, so the above is not ideal.
# we can select through css selectors to specifically look for an anchortag inside an element
company_url = soup.select_one(selector="p a")
print(company_url)
# we can select through css selectors to specifically look for an anchortag inside an id
name = soup.select_one(selector="#name")
print(name)
# we can select through css selectors to specifically look for an anchortag inside a class
title = soup.select(selector=".heading")
print(title)