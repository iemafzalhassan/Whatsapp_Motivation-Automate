import requests
url = "https://quotes.rest/qod?language=en"

res = requests.get(url=url)
data = res.json()
print(data['contents']['quotes'][0]['quote'])