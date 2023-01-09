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

def test_45int(to_int):
    while True:
        test = True
        try:
            to_int = int(to_int)
        except ValueError:
            to_int = input("Désolé la valeur saisie n'est pas un nombre, réessayez : ")
            test = False
        
        if test:
            if to_int < 1 or to_int > 45:
                to_int = input("Désolé la valeur saisie n'est pas un nombre tirable dans un loto (1-45) : ")
            else:
                to_int = int(to_int)
                return to_int

def facto(n):
    if n < 2:
        return 1
    
    return n * facto(n - 1)

def list_loto():
    return numpy.array(list(i for i in range(1, 46)))

def test_trichoix(tri):
    while True:
        test = True
        try:
            tri = int(tri)
        except ValueError:
            tri = input("Désolé la valeur saisie n'est pas un nombre, réessayez : ")
            test = False
            
        if test:
            if tri == 1 or tri == 2 or tri == 3:
                return tri
            
            else:
                tri = input("Veuillez entrer une valeur étant 1, 2 ou 3, réessayez :")