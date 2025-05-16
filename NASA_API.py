import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=YZ9vjHmuaY4Qfy6JnoFYz22l5IiDTVtQiB3qSMQT"

response = requests.get(url)

print(response.json())
# The above code fetches the current spot price of Bitcoin in USD from the Coinbase API.