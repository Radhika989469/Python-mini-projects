from requests import get
from pprint import PrettyPrinter

# New free API - no key needed
BASE_URL = "https://api.exchangerate-api.com/v4/latest/"

printer = PrettyPrinter()

def get_currencies():
    # Get all currencies from base USD
    try:
        data = get(BASE_URL + "USD").json()
        currencies = list(data['rates'].keys())
        currencies.append("USD")
        currencies.sort()
        return currencies
    except Exception as e:
        print(f"Error getting currencies: {e}")
        return ["USD", "INR", "EUR", "GBP"]

def print_currencies(currencies):
    for c in currencies:
        print(f"- {c}")

def exchange_rate(currency1, currency2):
    try:
        url = BASE_URL + currency1
        data = get(url).json()

        if 'rates' not in data:
            print('Invalid base currency.')
            return None

        rates = data['rates']
        if currency2 not in rates:
            print('Invalid target currency.')
            return None

        rate = rates[currency2]
        print(f"{currency1} -> {currency2} = {rate}")
        return rate

    except Exception as e:
        print(f"Error getting rate: {e}")
        return None

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount:.2f} {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")

main()