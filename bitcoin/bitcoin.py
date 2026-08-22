import os
import requests
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    
    try:
        quantity = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = os.getenv("coincap_api_key")

    url = "https://rest.coincap.io/v3/assets/bitcoin"

    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
        response.raise_for_status()

        data = response.json()
        price = float(data["data"]["priceUsd"])
        amount = price * quantity

        print(f"${amount:,.4f}")

    except requests.exceptions.RequestException:
        sys.exit("Request error")


if __name__ == "__main__":
    main()

