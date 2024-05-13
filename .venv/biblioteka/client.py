# Importowanie wymaganych bibliotek
from datetime import date
import os
import csv
import random


'''
NAME
    client

DESCRIPTION
    This module allows the user to create customer data saved in 
    address.csv and customer.csv as well as delete customer data by ID or NAME.
    The user can also save book ID's which have been borrowed by a client,
    and they can also be returned. "Book borrow" data is saved in the
    client's ID.txt.

    This script requires 'biblioteka' that should be installed within the Python
    environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    
    * dodaj_usun_klienta() - The user is given the choice to:
    (1) Add a new client to the database:
    This part of the function allows the user to register
    a customer in customer.csv. After the registration, 
    the program checks if the ID of the user already exists, 
    and if it does the process is stopped. 
    Otherwise it adds the customer's
    data to the customer.csv file. It also creates a .txt
    file that belongs to the customer's ID.
    OR
    (2) Remove a client from the database:
    This part of the function allows the user to delete
    customer data. The user needs to specify if they want to delete
    information based on the customer's ID or NAME. If the ID or
    NAME matches the user input, the entire row is deleted.

    * dodaj_address_klient - This function allows the user to 
    add address data related to an existing customer.

    * wypozyczanie_ksiazek - This function allows the user to
    specify which books a customer has borrowed. This is saved
    in the customer's ID.txt file. More books can be borrowed at
    the same time if they are seperated by "," during input.
    
    * zwrot_ksiazki - This function allows the user to specify
    specify which books a customer has returned. If the ID
    of the book matches the user input, then that row
    containing the book's ID is removed from the
    customer's ID.txt file.
'''



########################################################

# Rejestracja nowego klienta lub usuwanie danych klienta z bazy
def dodaj_usun_klienta(wybor_klient, jak_usun, ID_do_usuniecia, NAME, EMAIL, PHONE):
    # Rejestracja nowego klienta
    if wybor_klient == "1":
        ID = str(random.randint(1000, 9999))
        CREATED = date.today()
        UPDATED = date.today()

        # Sprawdzenie czy ID klienta juz istnieje w bazie
        with open('customer.csv', mode='r') as plik:
            czytaj2 = csv.reader(plik)
            next(czytaj2)
            for row in czytaj2:
                if int(row[0]) == ID:  # Jezeli tak, wypisuje komunikat i nie zapisuje klienta
                    print("Takie ID klienta juz istnieje")
                    break
            else:  # Jezeli nie, klient zostaje zapisany do bazy i robiony jest plik .txt
                with open('customer.csv', mode='a', newline='') as plik:
                    wpisz = csv.writer(plik)
                    wpisz.writerow([ID, NAME, EMAIL, PHONE, CREATED, UPDATED])
                    print(f"Klient zapisany: {ID}, {NAME}, {EMAIL}, {PHONE}, {CREATED}, {UPDATED}")
                    # Plik ID.txt
                    nowy_plik = str(ID) + ".txt"
                    file = open(nowy_plik, 'w')
                    file.close()

    # Usuniecie danych klienta
    elif wybor_klient == "2":

        ######
        if jak_usun == "ID":  # Sposob usuniecia danych klienta wzgledem ID
            with open('customer.csv', mode='r') as plik:
                czytaj = csv.reader(plik)
                wiersze = list(czytaj)

                usunieto = False  # Domyslnie ustawione na false

                with open('customer.csv', mode='w', newline='') as plik:
                    wpisz = csv.writer(plik)
                    for wiersz in wiersze:
                        if wiersz[0] != str(ID_do_usuniecia):  # Jezeli ID istnieje klient zostaje usuniety i podany jest komunikat
                            wpisz.writerow(wiersz)
                        else:
                            usunieto = True

                if usunieto:
                    print("Klient zostal usuniety")
                    os.remove(str(ID_do_usuniecia) + ".txt") # Usuwanie pliku zwiazanego z klientem

                else:
                    print("Klient nie istnieje")

        #####
        elif jak_usun == "NAME":  # Sposob usuniecia danych klienta wzgledem NAME
            with open('customer.csv', mode='r') as plik:
                czytaj = csv.reader(plik)
                wiersze = list(czytaj)

                usunieto = False  # Domyslnie ustawione na false

                with open('customer.csv', mode='w', newline='') as plik:
                    wpisz = csv.writer(plik)
                    for wiersz in wiersze:
                        if wiersz[1] != str(NAME):  # Jezeli NAME sie zgadza klient jest usuniety i podany jest komunikat
                            wpisz.writerow(wiersz)
                        else:
                            usunieto = True

                    if usunieto:
                        print("Klient zostal usuniety")
                        os.remove(str(ID_do_usuniecia) + ".txt")  # Usuwanie pliku zwiazanego z klientem

                    else:
                        print("Klient nie istnieje")

        else:  # Wyjatek do sposobu usuniecia
            raise ValueError("Sposob usuniecia nie istnieje lub jest podany blednie!")

    else:  # Wyjatek do numeru wyboru miedzy utworzeniem a usunieciem klienta
        raise ValueError("Niepoprawny numer wyboru!")


