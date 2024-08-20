#from multiprocessing.connection import Client
import os
from twilio.rest import Client
import requests
import schedule
import time


def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(base_url)
    data = response.json()
    return data

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def send_text_message(bod):
    account_sid = "XXXXXXXXXXXXXXXXXXXX"
    auth_token = "XXXXXXXXXXXXXXXXXXXX"
    from_phone_number = "XXXXXXXXXXXXXXXXXXXX"
    to_phone_number = "XXXXXXXXXXXXXXXXXXXX"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=bod,
        from_=from_phone_number ,
        to=to_phone_number
        )
    #print("Text message sent!")

def send_update():
    latitude = 33.9609
    longitude = -83.3779
    weather_data = get_weather(latitude,longitude)
    temperature_celsius = weather_data["hourly"]["temperature_2m"][0]
    temperature_fahrenheit = c_to_f(temperature_celsius)
    print(temperature_celsius)
    print(temperature_fahrenheit)
    weather_info = (
        f"Hello, Joshua\n"
        f"Weather in NY:\n"
        f"Temperature: {temperature_fahrenheit:.2f}°F"
    )
    #send_text_message(weather_info)

def main():
    print("hello")
    send_update()
  #  schedule.every().day.at("08:00").do(send_update)
   # while True:
    #    schedule.run_pending()
     #   time.sleep(1)
if __name__ == "__main__":
    main()