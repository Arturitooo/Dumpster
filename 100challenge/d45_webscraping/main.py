import requests
from bs4 import BeautifulSoup

from urllib.request import urlopen

url = "file:///C:/Users/Art/Documents/GitHub/learning/100challenge/d45_webscraping/website.html"
page = urlopen(url)
html_bytes = page.read()
contents = html_bytes.decode("utf-8")


soup = BeautifulSoup(contents, "html.parser")
print(soup.title.name)
print(soup.title.string)
print(soup.title)

# finds all anchors / links on our website
all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)

# finds all paragraphs on our website
all_par_s = soup.findAll(name="p")
print(all_par_s)


for tag in all_anchor_tags:
    print(tag.getText())  # shows text of links
    print(tag.get("href"))  # shows links to websites

heading = soup.find(name="h1", id="name").string
print(heading)

# we're looking here for first element, for which selector is anchor tag "a" in paragraph "p"
company_url = soup.select_one(selector="p a")
# element with id = name in that case h1 element
company_url = soup.select_one(selector="#name")
headings = soup.select(".heading")  # here we're looking for all headings


# scrapping live website
print("-"*30)

data = requests.get("https://news.ycombinator.com/news")

yc_web_page = data.text

soupp = BeautifulSoup(yc_web_page, "html.parser")

print(soupp.title.string)

yc_spans = soupp.find("span", class_="titleline")
yc_links = yc_spans.find("a")


print(yc_links.getText())
print(yc_links.get("href"))

yc_scores = soupp.find("span", class_="score")
print(yc_scores.getText())


# 100movies project

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]

movies = movie_titles[::-1]

with open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d45_webscraping\movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
