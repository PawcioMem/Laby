#Importowanie wymaganych bibliotek
import datetime
import os
import csv

########################################################

# Manualne wpisanie informacji o ksiazce
def dodaj_ksiazke():
    ID = int(input("Podaj ID ksiazki: "))
    AUTHOR = input("Podaj autora: ")
    TITLE = input("Podaj tytul: ")
    PAGES = int(input("Podaj liczbe stron: "))
    CREATED = date.today()
    UPDATED = date.today()

    # Sprawdzenie czy ID ksiazki juz istnieje w bazie
    with open('book.csv', mode='r') as plik:
        czytnik = csv.reader(plik)
        for row in czytnik:
            if int(row[0]) == ID:       # Jezeli tak, wypisuje komunikat i nie zapisuje ksiazki
                print("Takie ID juz istnieje")
                break
            else:                       # Jezeli nie, ksiazka zostaje wpisana do pliku
                with open('book.csv', mode='a', newline='') as plik:
                    wpisz = csv.writer(plik)
                    wpisz.writerow([ID, AUTHOR, TITLE, PAGES, CREATED, UPDATED])
                    print(f"Ksiazka wpisana: {ID}, {AUTHOR}, {TITLE}, {PAGES}, {CREATED}, {UPDATED}")

########################################################

# Usuwanie ksiazki pod wzgledem ID
def usun_ksiazke_ID():
    ID = input("Podaj ID ksiazki do usuniecia: ")   # Uzytkownik podaje ID ksiazki do usuniecia
    with open('book.csv', mode='r') as plik:
        czytaj = csv.reader(plik)
        wiersze = list(czytaj)

        with open('book.csv', mode='w', newline='') as plik:
            wpisz = csv.writer(plik)
            for wiersz in wiersze:
                if wiersz[0] != str(ID):            # Jezeli ID istnieje ksiazka zostaje usunieta i podany jest komunikat
                    wpisz.writerow(wiersz)
                    print("Ksiazka zostala usunieta")
                else:
                    print("Ksiazka nie zostala usunieta")
                    break

########################################################

# Usuwanie ksiazki pod wzgledem tytulu
def usun_ksiazke_tytul():
    tytul = input("Podaj tytul ksiazki do usuniecia: ")     # Uzytkownik podaje tytul ksiazki do usuniecia
    with open('book.csv', mode='r') as plik:
        czytaj = csv.reader(plik)
        wiersze = list(czytaj)

        with open('book.csv', mode='w', newline='') as plik:
            wpisz = csv.writer(plik)
            for wiersz in wiersze:
                if wiersz[2] != str(tytul):     # Jezeli tytul istnieje ksiazka zostaje usunieta i podany jest komunikat
                    wpisz.writerow(wiersz)
                    print("Ksiazka zostala usunieta")

########################################################

