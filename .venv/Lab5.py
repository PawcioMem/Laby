################## Dokumentacja  (docstrings) ########################################
################################################################################
#
# Dla zachowania czytelności i jednolitości kodu stosuj określoną gramatykę kodu, w pythonie
# najczęściej stosuje się konwencję opisaną w dokumencie PEP 258
# Wykonaj dokumentację kodu (dla funkcji, modułu)
# Stosuj obsługę wyjątków

# #################### Przykład 1 - dokumentacja funkcji (Google style)
# def divide(x: int,y: int) -> float:
#   """
#   Funkcja dzieli liczbę x przez liczbę y

#   Args:
#     x (int): dzielna
#     y (int): dzielnik

#   Returns:
#     wynik dzielenia x/y

#   """
#   result = x/y
#   return(result)

# print(divide(2,3))
# print(divide(x = 1, y = 2))
# help(divide)
# print(divide.__doc__)
################################################################################
################################################################################
######## Function: break() and continue()
################################################################################
## Funkcja break() jest używana często do zakończenia programu/pętli (for, while)
## podczas gdy funkcja continue() pozwala opuścić blok instrukcji
## i wrócić do początku pętli.

################### Example 1: the program only prints the numbers 0 1 2 3 4
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# licz = 0
# while licz in list_1:
#     print(list_1[licz]),
#     licz += 1  # licz = licz + 1
#     if licz >= 5:
#         break

####### Example: the program prints out only odd numbers: 1 3 5 7 9
# for x in range(1, 10):
#     if x % 2 == 0:  # Sprawdź, czy x jest parzystą liczbą
#         continue
#     print(x)

################################################################################
## Function with multiple arguments: args, kwargs
################################################################################

################################## Example 1:  sum of a sequence of numbers
# def suma(*args):
#     if not args:                        # case: no input parameters
#         return('no parameters')
#     return(sum(args))
#
# print(suma(1,2,3))
# print(suma(1,2,3,4,5,6))


############# Example 2: Sum of arithmetic sequence
## functional requirements:
##  minimum number of input parameters: 1

# def suma2(x,*args):
#     sumaLiczb = x + sum(args)
#     return(sumaLiczb)
#
# print(suma2(100,1,2,3))

############  Example 3:   Sum the first four elements of arithmetic sequence
## functional requirements:
##  minimum number of input parameters: 4

# def sum2(*args):
#     if bool(args):
#         sumaLiczb = args[0] + args[1] + args[2] + args[3]
#     else:
#         sumaLiczb = 0
#
#      print(sumaLiczb)
#     return(None)
#
# sum2(1,2,3,4,5,6,7,8,9,10)
# sum2()

############  Example 3:   Sum the three elements
## functional requirements:
## minimum number of input parameters: 3
## user enter the name of input parameters

# def dict1(**kwargs):
#    for klucz, wartosc in kwargs.items():
#        print(klucz, wartosc)
#
# dict1(a=1, b=2, c=3)

############  Example 4: Say hello to a friend
## functional requirements:
## minimum number of input parameters: unknown
## name of input parameters: unknown

# def hello(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# hallo(firstname="John", secondname='Smith')
# hallo(user="John")

############  Example 5: unpack list

# list_arg = [1, 3, 5]
#
# def unpack1(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
#
# unpack1(*list_arg)
#####################################################
################################################################################
################################################################################


########################## Zadania do wykonania
# # ################################ Task 0
# '''
## Napisz funkcję, która znajdzie wszystkie liczby podzielne przez 7 a
## nie są wielokrotnością 5 w zakresie od x do y (oba uwzględnione).
## Uzyskane liczby należy wydrukować w kolejności oddzielonej przecinkami na
## pojedynczej linii. Nie zapomnij o dokumentacji funkcji
#
# '''
# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
#
# ''


# def podzielne_siedem(x,y):
#   """
#   Funkcja szuka liczb w przedziale ktore sa podzielne przez 7 ale nie sa wielokrotnoscia 5
#
#   Args:
#     x (int): poczatek przedzialu
#     y (int): koniec przedzialu
#
#   Returns:
#     Uzyskane liczby sa wypisane w kolejnosci oddzielonej przecinkami na pojedynczej linii.
#   """
#   mylist = []
#   for liczba in range(x, y + 1):
#       if liczba % 7 == 0 and liczba % 5 != 0:
#           mylist.append(liczba)
#   return ', '.join(map(str, mylist))
#
#
#
# help(podzielne_siedem)
# print(podzielne_siedem( 1000,2101))

