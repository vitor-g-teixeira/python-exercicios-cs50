
def main():
    amount_due = 50
    money_input = 0

    while amount_due > 0:
        print("Amount Due: ", amount_due, sep="")
        money_input = int(input("Insert Coin: "))
        if money_input <= 25:
            amount_due = amount_due - money_input

    print("Change Owed: ", amount_due * -1, sep="")

main()
