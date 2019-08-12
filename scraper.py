import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/Hamilton-H82315931-Khaki-Scuba-Stainless/dp/B07D5GQ8RR/ref=sr_1_3?crid=3D8DSLZPFIZBM&keywords=hamilton+diver+watch&qid=1565628135&s=gateway&sprefix=hamilton+diver%2Caps%2C244&sr=8-3"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# print(soup.prettify())
def check_price():
    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:7])

    if(converted_price < $350.00):
        send_mail()

    print(title.strip())
    print(converted_price.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(##email, ##password)

    subject = "Price fell down!"
    body = "Check the Amzaon link! https://www.amazon.com/Hamilton-H82315931-Khaki-Scuba-Stainless/dp/B07D5GQ8RR/ref=sr_1_3?crid=3D8DSLZPFIZBM&keywords=hamilton+diver+watch&qid=1565628135&s=gateway&sprefix=hamilton+diver%2Caps%2C244&sr=8-3"

    msg = f"Subject: {subject}/n/n{body}"

    server.sendmail(
        '##from',
        '##to',
        msg
    )

    print('EMAIL SENT')

    server.quit()


while(True):
    check_price()
    time.sleep(60 * 120)

