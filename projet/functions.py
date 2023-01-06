import numpy

def test_bool(to_bool):
    while True:
        test = True
        try:
            to_bool = int(to_bool)
        except ValueError:
            to_bool = input("Désolé la valeur saisie n'est pas un nombre, réessayez : ")
            test = False
            
        if test:
            if to_bool == 0 or to_bool == 1:
                bool(to_bool)
                return to_bool
            
            else:
                to_bool = input("Veuillez entrer une valeur étant 0 ou 1, réessayez :")

def test_int(to_int):
    while True:
        try:
            to_int = int(to_int)
            return to_int
        except ValueError:
            to_int = input("Désolé la valeur saisie n'est pas un nombre, réessayez : ")

def facto(n):
    if n <= 1:
        return 1
    
    return n * facto(n - 1)

def list_loto():
    return numpy.array(list(i for i in range(1, 46)))