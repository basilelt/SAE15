import numpy
import pandas
import multiprocessing
from functions import test_bool, test_int

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

        for i in range(x):
           tirage.loc[i] = [f"Tirage {i + 1}"] + rng.choice(nombre, size = 5, replace = False).tolist() ## Distribution uniforme discrète utilisant une même seed connue

    else:
        rng = numpy.random.default_rng()
        for i in range(x):
            tirage.loc[i] = [f"Tirage {i + 1}"] + rng.choice(nombre, size = 5, replace = False).tolist() ## Distribution uniforme discrète utilisant une seed aléatoire
                
    return tirage

def run_loto(nombre):
    rejouer = True

    while rejouer:
        tirage = pandas.DataFrame(columns = ['Tirage', 'boule', 'boule', 'boule', 'boule','boule'])
        loto(tirage, nombre)

        print("\nVoici le(s) tirage(s) non-trié(s) : \n", tirage)
        
        rejouer = test_bool(input("\nVoulez-vous rejouer ? (0 : non, 1 : oui) : "))

    return tirage
