import requests
import json

query = input("Which type of news do you want to see?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-01-14&sortBy=publishedAt&apiKey=f4b48f2e4da1424eb107a2059cbf633f"

r = requests.get(url)
news = json.loads(r.text)

# print(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("\n-------------------------------------------\n")

