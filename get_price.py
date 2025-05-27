import requests
from datetime import datetime

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]
    now = datetime.utcnow().isoformat()
    print(f"[{now} UTC] Bitcoin price: ${price}")

if __name__ == "__main__":
    fetch_bitcoin_price()
