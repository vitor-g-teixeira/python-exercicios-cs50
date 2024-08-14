try:
    nameList = []
    numero = 0

    while True:
        nameList.append(input("Name:" ))

except EOFError:
    print("\nAdieu, adieu, to ", end="")
    aux = False

    while len(nameList) != 0:
        if len(nameList) == 1:
            print(nameList[numero])
        elif len(nameList) == 2 and aux:
            print(nameList[numero] + "," + " and ", end = "")
        elif len(nameList) == 2:
            print(nameList[numero] + " and ", end = "")
        elif len(nameList) > 2:
            print(nameList[numero] + ", ", end ="")
            aux = True
        nameList.pop(numero)

