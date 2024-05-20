#Importowanie wymaganych bibliotek
from datetime import date
import os
import csv




'''
NAME
    book

DESCRIPTION
    This module allows the user to add book data saved in
    book.csv as well as delete book data by ID or TITLE.

    This script requires 'biblioteka' that should be installed within the Python
    environment you are running this script in.
    
FUNCTIONS
    This module contains the following functions:
    
    *dodaj_ksiazke() - This function allows the user to add
    a new book to the book.csv file. If the book ID
    already exists the book is not added to the database.
    
    *usun_ksiazke() - This function allows the user to
    delete a book from the book.csv file, either
    by ID or TITLE. If the ID or TITLE matches the user input,
    the entire row is deleted.
'''

########################################################

# Wpisanie informacji o ksiazce
def dodaj_ksiazke(ID, AUTHOR, TITLE, PAGES):
    """

    :param ID: ID ksiazki.
    :param AUTHOR: Nazwa autora.
    :param TITLE: Tytul ksiazki.
    :param PAGES: Ilosc stron ksiazki.
    """
    CREATED = date.today()
    UPDATED = date.today()

    # Sprawdzenie czy ID ksiazki juz istnieje w bazie
    with open('book.csv', mode='r', newline='') as plik:
        czytnik = csv.reader(plik)
        next(czytnik)
        for row in czytnik:
            if len(row) > 0 and int(row[0]) == ID:  # Jezeli tak, wypisuje komunikat i nie zapisuje ksiazki
                print("Takie ID juz istnieje")
                break
        else:  # Jezeli nie, ksiazka zostaje wpisana do pliku
            with open('book.csv', mode='a', newline='') as plik:
                wpisz = csv.writer(plik)
                wpisz.writerow([ID, AUTHOR, TITLE, PAGES, CREATED, UPDATED])
                print(f"Ksiazka wpisana: {ID}, {AUTHOR}, {TITLE}, {PAGES}, {CREATED}, {UPDATED}")

########################################################

# Usuwanie ksiazki
def usun_ksiazke(jak_usun, id_lub_tytul):
    """

    :param jak_usun: Sposob usuniecia ksiazki. Wybor miedzy string "ID" lub "TITLE"
    :param id_lub_tytul: Wartosc id lub tytulu ksiazki zaleznie od wybranego sposobu usuniecia ksiazki.
    """
    if jak_usun == "ID":
        ID = int(id_lub_tytul)   # Użytkownik podaje ID książki do usunięcia
        with open('book.csv', mode='r') as plik:
            czytaj = csv.reader(plik)
            wiersze = list(czytaj)

        usunieto = False  # Domyslnie ustawione na false

        with open('book.csv', mode='w', newline='') as plik:
            wpisz = csv.writer(plik)
            for wiersz in wiersze:
                if wiersz[0] != str(ID):  # Jeżeli ID istnieje, ksiazka zostaje usunieta
                    wpisz.writerow(wiersz)
                else:
                    usunieto = True  # Ksiazka zostala usunieta

        if usunieto:
            print("Książka została usunięta")

        else:
            print("Ksiazka nie istnieje")


    elif jak_usun == "TITLE":
        tytul = id_lub_tytul  # Uzytkownik podaje tytul ksiazki do usuniecia
        with open('book.csv', mode='r') as plik:
            czytaj = csv.reader(plik)
            wiersze = list(czytaj)

        usunieto = False  # Domyslnie ustawione na false

        with open('book.csv', mode='w', newline='') as plik:
            wpisz = csv.writer(plik)
            for wiersz in wiersze:
                if wiersz[2] != tytul:  # Jezeli tytul istnieje ksiazka zostaje usunieta i podany jest komunikat
                    wpisz.writerow(wiersz)
                else:
                    usunieto = True  # Usuniecie ksiazki

        if usunieto:
            print("Ksiazka zostala usunieta")
        else:
            print("Ksiazka nie istnieje")

    else:  # Wyjatek do sposobu usuniecia
        raise ValueError("Sposob usuniecia nie istnieje lub jest podany blednie!")
