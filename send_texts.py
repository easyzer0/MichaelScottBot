import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from twilio.rest import Client
from twilio_keys import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
import requests

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)


def sendMessage():

    quotes = []
    url = "https://netflixlife.com/2022/02/18/best-michael-scott-quotes-the-office-every-mood/"
    driver = webdriver.Chrome("/Users/obi/chromedriver")
    driver.get(url)

    quoteList = driver.find_elements(By.CSS_SELECTOR,
                                     "em")

    for quote in quoteList:
        if quote.text != 'The Office':
            quotes.append(quote.text)

    driver.quit()

    quoteSelection = random.choice(quotes)

    print("Quote found. Sending to recipients...")

    memberDict = {}

    textMessage = requests.get("http://localhost:8000/api/member/").json()

    for i in range(len(textMessage)):
        memberDict[textMessage[i]['first_name']] = textMessage[i]['number']

    for i in memberDict:
        dailyQuote = "Hey, " + i.title() + "! Here's your daily Michael Scott quote! - EasyBot\n\n" + \
        quoteSelection
        client.messages.create(body=dailyQuote,
                               from_="19106065149",
                               to=memberDict[i])
    
    print("Text messages sent successfully...")

sendMessage()
