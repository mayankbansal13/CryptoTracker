📈 CryptoTracker
A real-time cryptocurrency price tracker built with Python. Fetches live prices from the CoinGecko API and plots an auto-updating chart with historical data.

✨ Features

🔴 Live price tracking — polls the latest price every 30 seconds
📊 Auto-updating chart — live matplotlib graph with price history
📅 Historical data preload — seed your chart with 1, 7, 30+ days of data
📉 24-hour change — shows % change alongside the current price
🚫 No API key required — uses CoinGecko's free public API
⚠️ Error resilient — retries on failure without crashing


🖥️ Demo
Enter cryptocurrency (e.g. bitcoin, ethereum): bitcoin
Days of history to preload (e.g. 1, 7, 30): 7

[14:32:01] bitcoin: $67,432.10  (+2.35%)
[14:32:31] bitcoin: $67,489.55  (+2.41%)
[14:33:01] bitcoin: $67,401.20  (+2.28%)

📦 Requirements

Python 3.7+
requests
matplotlib


🚀 Getting Started

1. Clone the repository
cd crypto-tracker
2. Install dependencies
bashpip install -r requirements.txt
3. Run the tracker
bashpython crypto_tracker.py
4. Follow the prompts
Enter cryptocurrency (e.g. bitcoin, ethereum): ethereum
Days of history to preload (e.g. 1, 7, 30): 7
The chart will open and update every 30 seconds automatically.
Press Ctrl+C to stop.

⚙️ Configuration

You can tweak these constants at the top of crypto_tracker.py:
ConstantDefaultDescriptionPOLL_INTERVAL30Seconds between price updatesCOINGECKO_API_URLCoinGecko v3Base API URL

🪙 Supported Cryptocurrencies

Any coin listed on CoinGecko works. Use the coin's ID (not ticker symbol):
CoinID to enterBitcoinbitcoinEthereumethereumSolanasolanaDogecoindogecoinCardanocardano
To find any coin's ID, search on coingecko.com and check the URL:
https://www.coingecko.com/en/coins/bitcoin

📡 API Reference

This project uses the CoinGecko Public API v3 (no key needed):
EndpointUsed for/simple/priceCurrent price + 24h change/coins/{id}/market_chartHistorical price data
Rate limit on the free tier: ~10–30 requests/min. The 30-second poll interval stays well within this.

🛠️ Troubleshooting

ValueError: Cryptocurrency 'xxx' not found
→ Make sure you're using the CoinGecko coin ID (e.g. bitcoin), not the ticker (BTC).
429 Too Many Requests
→ You've hit the rate limit. Increase POLL_INTERVAL to 60 or more.

🙌 Acknowledgements

CoinGecko API — free crypto data
Matplotlib — charting library
Chart doesn't open
→ Make sure you're not running in a headless environment. Try adding import matplotlib; matplotlib.use('TkAgg') at the top of the file.
