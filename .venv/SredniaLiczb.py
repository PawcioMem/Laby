def srednia_arytmetyczna(*args):
    lis = []
    for i in args:
        lis.append(i)
    suma = sum(lis)
    wynik = suma/len(lis)
    print("Srednia wynosi: ", wynik)
