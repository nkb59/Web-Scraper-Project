#import libraries

from bs4 import BeautifulSoup 
import requests
import time 
import datetime 
import smtplib 

#Connect to Website 

def check_price(): 
    URL = 'http://books.toscrape.com/catalogue/the-murder-of-roger-ackroyd-hercule-poirot-4_852/index.html'


    get_url = requests.get(URL)
    get_text = get_url.text
    soup1 = BeautifulSoup(get_text, "html.parser")



    title = soup1.find_all('h1')


    title1 = []
    for tags in title:
        title1.append(tags.text)


    print(title1)






    price = soup1.find('p',{'class':'price_color'})
    price1 = []
    for tags in price:
        price1.append(tags.text)

    print(price1)


    stock = soup1.find('p',{'class':'instock availability'})
    stock1 = []
    for tags in stock:
        stock1.append(tags.text)

    print(stock1)


#Get the date and time for when the data is pulled from the site 

    import datetime

    today = datetime.date.today()

    print(today)


#Create a CSV to put all the data into 

    import csv 

    header = ['Title', 'Price', 'Stock', 'Date']
    data = [title,price,stock,today]


    with open('WebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

 

    with open('WebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
#Set a timer for how many seconds the check_price method should run 

while(True):
    check_price()
    time.sleep(86400)
    
import pandas as pd

df = pd.read_csv(r'/Users/niketanbaranwal/Downloads/WebScraperDataset.csv')

print(df)

#Create a method to send an email once the item you want is at a price you can afford
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('niketan2225@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Book you want is below £45! Now is your chance to buy!"
    body = "Niketan, This is the moment we have been waiting for. Now is your chance to pick up the book of your dreams. Don't mess it up! Link here: http://books.toscrape.com/catalogue/the-murder-of-roger-ackroyd-hercule-poirot-4_852/index.html"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'niketan2225@gmail.com',
        msg
     
    )
