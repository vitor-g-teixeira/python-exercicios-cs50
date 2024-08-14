def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    get_order(menu)

def get_order(_dictionary):
    _cost = 0
    while True:
        try:
            _order = input("Item: ").title()
        except EOFError:
            break
        else:
            try:
                _cost += _dictionary[_order]
            except ValueError:
                pass
            except KeyError:
                pass
            else:
                print(f"Total: ${_cost:.2f}")
main()
