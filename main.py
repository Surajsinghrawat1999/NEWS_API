import requests
from send_email import send_email

api_key = "963c46df67804606afa5c6b730a4288b"

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-06-21&" \
      "sortBy=publishedAt&" \
      "apiKey=963c46df67804606afa5c6b730a4288b&" \
      "language=en"

request = requests.get(url)

content = request.json()
body = ""
for article in content["articles"][:20]:        #[:20] now this part will only give 20 news
    if article["title"] is not None:
        body = "Subject:Todays news" + "\n" + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               +article["url"]+ 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
