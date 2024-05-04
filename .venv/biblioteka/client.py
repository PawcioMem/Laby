# Importowanie wymaganych bibliotek
import datetime
import os
import csv
import random


########################################################

# Rejestracja nowego klienta lub usuwanie danych klienta z bazy
def dodaj_usun_klienta():
    wybor = input("(1) Dodaj nowego klienta lub (2) usun dane klienta z bazy: ")
    # Rejestracja nowego klienta
    if wybor == "1":
        ID = random.randint(1000, 9999)
        NAME = input("Podaj imie i nazwisko nowego klienta: ")
        EMAIL = input("Podaj email nowego klienta: ")
        PHONE = int(input("Podaj numer telefonu nowego klienta: "))
        CREATED = date.today()
        UPDATED = date.today()

        # Sprawdzenie czy ID klienta juz istnieje w bazie
        with open('customer.csv', mode='r') as plik:
            czytaj2 = csv.reader(plik)
            for row in czytaj2:
                if int(row[0]) == ID:  # Jezeli tak, wypisuje komunikat i nie zapisuje klienta
                    print("Takie ID klienta juz istnieje")
                    break
                else:  # Jezeli nie, klient zostaje zapisany do bazy i robiony jest plik .txt
                    with open('customer.csv', mode='a', newlinijka='') as plik:
                        wpisz = csv.writer(plik)
                        wpisz.writerow([ID, NAME, E - MAIL, PHONE, CREATED, UPDATED])
                        print(f"Klient zapisany: {ID}, {NAME}, {E - MAIL}, {PHONE}, {CREATED}, {UPDATED}")
                        # Plik ID.txt
                        nowy_plik = ID + ".txt"
                        file = open(nowy_plik, 'w')
                        file.close()

    # Usuniecie danych klienta
    elif wybor == "2":

        jak_usun = input("Jak usunac dane klienta? Wzgledem (ID) lub (NAME)?: ")
        ######
        if jak_usun == "ID":  # Sposob usuniecia danych klienta wzgledem ID

            ID = input("Podaj ID klienta do usuniecia: ")  # Uzytkownik podaje ID klienta do usuniecia
            with open('customer.csv', mode='r') as plik:
                czytaj = csv.reader(plik)
                wiersze = list(czytaj)

                with open('customer.csv', mode='w', newlinijka='') as plik:
                    wpisz = csv.writer(plik)
                    for wiersz in wiersze:
                        if wiersz[0] != str(ID):  # Jezeli ID istnieje klient zostaje usuniety i podany jest komunikat
                            wpisz.writerow(wiersz)
                            print("Klient zostal usuniety")

        #####
        elif jak_usun == "NAME":  # Sposob usuniecia danych klienta wzgledem ID
            name = input("Podaj imie i nazwisko klienta do usuniecia: ")  # Uzytkownik podaje NAME do usuniecia
            with open('customer.csv', mode='r') as plik:
                czytaj = csv.reader(plik)
                wiersze = list(czytaj)

                with open('customer.csv', mode='w', newlinijka='') as plik:
                    wpisz = csv.writer(plik)
                    for wiersz in wiersze:
                        if wiersz[1] != str(
                                name):  # Jezeli NAME sie zgadza klient jest usuniety i podany jest komunikat
                            wpisz.writerow(wiersz)
                            print("Klient zostal usuniety")

        else:  # Wyjatek do sposobu usuniecia
            print("Sposob usuniecia nie istnieje lub jest podany blednie!")

    else:  # Wyjatek do numeru wyboru miedzy utworzeniem a usunieciem klienta
        print("Niepoprawny numer wyboru!")


########################################################

# Dodawanie przez administratora danych address klienta
def dodaj_address_klient():
    ID = input("Podaj ID Klienta: ")
    with open('address.csv', mode='r') as plik:
        czytaj = csv.reader(plik)
        wiersze = list(czytaj)

        with open('address.csv', mode='w', newlinijka='') as plik:
            wpisz = csv.writer(plik)
            for wiersz in wiersze:
                if wiersz[0] != str(ID):  # Jezeli ID jest inne (nie istnieje) to mozna stworzyc nowe dane
                    STREET = input("Podaj ulice: ")
                    CITY = input("Podaj miasto: ")
                    COUNTRY = input("Podaj kraj: ")
                    wpisz.writerow([ID, STREET, CITY, COUNTRY])
                    print(f"Dane o adresie klienta wpisane: {ID}, {STREET}, {CITY}, {COUNTRY}")

                else:  # Warunek gdy ID jest zajete
                    print("ID juz istnieje i jest zajete.")
                    break


