# Creating a weather app using python
# - - - - - - - - - - -- - ----------->>
import requests

api_key = "66c7de2faaa5e5c7252ac24458a454de"
user_input = input("Enter a city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"

response = requests.get(url)
print(response)
