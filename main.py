import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import time

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
POLL_INTERVAL = 30  # seconds between live updates

def get_crypto_price(crypto_symbol):
    response = requests.get(f"{COINGECKO_API_URL}/simple/price", params={
        'ids': crypto_symbol,
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }, headers={"accept": "application/json"}, timeout=10)
    response.raise_for_status()
    data = response.json()
    if crypto_symbol not in data:
        raise ValueError(f"Cryptocurrency '{crypto_symbol}' not found.")
    return data[crypto_symbol]['usd'], data[crypto_symbol]['usd_24h_change']

def get_historical_data(crypto_symbol, days):
    response = requests.get(f"{COINGECKO_API_URL}/coins/{crypto_symbol}/market_chart", params={
        'vs_currency': 'usd',
        'days': days
    }, timeout=10)
    response.raise_for_status()
    data = response.json()
    if 'prices' not in data:
        raise ValueError(f"No historical data for '{crypto_symbol}'.")
    return data['prices']

def run_live_tracker(crypto, days):
    """Poll price every POLL_INTERVAL seconds and update chart live."""
    # Seed with historical data
    historical = get_historical_data(crypto, days)
    times  = [datetime.datetime.fromtimestamp(p[0] / 1000, tz=datetime.timezone.utc) for p in historical]
    prices = [p[1] for p in historical]

    plt.ion()  # Interactive mode — non-blocking
    fig, ax = plt.subplots(figsize=(12, 6))

    print(f"\nTracking {crypto} live. Press Ctrl+C to stop.\n")

    while True:
        try:
            price, change = get_crypto_price(crypto)
            times.append(datetime.datetime.now(tz=datetime.timezone.utc))
            prices.append(price)

            ax.clear()
            ax.plot(times, prices, color='royalblue', linewidth=1.5)
            ax.fill_between(times, prices, alpha=0.1, color='royalblue')
            ax.set_title(f"{crypto.capitalize()}  |  ${price:,.2f}  |  24h: {change:+.2f}%", fontsize=14)
            ax.set_xlabel("Time (UTC)")
            ax.set_ylabel("Price (USD)")
            ax.tick_params(axis='x', rotation=45)
            ax.grid(True, linestyle='--', alpha=0.5)
            fig.tight_layout()
            plt.pause(0.1)  # Refresh chart without blocking

            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {crypto}: ${price:,.2f}  ({change:+.2f}%)")
            time.sleep(POLL_INTERVAL)

        except KeyboardInterrupt:
            print("\nTracker stopped.")
            break
        except Exception as e:
            print(f"Error: {e}. Retrying in {POLL_INTERVAL}s...")
            time.sleep(POLL_INTERVAL)

def main():
    crypto = input("Enter cryptocurrency (e.g. bitcoin, ethereum): ").strip().lower()
    while True:
        try:
            days = int(input("Days of history to preload (e.g. 1, 7, 30): "))
            if days <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")

    run_live_tracker(crypto, days)

if __name__ == "__main__":
    main()