import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from twilio.rest import Client
from twilio_keys import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
import requests

# Import tokens from keys file to access APIs
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

# Function to scrape the chosen website for the quotes using Selenium, select a random quote, and send it to members in the database
def sendMessage():

    quotes = []
    url = "https://netflixlife.com/2022/02/18/best-michael-scott-quotes-the-office-every-mood/"
    driver = webdriver.Chrome("/Users/obi/chromedriver")
    driver.get(url)
    # Create a list of quotes with the quotes from the website, using the <em> tag as the CSS selector
    quoteList = driver.find_elements(By.CSS_SELECTOR,
                                     "em")
    # Iterate through the quotes and add them to the list in text form, removing the extra non-quotes in the process
    for quote in quoteList:
        if quote.text != 'The Office':
            quotes.append(quote.text)
    # Close the window
    driver.quit()

    quoteSelection = random.choice(quotes)

    print("Quote found. Sending to recipients...")
    
    memberDict = {}
    # Pull the data from the REST API
    textMessage = requests.get("http://localhost:8000/api/member/").json()
    # Create the member dictionary, with the names as keys and phone numbers as values
    for i in range(len(textMessage)):
        memberDict[textMessage[i]['first_name']] = textMessage[i]['number']
    # Create the text message body, and iterate through the dictionary to add the names to the message and sent it to each member
    for i in memberDict:
        dailyQuote = "Hey, " + i.title() + "! Here's your daily Michael Scott quote! - EasyBot\n\n" + \
        quoteSelection
        client.messages.create(body=dailyQuote,
                               from_="19106065149",
                               to=memberDict[i])
    
    print("Text messages sent successfully...")

sendMessage()
