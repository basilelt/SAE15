import numpy
import pandas

def loto(tirage, nombre): 
    x = test_int(input("Combien de tirage voulez-vous effectuer ? : "))

    choix = test_bool(input("Voulez-vous utiliser une seed identique pour ceux-ci ? (0 : non, 1 : oui) : "))
    
    if choix:
        if test_bool(input("Voulez-vous la saisir vous même ? (0 : non, 1 : oui) : ")):
            graine = test_int(input("Veuillez indiquer votre seed : ")) ## Demande une seed pour la génération des nombres aléatoire avec numpy
        
        else:
            graine = numpy.random.randint(100) ## La seed est définie aléatoirement
            print(f"La seed est : {graine}")
        
        rng = numpy.random.default_rng(graine)

        for i in range (x):
            tirage[f"Tirage {i + 1}"] = rng.choice(nombre, size = 5, replace = False) ## Distribution uniforme discrète utilisant une même seed connue

    else:
        rng = numpy.random.default_rng()
        for i in range (x):
            tirage[f"Tirage {i + 1}"] = rng.choice(nombre, size = 5, replace = False) ## Distribution uniforme discrète utilisant une seed aléatoire
    
    return tirage

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

def run_loto():
    return(tirage)

rejouer = True
nombre = numpy.array(list(i for i in range(1, 46)))

while rejouer:
    tirage = pandas.DataFrame()
    loto(tirage, nombre)
    
    rejouer = test_bool(input("Voulez-vous rejouer ? (0 : non, 1 : oui) : "))
