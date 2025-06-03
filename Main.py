import datetime
import smtplib
from config import my_email ,my_password,api_url
import requests
# ENTER YOUR EMAIL HERE
your_email = 'lospollos313@gmail.com'
def main():
    response = requests.get(url=api_url)
    data = response.json()
    author= data['quote']['author']
    quote = data['quote']['body']

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=your_email,msg=f'Subject:Your Daily Quotes and Weather\n\n{quote}\n{author}')

main()