########################################################

# Dodawanie danych address klienta
def dodaj_address_klient(ID, STREET, CITY, COUNTRY):
    nowy_wiersz = [str(ID), STREET, CITY, COUNTRY]  #Dane sa tymczasowo zapisywane tutaj
    dane_nowe = []
    czy_id_istnieje = False         # Domyslnie false

    with open('address.csv', mode='r') as plik:
        czytaj = csv.reader(plik)
        wiersze = list(czytaj)

        for wiersz in wiersze:
            if wiersz[0] == str(ID):    # Jezeli ID istnieje to nie mozna nadpisac istniejacego
                czy_id_istnieje = True
                print("ID już istnieje i jest zajete.")
                break

        if not czy_id_istnieje:     # Jezeli ID jest inne (nie istnieje) to mozna stworzyc nowe dane
            dane_nowe = wiersze + [nowy_wiersz]

    with open('address.csv', mode='w', newline='') as plik:
        wpisz = csv.writer(plik)
        wpisz.writerows(dane_nowe)

        if not czy_id_istnieje:
            print(f"Dane o adresie klienta wpisane: {ID}, {STREET}, {CITY}, {COUNTRY}")


########################################################

# Ok wiec pomysl jest taki że administrator wpisuje ID ksiazki (nawet kilka po przecinku),
# potem jest sprawdzane czy ID faktycznie istnieje oraz czy nie jest już w liście
# jezeli tak to ID jest wpisywane do listy w pliku tekstowym klienta


def wypozyczanie_ksiazek(id_klienta, id_ksiazki_input):
    klient_istnieje = False  # Domyslnie false

    with open('customer.csv', mode='r') as plik:
        czytaj = csv.reader(plik)
        wiersze = list(czytaj)
        for wiersz in wiersze:
            if wiersz[0] == str(id_klienta):  # Sprawdzamy czy ID klienta istnieje
                klient_istnieje = True
                break  # Jeżeli klient istnieje, przerywamy pętlę

    if not klient_istnieje:  # Jezeli klient nie istnieje, zglaszamy blad
        raise ValueError("ID Klienta nie istnieje!")

    id_ksiazki_lista = id_ksiazki_input.split(',')  # Rozdzielamy ID książek na listę

    for id_ksiazki in id_ksiazki_lista:
        with open('book.csv', mode='r') as plik_csv:
            czytaj2 = csv.reader(plik_csv)
            next(czytaj2)
            for row in czytaj2:
                if int(row[0]) == int(id_ksiazki):  # Sprawdzamy czy ID ksiazki istnieje
                    plik = str(id_klienta) + ".txt"
                    with open(plik, 'a') as plik_txt:  # Otwieramy plik
                        plik_txt.write(id_ksiazki + '\n')  # Dodajemy ID książki do pliku tekstowego
                    print("Ksiazka zostala wypozyczona")
                    break
            else:
                print("Ksiazka nie istnieje")

########################################################

#Dekorator umozliwiajacy zwrot wielu ksiazek

def dekorator_zwrot(funkcja):
    def wewnetrzna(id_klienta, id_ksiazki_input, *args, **kwargs):
        id_ksiazki_lista = id_ksiazki_input.split(',')
        return funkcja(id_klienta, id_ksiazki_lista, *args, **kwargs)
    return wewnetrzna


########################################################

# Zwrot ksiazki dziala na odwrot, uzytkownik wpisuje ID ksiazki ktora chce zwrocic
# czytany jest book.csv i sprawdzane jest ID. Jezeli ksiazka istnieje w bazie i w liscie
# usuwane jest ID z pliku tekstowego

@dekorator_zwrot
def zwrot_ksiazki(id_klienta, id_ksiazki_input):

    with open('customer.csv', mode='r') as plik:
        czytaj = csv.reader(plik)
        wiersze = list(czytaj)

        klient_istnieje = False             # Klient istnieje jest domyslnie false dopoki nie ma dowodu

        for wiersz in wiersze:
            if wiersz[0] == id_klienta:
                klient_istnieje = True
                break

        if not klient_istnieje:
            raise ValueError("ID Klienta nie istnieje!")

    id_ksiazki_lista = id_ksiazki_input  # Rozdzielamy ID ksiazek na liste

    for id_ksiazki in id_ksiazki_lista:
        with open('book.csv', mode='r') as plik_csv:
            czytaj2 = csv.reader(plik_csv)
            ksiazka_istnieje = False         # Ksiazka istnieje jest domyslnie false dopoki nie ma dowodu
            for row in czytaj2:
                if row[0] == id_ksiazki:
                    ksiazka_istnieje = True
                    break

                if not ksiazka_istnieje:
                    continue

            plik = str(id_klienta) + ".txt"
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

            if not ksiazka_istnieje:  # Jezeli ksiazka nie istnieje po sprawdzeniu, wyswietlany jest komunikat
                print("Ksiazka nie istnieje")