def main():
    expression = input("Expression: ")

    x, y, z = expression.split(" ", 3)

    match(y):
        case "+":
            result = float(x) + float(z)
        case "-":
            result = float(x) - float(z)
        case "/":
            result = float(x) / float(z)
        case "*":
            result = float(x) * float(z)

    print(round(result, 1))

main()
