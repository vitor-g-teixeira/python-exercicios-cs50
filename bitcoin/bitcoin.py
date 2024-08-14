import requests
import sys

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    price_now = r["bpi"]["USD"]["rate"].replace(",", "")

    try:
        dolar_value = float(sys.argv[1]) * float(price_now)
        if dolar_value > 1000:
            dolar_value = str(dolar_value)
            formatted_value, cents = dolar_value.split(".", 2)
            cents = cents[:4]
            cents = "." + cents

            numb_letters = 0
            for letter in formatted_value:
                numb_letters += 1

            iterations = 0
            while numb_letters > 3:
                iterations += 1
                formatted_value = formatted_value[:-3 * iterations] + "," + formatted_value[-3 * iterations:]
                numb_letters -= 3
            dolar_value = formatted_value + cents
        print("$" + dolar_value, end = "")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")

except requests.RequestException:
    print("erro")
