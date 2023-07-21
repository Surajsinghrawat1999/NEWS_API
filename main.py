import requests
from send_email import send_email

api_key = "963c46df67804606afa5c6b730a4288b"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-21&sortBy=publishedAt&apiKey=963c46df67804606afa5c6b730a4288b"

request = requests.get(url)

content = request.json()
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
