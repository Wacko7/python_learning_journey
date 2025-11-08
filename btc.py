# Week 1 Project — Bitcoin Data Basics

import json
import requests

# 1. Create and save basic Bitcoin information
btc_info = {
    "name": "Bitcoin",
    "symbol": "BTC",
    "market_cap": 1280000000000
}

with open("btc_info.json", "w") as f:
    json.dump(btc_info, f, indent=4)

print("btc_info.json created.")

# 2. Fetch live Bitcoin price from CoinGecko API
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = requests.get(url)
data = response.json()

price = data["bitcoin"]["usd"]
print(f"Current BTC price: ${price}")

# 3. Save the live price to a JSON file
with open("btc_price.json", "w") as f:
    json.dump({"bitcoin_price_usd": price}, f, indent=4)

print("btc_price.json saved.")

# 4. Read the price back from the file and display it
with open("btc_price.json", "r") as f:
    loaded_data = json.load(f)

print("Stored BTC price:", loaded_data["bitcoin_price_usd"])
