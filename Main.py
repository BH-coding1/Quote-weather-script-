import datetime
import smtplib
from config import  my_email ,my_password,api_url,API_key
import requests
# ENTER YOUR EMAIL HERE
your_email = ''
# ENTER YOUR CITY HERE WITH CAPITAL LETTER AT BEGINING
your_city = 'Miami'
def main():

    # getting quote data
    response = requests.get(url=api_url)
    data = response.json()
    author= data['quote']['author']
    quote = data['quote']['body']

    # getting weather data
    response2 = requests.get(url=f'https://api.openweathermap.org/data/2.5/weather?q={your_city}&appid={API_key}&units=metric')
    data2 = response2.json()
    temp = data2["main"]["temp"]
    description = data2["weather"][0]["description"]
    humidity = data2["main"]["humidity"]
    wind_speed = data2["wind"]["speed"]

    if response.status_code == 200 and response2.status_code == 200:
        subject = "🌤️ Your Daily Quote & Weather"


        weather = f"""\
        Weather in {your_city}:
        🌡️ Temperature: {temp}°C
        ☁️ Description: {description}
        💧 Humidity: {humidity}%
        💨 Wind Speed: {wind_speed} m/s
        """

        body = f"""
        Good morning!
    
        Here’s your quote for today:
        "{quote}"
        — {author}
    
        
        {weather}
    
        Have an amazing day! 
        """

        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs=your_email,

                                msg=message.encode('utf-8'))
    else :
        print('Error',data.get('message'),data2.get('message'))



main()




