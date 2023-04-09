import requests
import json
from datetime import date, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "JRPPY8W3PZ7UKXM1"
NEWS_API_KEY = "458229a041764004b09c21e241202d6c"
TWILIO_SID = "AC36861dd063c4b20e3e61e6ff8b81ea79"
TWILIO_AUTH_TOKEN = "8fac0e4849894746b095b1a29bdc17f1"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#get the prpices for last few days
stock_params = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol":STOCK_NAME,
    "interval":"30min",
    "apikey":STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params= stock_params)

#gets needed data into dictionary
data = stock_response.json()["Time Series (30min)"]

#checks what was the price on yesterday's closing (in fact it's from 3 days ago XD)
yesterday = date.today()-timedelta(days=3)
yesterdayClosingTime = (yesterday.strftime("%Y")+"-"+yesterday.strftime("%m")+"-"+yesterday.strftime("%d")+" 20:00:00")
yesterdayClosingPrice = (data[yesterdayClosingTime]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price

befYesterday = date.today()-timedelta(days=4)
befYesterdayClosingTime = (befYesterday.strftime("%Y")+"-"+befYesterday.strftime("%m")+"-"+befYesterday.strftime("%d")+" 20:00:00")
befYesterdayClosingPrice = (data[befYesterdayClosingTime]["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
differenceClosingPrice = float(yesterdayClosingPrice) - float(befYesterdayClosingPrice)
up_down = None
if differenceClosingPrice > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
differencePercentage = (differenceClosingPrice*100/float(befYesterdayClosingPrice))



#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

differencePercentage = 5.7 #toberemoved later
differenceRounded = round(differencePercentage)
print(differenceRounded)

news_params = {
    "apiKey":NEWS_API_KEY,
    "q":COMPANY_NAME,
    "searchIn":"title",
}

if differencePercentage >= 5:
    #print("Get news")


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:1]



#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME} {up_down}{differenceRounded}%\n Headline: {article['title']}. \n\nBrief: {article['description']}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 
    for article in formatted_articles:
        message = client.messages.create(body = article, from_ = '+15076323424',to = '+48730176733')


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

