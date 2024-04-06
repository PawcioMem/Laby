def Silnia(liczba):
    if liczba == 0:
        return 1
    else:
        return liczba * Silnia(liczba - 1)
