import requests
from bs4 import BeautifulSoup


url = 'https://www.ceneo.pl/101052360#tab=reviews'
response = requests.get(url)

page = BeautifulSoup(response.text, "html.parser")

opinions = page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").getText().strip()
recommendation = opinion.select_one("span.user-post__author-recomendation > em")
stars = opinion.select("span.user-post__score-count")
content = opinion.select_one("div.user-post__text").getText().strip()
pros = opinion.select_one("div[class$=positives] ~ div.review-feature__item").getText().strip()
cons = opinion.select_one("div[class$=negatives] ~ div.review-feature__item").getText().strip()
useful = opinion.select_one("button.vote-yes").getText().strip()
useless = opinion.select_one("button.vote-yes > span").getText().strip()
published = opinion.select_one("span.user-post__published >time:nth-child(1)")["datetime"]
purchased = opinion.select_one("span.user-post__published >time:nth-child(2)")["datetime"]

print(opinion_id)
print(opinion)
print(type(content))