# # ################################ Task 1
## Witryna wymaga od użytkowników wprowadzenia nazwy użytkownika i hasła w celu rejestracji.
## Utwórz funkcję sprawdzającą ważność hasła wprowadzonego przez użytkowników.
## Używanie funkcji continue() lub break().
## Poniżej znajdują się kryteria sprawdzania hasła:
## 1. Co najmniej 1 litera pomiędzy [a-z]
## 2. Co najmniej 1 liczba z zakresu [0-9]
## 3. Co najmniej 1 litera pomiędzy [A-Z]
## 4. Minimalna długość hasła transakcji: 4
## 5. Maksymalna długość hasła transakcji: 8
## Powinieneś udokumentować swój kod za pomocą dokumentacji Pythona (google)
## Zapisz wynik do pliku *.txt

# def sprawdz_haslo(username, password):
#     """
#     Funkcja sprawdza waznosc hasla wprowadzanego przez uzytkownika.
#     Ponizej znajduja sie kryteria sprawdzania hasła:
#       1. Co najmniej 1 litera pomiedzy [a-z]
#       2. Co najmniej 1 liczba z zakresu [0-9]
#       3. Co najmniej 1 litera pomiedzy [A-Z]
#       4. Minimalna dlugosc hasla transakcji: 4
#       5. Maksymalna dlugosc hasla transakcji: 8
#
#     Args:
#       username (str): pseudonim uzytkownika
#       password (str): haslo ktore podlega sprawdzeniu waznosci
#
#     Returns:
#       Wynik jest zapisywany do pliku 'sprawdz_haslo.txt'
#     """
#     if len(password) >= 4 and len(password) <= 8 and any(ilosc.islower() for ilosc in password) and any(ilosc.isupper() for ilosc in password) and any(ilosc.isdigit() for ilosc in password):
#         file = open('sprawdz_haslo.txt', 'w')
#         file.write(f"Haslo {password} uzytkownika {username} spelnia wszystkie kryteria")
#         file.close()
#     else:
#         file = open('sprawdz_haslo.txt','w')
#         file.write(f"Haslo {password} uzytkownika {username} nie spelnia wszystkich kryteriow")
#         file.close()
#
# pseudonim = input("Podaj swoj pseudonim: ")
# haslo = input("Podaj swoje haslo do sprawdzenia: ")
# sprawdz_haslo(pseudonim, haslo)


################ Task 2
## Napisz funkcję, która znajdzie wszystkie liczby podzielne przez 7 a
## nie są wielokrotnością 5 w zakresie od x do y (oba uwzględnione).
## Uzyskane liczby należy wydrukować w kolejności oddzielonej przecinkami na a
## pojedyncza linia.
## Powinieneś udokumentować swój kod, używając dokumentów Pythona
## (dokumentacja kodu styl google)
## Nie zapomnij o obsłudze wyjątków
## Zapisz wynik do pliku *.pkl, użyj pakietu pickle
# '''
# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
#

# import pickle
#
# try:
#     def podzielne_siedem(x,y):
#       """
#       Funkcja szuka liczb w przedziale ktore sa podzielne przez 7 ale nie sa wielokrotnoscia 5.
#       Teraz obsluguje rowniez wyjatki.
#
#       Args:
#         x (int): poczatek przedzialu
#         y (int): koniec przedzialu
#
#       Returns:
#         Uzyskane liczby sa wypisane w kolejnosci oddzielonej przecinkami na pojedynczej linii.
#         Wynik jest zapisywany w podzielne_siedem.txt uzywajac pakietu pickle.
#       """
#       mylist = []
#       for liczba in range(x, y + 1):
#           if liczba % 7 == 0 and liczba % 5 != 0:
#               mylist.append(liczba)
#       wynik = ', '.join(map(str, mylist))
#       filename = 'podzielne_siedem.txt'
#       file = open(filename, 'wb')
#       pickle.dump(wynik, file)
#       file.close()
#       return wynik
#
# except (ValueError, TypeError) as e:
#     print("Blad: ", e)
#
# help(podzielne_siedem)
# print(podzielne_siedem( 1000,2101))




