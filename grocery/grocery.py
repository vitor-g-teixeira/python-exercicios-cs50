
def main():
    user_groceries = get_list()
    user_groceries = dict(sorted(user_groceries.items()))
    for item in user_groceries:
        print(user_groceries[item], item.upper())


def get_list():
    _groceries = {}
    while True:
        try:
            _item = input()
        except EOFError:
            return _groceries
        else:
            if _item in _groceries:
                _groceries[_item] += 1
            else:
                _groceries[_item] = 1

main()
