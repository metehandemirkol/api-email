import requests
topic = "tesla"
api_key = "c15eb79e866d435689bcfcd228807e91"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-01-13&sortBy=publishedAt&apiKey=" \
      "c15eb79e866d435689bcfcd228807e91&"
      "language=en"
#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description

body = ''
for article in content["articles"][:20]:
      if article["title"]   is not None:
            body = body + article["title"] + "\n"\
                   + article['description']\
                   +"\n" +article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)