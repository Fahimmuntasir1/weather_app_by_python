# Creating a weather app using python
# - - - - - - - - - - -- - ----------->>
import requests

# get api key from openweathermap.org
api_key = "66c7de2faaa5e5c7252ac24458a454de"
user_input = input("Enter a city: ")
weather_data = (
    f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"
)

response = requests.get(weather_data)
# print(response.json())

# Add condition to avoid unexpected errors
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    country = data["sys"]["country"]
    print(f"Temperature: {temperature - 273} C")
    print(f"Description: {description}")
    print(f"Country: {country}")
else:
    print("Something went wrong in this app, try again later.")
