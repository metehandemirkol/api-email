import requests

api_key = "c15eb79e866d435689bcfcd228807e91"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-01-13&sortBy=publishedAt&apiKey=" \
      "c15eb79e866d435689bcfcd228807e91"
#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description

for article in content["articles"]:
      print(article["title"])
      print(article["description"])
      