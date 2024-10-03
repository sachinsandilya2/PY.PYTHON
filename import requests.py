import requests
from twilio.rest import Client

# OpenWeatherMap API key
api_key = '2aa27409fb729f0fb4155ac2fa6b4d54'
location = 'Muzaffarpur'  # Use quotes to define location

# Twilio account details
account_sid = 'AC6379de6e3dee4265d919444adf7f89f0'
auth_token = '5d7379f7ba5ba6e91ca2c61e4f721d89'
twilio_client = Client(account_sid, auth_token)
from_whatsapp_number = 'whatsapp:+917256932133'  # Twilio sandbox number
to_whatsapp_number = 'whatsapp:+91725693233'   # Your WhatsApp number

def get_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def generate_message(weather_data):
    weather_condition = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    
    # Custom messages based on weather condition
    if weather_condition == "Clear":
        return f"Aaj bahut achhi dhup hai! Taapmaan hai {temp}°C. Enjoy the sunny day! 😎"
    elif weather_condition == "Clouds":
        return f"Aaj kuchh badal chhaye hue hain. Taapmaan hai {temp}°C. Stay cozy! ☁️"
    elif weather_condition == "Rain":
        return f"Bahar barish ho rahi hai. Taapmaan hai {temp}°C. Apni chhata lena mat bhoolna! 🌧️"
    elif weather_condition == "Haze":
        return f"Aaj dhund bhari hai. Taapmaan hai {temp}°C. Apna dhyan rakhein! 🌫️"
    elif weather_condition == "Snow":
        return f"Barf gir rahi hai! Taapmaan hai {temp}°C. Garam kapde pehn lo! ❄️"
    else:
        return f"Aaj ka mausam {weather_condition} hai aur taapmaan {temp}°C. Apna din acche se guzariye!"

def send_message(message):
    message = twilio_client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    print(f"Message sent: {message.sid}")

if __name__ == "__main__":
    weather_data = get_weather_data()
    if weather_data:  # Check if weather data was retrieved successfully
        message = generate_message(weather_data)
        send_message(message)
