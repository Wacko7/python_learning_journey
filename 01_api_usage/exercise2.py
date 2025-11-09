import requests
import json

crypto = input("Enter the cryptocurrency id (e.g., 'bitcoin', 'ethereum'): ").strip().lower()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd,eur"
response = requests.get(url)

if response.status_code != 200:
    print("Request failed. Status code:", response.status_code)
    exit()

data = response.json()

if crypto not in data:
    print(f"'{crypto}' not found. Check spelling or try another coin.")
    exit()

usd = data[crypto]["usd"]
eur = data[crypto]["eur"]

print(f"\nCurrent {crypto.capitalize()} price:")
print("USD:", usd)
print("EUR:", eur)

# Save to file
filename = f"price_{crypto}.json"
with open(filename, "w") as f:
    json.dump({crypto: {"usd": usd, "eur": eur}}, f, indent=2)

print(f"\nData saved to {filename}")
