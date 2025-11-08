import json
import requests
from datetime import datetime


url = "https://mempool.space/api/blocks"
response = requests.get(url)
blocks =response.json()

block_id =  blocks[-1]["id"]
tx_url = f"https://mempool.space/api/block/{block_id}/txs"
tx_response = requests.get(tx_url)
transactions = tx_response.json()
'''
for tx in transactions[:3]:
    print("Transaction ID:", tx['txid'])
    print("Number of outputs:", len(tx["vout"]))
    print("Value (satoshis):", sum(output["value"] for output in tx["vout"]))
    print("Value (BTC):", sum(output["value"] for output in tx["vout"]) / 100_000_000)
    print("value (USD):", (sum(output["value"] for output in tx["vout"]) / 100_000_000) * 106839)  # Assuming BTC price is $106,839
    print()
'''
total_value_btc = 0
for tx in transactions:
    total_value_btc += sum(output["value"] for output in tx["vout"]) / 100_000_000
print("Total value of all transactions in the latest block (BTC):", total_value_btc)
print("Total value of all transactions in the latest block (USD):", total_value_btc * 106839)  # Assuming BTC price is $106,839
print()