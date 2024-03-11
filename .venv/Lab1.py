## 1. Sprawdź wynik działań
# 0 > 1 [FALSE]
# 0 <= 1 [TRUE]
# 0 >= 1 [FALSE]
# 1 == 0 [FALSE]
# 1 == 1 [TRUE]
# 1 != 0 [TRUE]
# 1 != 1 [FALSE]


## 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)
#
# x = int(input('Podaj x: '))
# y = int(input('Podaj y: '))
# wynik = 2 * x + 5 * y
# print(wynik)

## 3. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
##  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)
#
# a = input('Podaj imię: ')
# b = input('Podaj nazwisko: ')
# c = int(input('Podaj swoj wiek: '))
# d = input('Podaj kierunek studiów: ')
#
# print("Jestem {} {} mam {} lat studiuję {}".format(a, b, c, d))
#
# ## 4. Sprawdź/porównaj czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646
#
# a = 1 + 2 + 10 + 20000001 + 4 + 347586970885
# b = 321784560456434534646
# print(a == b)[FALSE]
#
# ## 5. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat
#
# a = int(input('Podaj a: '))
# b = int(input('Podaj b: '))
# suma = a + b
# print(suma)
#
# if suma % 2 == 0:
#     print('Suma liczb jest parzysta!')
#
# if suma % 2 != 0:
#     print('Suma liczb jest nieparzysta!')
#
#
# ## 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
# ## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.
#
# def potega(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a * potega(a, b - 1)
#
#
# x = int(input('Podaj x: '))
# y = int(input('Podaj y: '))
#
# wybor = int(input('Wybierz opcję: (1 = SUMA) (2 = RÓŻNICA) (3 = ILOCZYN) (4 = ILORAZ) (5 = POTĘGA LICZB): '))
#
# if wybor == 1:
#     print(x + y)
#
# elif wybor == 2:
#     print(x - y)
#
# elif wybor == 3:
#     print(x * y)
#
# elif wybor == 4:
#     if y != 0:
#         print(x / y)
#     else:
#         print('Nie ma dzielenia przez 0')
#
# elif wybor == 5:
#     print({potega(x, y)})
#
# else:
#     print('Nie ma takiej opcji!')
#
# ## 7. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (x != 5 or x < 0)
#
# x = int(input('Podaj x: '))
# a = (x > 1 and x < 13)
# b = (x != 5 or x < 0)
#
# print(a)
# print(b)
#
# ZADANIA
# DODATKOWE !!!!
#
# # 1. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania: "Czy zdrowo się odżywiasz?",
# # , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.
#
# print('ANKIETA')
# print('DANE OSOBOWE')
# imie = input('Podaj swoje imię: ')
# nazwisko = input('Podaj swoje nazwisko: ')
# wiek = int(input('Podaj swój wiek: '))
# print('PYTANIA')
# zdrowo = input('Czy zdrowo się odżywiasz? ODP: ')
# sport = input('Czy lubisz sport? ODP: ')
# zwierze = input('Czy masz jakieś zwierzę domowe? ODP: ')
# samochod = input('Jakiej marki jest twój samochód? ODP: ')
# tajwan = input('Czy według ciebie Tajwan to kraj czy część Chin? ODP: ')
# print('')
# print('')
# print('PODSUMOWANIE')
# print('Czy zdrowo się odżywiasz? TWOJA ODP: {}'.format(zdrowo))
# print('Czy lubisz sport? TWOJA ODP: {}'.format(sport))
# print('Czy masz jakieś zwierzę domowe? TWOJA ODP: {}'.format(zwierze))
# print('Jakiej marki jest twój samochód? TWOJA ODP: {}'.format(samochod))
# print('Czy według ciebie Tajwan to kraj czy część Chin? TWOJA ODP: {}'.format(tajwan))
# print('')
# print('Dziękujemy za udział w ankiecie, {} {}, {}.'.format(imie, nazwisko, wiek))

