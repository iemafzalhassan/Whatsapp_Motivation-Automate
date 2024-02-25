import requests

def get_quote_of_the_day(category):
    url = "https://quotes.rest/qod?category={}".format(category)
    res = requests.get(url=url)
    data = res.json()
    status = res.status_code
    match status:
        case 200:
            quote = data['contents']['quotes'][0]['quote']
        case 404:
            quote = data["errror!"]["message"]
        case _:
            quote = "An error occurred"
    return quote

    quote = data['contents']['quotes'][0]['quote']

quotw = get_quote_of_the_day(category="inspire")