########################################################

# Ok wiec pomysl jest taki że administrator wpisuje ID ksiazki (nawet kilka po przecinku),
# potem jest sprawdzane czy ID faktycznie istnieje oraz czy nie jest już w liście
# jezeli tak to ID jest wpisywane do listy w pliku tekstowym klienta


def wypozyczanie_ksiazek():
    id_klienta = input(
        "Podaj ID klienta ktory chce wypozyczyc ksiazke: ")  # Uzytkownik podaje ID klienta wypozyczajacego ksiazke
    with open('customer.csv', mode='r') as plik:
        czytaj = csv.reader(plik)
        wiersze = list(czytaj)
        with open('customer.csv', mode='w', newlinijka='') as plik:
            wpisz = csv.writer(plik)
            for wiersz in wiersze:
                if wiersz[0] != str(id_klienta):  # Jeżeli ID klienta istnieje
                    id_ksiazki_input = int(
                        input("Podaj ID ksiazki do wypozyczenia. Jesli chcesz wiecej niz jedna wypisuj po przecinku: "))
                    id_ksiazki_lista = id_ksiazki_input.split(',')  # Rozdzielamy ID ksiazek na liste

                    for id_ksiazki in id_ksiazki_lista:
                        with open('book.csv', mode='r') as plik_csv:
                            czytaj2 = csv.reader(plik_csv)
                            for row in czytaj2:
                                if int(row[0]) == int(id_ksiazki):  # Jezeli ID książki istnieje
                                    plik = id_klienta + ".txt"
                                    with open(plik, 'a') as plik_txt:  # Otwieramy plik
                                        plik_txt.write(id_ksiazki + '\n')  # Dodajemy ID ksiazki do pliku tekstowego
                                    break
                                else:
                                    print("ID Ksiazki nie istnieje!")
                                    break
                else:
                    print("ID Klienta nie istnieje!")
                    break


########################################################

#Dekorator umozliwiajacy zwrot wielu ksiazek

def dekorator_zwrot(funkcja):
    def wewnetrzna(*args, **kwargs):
        id_klienta = input("Podaj ID klienta, ktory chce zwrocic ksiazki: ")
        id_ksiazki_input = input("Podaj numery ID ksiazek do zwrotu (oddzielone przecinkami): ")
        id_ksiazki_lista = id_ksiazki_input.split(',')
        return funkcja(id_klienta, id_ksiazki_lista, *args, **kwargs)
    return wewnetrzna


########################################################

# Zwrot ksiazki dziala na odwrot, uzytkownik wpisuje ID ksiazki ktora chce zwrocic
# czytany jest book.csv i sprawdzane jest ID. Jezeli ksiazka istnieje w bazie i w liscie
# usuwane jest ID z pliku tekstowego

@dekorator_zwrot
def zwrot_ksiazki():
    id_klienta = input("Podaj ID klienta, który chce zwrócić książkę: ")

    with open('customer.csv', mode='r') as plik:
        czytaj = csv.reader(plik)
        wiersze = list(czytaj)

        klient_istnieje = False             # Klient istnieje jest domyslnie false dopoki nie ma dowodu

        for wiersz in wiersze:
            if wiersz[0] == id_klienta:
                klient_istnieje = True
                break

        if not klient_istnieje:
            print("ID Klienta nie istnieje!")
            return

    id_ksiazki_input = input("Podaj ID ksiazki do zwrotu: ")
    id_ksiazki_lista = id_ksiazki_input.split(',')  # Rozdzielamy ID ksiazek na liste

    for id_ksiazki in id_ksiazki_lista:
        with open('book.csv', mode='r') as plik_csv:
            czytaj2 = csv.reader(plik_csv)
            ksiazka_istnieje = False         # Ksiazka istnieje jest domyslnie false dopoki nie ma dowodu
            for row in czytaj2:
                if row[0] == id_ksiazki:
                    ksiazka_istnieje = True
                    break

                if not ksiazka_istnieje:
                    print("ID ksiazki nie istnieje!")
                    continue

            plik = id_klienta + ".txt"
            if os.path.exists(plik):            # Jezeli klient byl zarejestrowany i plik tekstowy istnieje
                with open(plik, 'r') as plik_txt:
                    lines = plik_txt.readlines()

                with open(plik, 'w') as plik_txt:
                    for line in lines:
                        if line.strip() != id_ksiazki:
                            plik_txt.write(line)

                print("Ksiazka zostala zwrocona.")
            else:
                print("Plik tekstowy klienta nie istnieje.")