
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from datetime import date

today = date.today()

print(date.today())

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&interval=60min&apikey=SZ0FOZU6GGMIB6LC"
r = requests.get(url)
data = r.json()

keys = list(data['Time Series (Daily)'].keys())
price_yes = float(data['Time Series (Daily)'][keys[0]]["4. close"])
price_bef_yes = float(data['Time Series (Daily)'][keys[1]]["4. close"])
if price_yes - price_bef_yes >= 0.02 * price_bef_yes or price_bef_yes - price_yes >= 0.02 * price_bef_yes:
    news_ = True
else:
    print("no")

if news_:
    news_url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-11-15&sortBy=publishedAt&language=en&apiKey=ca3bc0bf5733403b89e039d2c207ddf4'
    n = requests.get(news_url)
    news = n.json()
    # print(news)
    art_1 = news['articles'][0]
    art_2 = news["articles"][1]
    # print(art_1)
    # print(art_2)

    from twilio.rest import Client

    account_sid = 'AC1ed2dfc31dd4618abf484b0fd5172fb2'
    auth_token = 'b2e192386cb681f81982e4c85c881d57'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+16562163246',
        body=f'Headline: {art_1["title"]}\nNews:{art_1["description"]}\n\n\nHeadline:{art_2["title"]}\nNews:{art_2["description"]}',
        to='+917223085309'
    )

    print(message.sid)
