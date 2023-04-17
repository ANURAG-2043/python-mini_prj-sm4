import requests
from bs4 import BeautifulSoup
import smtplib
import time

email_id = 'abc.20.23.mp@gmail.com'
email_pass = 'csxrjumclmzfpfmb'

def check_price ():
    URL = "https://www.amazon.in/Apple-iPhone-14-128GB-Blue/dp/B0BDK62PDX/ref=sr_1_5?crid=215WNQTTSDE8&keywords=iphone%2B14&qid=1681734368&sprefix=iphone%2Caps%2C204&sr=8-5&th=1"
    headers = {"user-Agents" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15'  }

    page = requests.get(URL , headers = headers)
    soup = BeautifulSoup(page.content , 'html.parser')
    

    title =soup.find(id = "productTitle").get_text()
    
    price = soup.find(class_ = "a-price-whole").get_text()
    converted_price = int(float(price[0:8].replace(",","")))

    print(title.strip())
    print(converted_price) 
    
    if(converted_price <= 71999):
        send_email()
    else:
        print("Price is not dropped")
        print("No email sent")
        
def send_email():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()  # stablishing connection with the server and the gmail
        server.starttls()
        server.ehlo()

        server.login(email_id, email_pass)

        subject = " Hey The Price Fall!! "
        body = " Check the Amazon link https://www.amazon.in/Apple-iPhone-14-128GB-Blue/dp/B0BDK62PDX/ref=sr_1_5?crid=215WNQTTSDE8&keywords=iphone%2B14&qid=1681734368&sprefix=iphone%2Caps%2C204&sr=8-5&th=1"

        msg = f"Subject : { subject}\n\n{body}"

        server.sendmail(email_id, 'kumbhareanurag1023@gmail.com', msg )
        
        print('HEY EMAIL HAS BEEN SENT!')
        server.quit()  # quit the server

check_price()
time.sleep(2)
    


