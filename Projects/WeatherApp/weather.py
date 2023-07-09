import requests

API_KEY = "1622849fc9bc6e24be2f5e977246239f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input('Enter a city name: ')
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather']
    description = weather[0]['description']
    temperature = format(data['main']['temp'] - 273.15, ".2f")
    feels_like = format(data['main']['feels_like'] - 273.15, ".2f")
    humidity = data['main']['humidity']

    print(f"\nWeather Today at {city.upper()}:\n")
    print(f"Temperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Overall Weather: {description.upper()}")
else:
    print('Error Occurred')

