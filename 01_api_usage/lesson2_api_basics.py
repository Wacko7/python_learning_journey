# lesson2_api_basics.py
# Lesson 2 — API Basics (CoinGecko Example)
# Goal: Fetch live Bitcoin data from an online API using the requests library.

import requests

# 1. Define the API endpoint (CoinGecko free API)
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# 2. Send an HTTP GET request to the API
response = requests.get(url)

# 3. Check that the request was successful (status 200 = OK)
print("Status code:", response.status_code)

# 4. Parse the returned JSON text into a Python dictionary
data = response.json()

# 5. Inspect the structure of the returned data
print("Full JSON response:", data)

# 6. Extract the Bitcoin price in USD
btc_price_usd = data["bitcoin"]["usd"]
print("Current Bitcoin price (USD):", btc_price_usd)

# 7. Save the data into a local JSON file
import json
result = {"bitcoin_price_usd": btc_price_usd}

with open("btc_price.json", "w") as f:
    json.dump(result, f, indent=2)

print("\nBitcoin price saved to btc_price.json")
