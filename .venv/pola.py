import pole_trojkata, pole_prostokata
import globals
def pola(wybor):

    if wybor == 1:   #Prostokat
        wartosc_a = int(input('Podaj wartosc boku a: '))
        wartosc_b = int(input('Podaj wartosc boku b: '))
        return pole_prostokata.pole_prostokata(wartosc_a, wartosc_b)

    elif wybor == 2:  #Trojkat
        wartosc_a = int(input('Podaj wartosc boku a: '))
        wartosc_h = int(input('Podaj wartosc wysokosci trojkata: '))
        return pole_trojkata.pole_trojkata(wartosc_a,wartosc_h)

    elif wybor == 3:    #kwadrat
        wartosc_a = int(input('Podaj wartosc boku a: '))
        return pole_prostokata.pole_prostokata(wartosc_a)

    else:
        print("ERROR Nieodpowiedni numer wyboru")