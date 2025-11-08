import json
import requests
from datetime import datetime


url = "https://mempool.space/api/blocks"
response = requests.get(url)
blocks =response.json()

for block in blocks[:5]:
    print("Block Height:",block['height'])
    print("Block ID:",block["id"])
    print("Transactions:",block["tx_count"])
    print("Size (bytes):",block["size"])
    time = datetime.fromtimestamp(block["timestamp"])
    print("Time:",time)
    print()

