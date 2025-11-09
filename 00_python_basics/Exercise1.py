import json
btc_price_usd = float(input("Enter the current Bitcoin price in USD: "))
holding_btc = float(input("Enter the amount of Bitcoin you hold: "))

portfolio_value = btc_price_usd * holding_btc
portfolio_value_eur = portfolio_value * 0.92

print("Your portfolio value:")
print("USD:", portfolio_value)
print("EUR:", portfolio_value_eur)

data = {
    "btc_price_usd": btc_price_usd,
    "btc_owned": holding_btc,
    "portfolio_usd": portfolio_value,
    "portfolio_eur": portfolio_value_eur
}

with open ("portfolio.json", "w") as f:
    json.dump(data,f, indent=2)

print("Portfolio data saved to portfolio.json")
