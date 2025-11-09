# lesson1_basics.py

# 1. Variables and arithmetic
btc_price_usd = 68000
holding_btc = 0.25
portfolio_value = btc_price_usd * holding_btc
print("Portfolio value in USD:", portfolio_value)

# 2. Lists and loops
transactions = [12000, -5000, 3000, -2000]
total = 0
for tx in transactions:
    total += tx
print("Net transaction value:", total)

# 3. Dictionaries
wallet = {"address": "bc1xyz...", "balance_btc": 0.25, "owner": "Tito"}
print(wallet["balance_btc"])

# 4. Function example
def usd_to_eur(amount_usd, rate=0.92):
    return amount_usd * rate

print("Portfolio in EUR:", usd_to_eur(portfolio_value))

# 5. JSON example
import json
btc_data = {"price_usd": btc_price_usd, "holdings": holding_btc}
with open("btc_data.json", "w") as f:
    json.dump(btc_data, f, indent=2)
print("Saved JSON file.")
