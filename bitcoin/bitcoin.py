import json
import requests
import sys


try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    quantity = sys.argv[1]

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=33c955a5da0effc1ecf7a350227cbc0ba89456208da70d5805299de185490e7b")

    r = response.json()
    amount = float(r["data"]["priceUsd"]) * float(quantity)

    print(f"${amount:,.4f}")


except requests.exceptions.RequestException:
    sys.exit("Request error")
except ValueError:
    sys.exit("Command-line argument is not a number")
