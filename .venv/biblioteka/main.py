## zaladowanie biblioteka
## wywolanie funkcji z modulow book.py, client.py
## TUTAJ JUZ MOZNA INPUT itd

def __main__():
    import book
    import client
    import os
    os.chdir("Library")


    print(" \n \n===============================================")
    print("BIBLIOTEKA")
    print("Prosze wybrac opcje: \n\nBOOK\n(1) Dodaj ksiazke \n(2) Usun ksiazke (ID lub TYTUL) \n")
    print("KLIENT\n(3) Dodaj lub usun klienta \n(4) Dodaj adres klienta \n(5) Zapisz ksiazki w pliku klienta ktore wypozyczyl")
    print("(6) Usun ksiazki z pliku klienta ktore zostaly zwrocone \n")
    print("(7) Wylacz program")
    print("=============================================== \n")

    #############################
    print("=====================")
    wybor = int(input("Wybor: "))
    print("=====================")

    while wybor != 7:
        if wybor == 1:  ##book.dodaj_ksiazke
            ID = int(input("Podaj ID ksiazki: "))
            AUTHOR = input("Podaj autora: ")
            TITLE = input("Podaj tytul: ")
            PAGES = int(input("Podaj liczbe stron: "))
            book.dodaj_ksiazke(ID, AUTHOR, TITLE, PAGES)

        elif wybor == 2:  ##book.usun_ksiazke
            jak_usun = input("Jak chcesz usunac ksiazke? Wpisz (ID) lub (TYTUL): ")
            id_lub_tytul = input("Podaj wartosc wczesniej wybranej opcji: ")
            book.usun_ksiazke(jak_usun, id_lub_tytul)

        elif wybor == 3:  ##client.dodaj_usun_klienta
            wybor_klient = int(input("(1) Dodaj nowego klienta lub (2) usun dane klienta z bazy: "))
            if wybor_klient == 1:
                NAME = input("Podaj imie i nazwisko nowego klienta: ")
                EMAIL = input("Podaj email nowego klienta: ")
                PHONE = input("Podaj numer telefonu nowego klienta: ")
                client.dodaj_usun_klienta("1", None, None, NAME, EMAIL, PHONE)
            elif wybor_klient == 2:
                jak_usun = input("Jak chcesz usunac dane klienta? Wpisz (ID) lub (NAME): ")
                if jak_usun == "ID":
                    ID_do_usuniecia = int(input("Podaj ID klienta do usuniecia: "))
                    client.dodaj_usun_klienta("2", "ID", ID_do_usuniecia, None, None, None)
                elif jak_usun == "NAME":
                    NAME = input("Podaj imie i nazwisko klienta do usuniecia: ")
                    client.dodaj_usun_klienta("2", "NAME", None, NAME, None, None)
                else:
                    raise ValueError("Sposob usuniecia nie istnieje lub jest podany blednie!")

        elif wybor == 4:  ##client.dodaj_address_klient
            ID = input("Podaj ID Klienta: ")
            STREET = input("Podaj ulice: ")
            CITY = input("Podaj miasto: ")
            COUNTRY = input("Podaj kraj: ")
            client.dodaj_address_klient(ID, STREET, CITY, COUNTRY)

        elif wybor == 5:  ##client.wypozyczanie_ksiazek
            id_klienta = input("Podaj ID klienta ktory chce wypozyczyc ksiazke: ")
            id_ksiazki_input = input(
                "Podaj ID ksiazki do wypozyczenia. Jesli chcesz wiecej niz jedna wypisuj po przecinku: ")
            client.wypozyczanie_ksiazek(id_klienta, id_ksiazki_input)

        elif wybor == 6:  ##client.zwrot_ksiazki
            id_klienta = input("Podaj ID klienta, który chce zwrocic ksiazke: ")
            id_ksiazki_input = input(
                "Podaj ID ksiazki do zwrotu [DEKORATOR: NUMERY ID KILKU KSIAZEK (oddzielone przecinkami)]: ")
            client.zwrot_ksiazki(id_klienta, id_ksiazki_input)

        else:
            print("Niepoprawny wybor.")

        print("=====================")
        wybor = int(input("Wybor: "))
        print("=====================")

    print("EXIT")

###########################
__main__()