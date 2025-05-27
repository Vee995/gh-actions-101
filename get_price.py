import sys
import requests
from datetime import datetime, timezone
from typing import Dict
import yaml

def load_config(path: str = "config.yaml") -> Dict[str, str]:
    """
    Load configuration parameters from a YAML file.

    Args:
        path (str): Path to the YAML config file. Defaults to "config.yaml".

    Raises:
        ValueError: If the config file is not a valid YAML mapping or
                    if required keys ('crypto_id', 'vs_currency') are missing.

    Returns:
        Dict[str, str]: Configuration dictionary containing 'crypto_id' and 'vs_currency'.
    """
    with open(path, "r") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("Config file is not a valid YAML mapping")
    if "crypto_id" not in config or "vs_currency" not in config:
        raise ValueError("Config missing 'crypto_id' or 'vs_currency' keys")
    return config

def fetch_crypto_price(crypto_id: str, vs_currency: str) -> None:
    """
    Fetch and print the price of a cryptocurrency in the specified currency,
    along with the current UTC timestamp.

    Args:
        crypto_id (str): Cryptocurrency ID recognized by CoinGecko API (e.g., 'bitcoin').
        vs_currency (str): Currency code to compare against (e.g., 'usd').

    Prints:
        The current UTC timestamp and the fetched price in a formatted string.

    Handles:
        - Network errors and HTTP errors gracefully, printing to stderr.
        - Missing or unexpected data in the API response.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={vs_currency}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data[crypto_id][vs_currency]
    except requests.RequestException as e:
        print(f"Network or HTTP error: {e}", file=sys.stderr)
        return
    except KeyError:
        print(f"Unexpected response structure or invalid crypto_id/vs_currency", file=sys.stderr)
        return

    now = datetime.now(timezone.utc).isoformat()
    print(f"[{now} UTC] {crypto_id.capitalize()} price: {price} {vs_currency.upper()}")

def main() -> None:
    """
    Main entry point of the script.

    Loads the configuration, then fetches and prints the cryptocurrency price.
    Prints errors to stderr if the configuration loading fails.
    """
    try:
        config = load_config()
    except Exception as e:
        print(f"Failed to load config: {e}", file=sys.stderr)
        return
    fetch_crypto_price(config["crypto_id"], config["vs_currency"])

if __name__ == "__main__":
    main()