################ Task 3
## Utwórz funkcję z wieloma argumentami (x1,x2,...,xn), która akceptuje ciąg liczb oddzielonych przecinkami z konsoli i zwraca:
## x1^x1 jeśli liczba parametrów wejściowych jest równa 1, to y = x1^x1
## x1^x1, x2^x2 jeśli liczba parametrów wejściowych jest równa 2
## x1^x1, x2^x2, x3^x3 jeśli liczba parametrów wejściowych wynosi 3
## ....
## x1^x1, ... , x99^x99 jeśli liczba parametrów wejściowych wynosi 99
## jeśli liczba parametrów wejściowych jest większa niż 100, wyświetli się komunikat o błędzie.
## Wymagania:
## Nazwa parametrów wejściowych:
## Powinieneś udokumentować swój kod za pomocą dokumentacji Pythona (google)
###############


# def potegi(*args):
#     """
#     Funkcja przyjmuje ciag liczb i zwraca potegi. Komunikat z bledem pojawia sie gdy liczba parametrow wejsciowych jest wieksza od 99.
#
#     Args:
#     *args: Argumenty.
#
#     Returns:
#     list: Lista zawierajaca potęgi.
#     """
#     if len(args) > 99:
#         print("BLAD: Liczba parametrow wejsciowych jest wieksza od 99")
#     else:
#         potegi = [x ** x for x in args]
#         return potegi
#
#
# help(potegi)
#
# print(potegi(*range(1, 100))) #drugi argument mozna ustawic na 101 zeby odpalic blad

################ Task 4
## Utwórz funkcję z wieloma argumentami (x1,x2,...,xn), która akceptuje ciąg liczb oddzielonych przecinkami z konsoli i zwraca:
## x1^x1 jeśli liczba parametrów wejściowych jest równa 1, to y = x1^x1
## x1^x1, x2^x2 jeśli liczba parametrów wejściowych jest równa 2
## x1^x1, x2^x2, x3^x3 jeśli liczba parametrów wejściowych wynosi 3
## ....
## x1^x1, ... , x99^x99 jeśli liczba parametrów wejściowych wynosi 99
## jeśli liczba parametrów wejściowych jest większa niż 100, wyświetli się komunikat o błędzie.
## Wymagania:
## Użyj: nazwa zmiennej dynamicznej (exec() lub globals() lub locals())
## Nazwa parametrów wejściowych: x1, x2, ..., xn
## Powinieneś udokumentować swój kod za pomocą dokumentacji Pythona (google)
## Nie zapomnij o obsłudze wyjątków
###############

# def potegi(*args):
#     """
#     Funkcja przyjmuje ciag liczb i zwraca potegi.
#
#     Args:
#     *args: Argumenty.
#
#     Returns:
#     list: Lista zawierajaca potęgi.
#
#     Raises:
#     ValueError: Komunikat z bledem pojawia sie gdy liczba parametrow wejsciowych jest wieksza od 99.
#     """
#
#     if len(args) > 99:
#         raise ValueError("Liczba parametrów wejściowych nie może być większa niż 99")
#
#     for i, arg in enumerate(args, start=1):
#         globals()[f'x{i}'] = arg
#
#     potegi = [eval(f'x{i}') ** eval(f'x{i}') for i in range(1, len(args) + 1)]
#     return potegi
#
#
# help(potegi)
#
# try:
#     wyniki = potegi(*range(1, 100)) #drugi argument mozna ustawic na 101 zeby odpalic blad
#     print(wyniki)
# except ValueError as blad:
#     print(f"Powod bledu: {blad}")


