import globals

def pole_prostokata(a, *args):
    if len(args) == 0:
        poleP = a * a
        print(f'Pole kwadratu wynosi: {poleP}')
    else:
        poleP = a * args[0]
        print(f'Pole prostokąta wynosi: {poleP}')