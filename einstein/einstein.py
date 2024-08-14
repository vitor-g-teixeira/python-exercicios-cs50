def main():
    m = int(input("Choose the mass (kg) wich you wanna know the equivalent in Joules: "))
    c = 300000000
    e = round(m * pow(c, 2))
    print(e)

main()