########################## Task 5 ########################
## Pierwszy krok,
## generuj dane testowe: utwórz folder. Utwórz 5 plików tekstowych w tym folderze,
## każdy plik zawiera więcej niż 5 zdań.
## Nazwy plików: Text1ID_ABC, Text2ID_405.txt, Text3ID_607.txt, Text4ID_ABC5.txt, Text5ID_DEF.txt
##
## Utwórz funkcję z wieloma argumentami, która:
## a) wydrukuj cały plik z folderu
## b) jeśli nazwa pliku zawiera 'ABC', policz, ile słów znajduje się w tekście pliku
## które zawierają słowa zawierające więcej niż 3 litery
## Następny krok: udekoruj tę funkcję, dodaj następującą funkcjonalność:
## a) funkcja sprawdzi, ile plików ma w nazwie 0
## b) jeśli plik ma w nazwie 0, to funkcja zlicza słowa w tekście pliku
## c) jeśli nazwa pliku zawiera 'EF.txt', to funkcja kopiuje ten plik do
## Katalog „DocumentLab5copy”.
#
# import os
#
# # os.makedirs('.\DocumentLab5')
# # os.makedirs('.\DocumentLab5copy')
# os.chdir("DocumentLab5")
#
# file1 = open('Text1ID_ABC.txt', 'w', encoding='utf-8')
# file1.write('Kot biegnie przez ogrod. Słonce swieci na niebie. Dzieci bawia się na placu zabaw. Ptaki spiewaja w lesie. Samochod przemierza ulice. Motyl usiadl na kwiatku.')
# file1.close()
#
# file2 = open('Text2ID_405.txt', 'w', encoding='utf-8')
# file2.write('Pies biegnie przez park. Slonce swieci na niebie. Dzieci graja w pilke. Ptaki spiewaja w lesie. Samochod przemierza ulice. Kot spi na kanapie.')
# file2.close()
#
# file3 = open('Text3ID_607.txt', 'w', encoding='utf-8')
# file3.write('Slonce zachodzi za gorami. Deszcz pada na dach. Dzieci bawia sie na placu zabaw. Motyl fruwa wokol kwiatow. Wiatr szumi w koronach drzew. Ptak siada na galezi.')
# file3.close()
#
# file4 = open('Text4ID_ABC5.txt', 'w', encoding='utf-8')
# file4.write('Ksiezyc swieci na nocnym niebie. Dzieci tancza na podworku. Liscie opadaja z drzew. Ptaki zbieraja sie na drzewach. Samolot leci wysoko w chmurach. Woda plynie w rzece.')
# file4.close()
#
# file5 = open('Text5ID_DEF.txt', 'w', encoding='utf-8')
# file5.write('Ryby plywaja w stawie. Slimak przesuwa się po galezi. Koniczyna rosnie na polu. Zolw sunie powoli po trawie. Ludzie rozmawiaja na lawce. Kwiaty kwitna w ogrodzie.')
# file5.close()
#
#
# ##DEKORATOR
# def dekorator(funkcja):
#     def wrapper():
#         #(a)
#         plik_zero = sum(1 for plik in os.listdir() if '0' in plik)
#         print(f"Liczba plikow zawierajacych '0' w nazwie: {plik_zero}")
#
#         #(b)
#         lista_plikow = os.listdir()
#         for plik in lista_plikow:
#             if '0' in plik:
#                 with open(plik, 'r', encoding='utf-8') as file:
#                     zawartosc = file.read()
#                     wszystkie_slowa = zawartosc.split()
#                     dek_litery = sum(1 for slowo in wszystkie_slowa)
#                     print(f"Liczba slow w pliku {plik}: {dek_litery}")
#
#             #(c)
#             if 'EF.txt' in plik:
#                 oryginal = open(plik, 'r', encoding='utf-8')
#                 os.chdir('..\DocumentLab5copy')
#                 kopia = open(plik, 'w', encoding='utf-8')
#
#                 kopia.write(oryginal.read())
#
#                 oryginal.close()
#                 kopia.close()
#     funkcja()
#     return wrapper
#
# ## FUNKCJA
# @dekorator
# def pliki():
#     #(a)
#     print(os.listdir())
#     #(b)
#     lista_plikow = os.listdir()
#     for plik in lista_plikow:
#         if 'ABC' in plik:
#             with open(plik, 'r', encoding='utf-8') as file:
#                 zawartosc = file.read()
#                 wszystkie_slowa = zawartosc.split()
#                 trzy_litery = sum(1 for slowo in wszystkie_slowa if len(slowo) > 3)
#                 print(f"Liczba slow zawierajacych wiecej niz 3 litery w pliku {plik}: {trzy_litery}")
#
# pliki()
