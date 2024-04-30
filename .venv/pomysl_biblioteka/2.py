from datetime import date
import csv
import random

def dodaj_ksiazke(ID, AUTHOR, TITLE, PAGES, CREATED, UPDATED):
    with open('book.csv', mode='a', newline='') as plik:
        writer = csv.writer(plik)
        writer.writerow([ID, AUTHOR, TITLE, PAGES, CREATED, UPDATED])
        print("Książka została dodana")

def usun_ksiazke_po_id(ID):
    with open('book.csv', mode='r') as plik:
        reader = csv.reader(plik)
        wiersze = list(reader)

    with open('book.csv', mode='w', newline='') as plik:
        writer = csv.writer(plik)
        for wiersz in wiersze:
            if wiersz[0] != str(ID):
                writer.writerow(wiersz)
        print("Książka została usunięta")

def usun_ksiazke_po_tytule(tytul):
    with open('book.csv', mode='r') as plik:
        reader = csv.reader(plik)
        wiersze = list(reader)

    with open('book.csv', mode='w', newline='') as plik:
        writer = csv.writer(plik)
        for wiersz in wiersze:
            if wiersz[2] != tytul:
                writer.writerow(wiersz)
        print("Książka została usunięta")

def dodaj_ksiazke_input():
    ID = random.randint(1, 999)
    AUTHOR = input("Podaj autora książki: ")
    TITLE = input("Podaj tytuł książki: ")
    PAGES = int(input("Podaj liczbę stron: "))
    CREATED = int(input("Podaj rok powstania: "))
    UPDATED = date.today()
    dodaj_ksiazke(ID, AUTHOR, TITLE, PAGES, CREATED, UPDATED)

def usun_ksiazke_input_id():
    ID = int(input("Podaj ID książki do usunięcia: "))
    usun_ksiazke_po_id(ID)

def usun_ksiazke_input_tytul():
    tytul = input("Podaj tytuł książki do usunięcia: ")
    usun_ksiazke_po_tytule(tytul)

while True:
    print("\nMenu:")
    print("1. Dodaj książkę")
    print("2. Usuń książkę względem ID")
    print("3. Usuń książkę względem tytułu")
    print("4. Wyjście")

    wybor = input("Wybierz opcję: ")

    if wybor == '1':
        dodaj_ksiazke_input()
    elif wybor == '2':
        usun_ksiazke_input_id()
    elif wybor == '3':
        usun_ksiazke_input_tytul()
    elif wybor == '4':
        break
    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")