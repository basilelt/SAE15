import numpy
import pandas

def loto():
    tirage = pandas.DataFrame()
    
    while True:
        x = input("Combien de tirage voulez-vous effectuer ? : ")
        try:
            x = int(x)
            break
        except ValueError:
            print("Désolé la valeur saisie n'est pas un nombre.")


    while True:
        choix = input("Voulez-vous utiliser une seed identique pour ceux-ci ? (0 : non, 1 : oui) : ")
        test = True
        try:
            choix = int(choix)
        except ValueError:
            print("Désolé la valeur saisie n'est pas un nombre.")
            test = False
            
            if test:
                if choix == {0, 1}:
                    bool(choix)
                    break
            
                else:
                    print("Veuillez entrer une valeur étant 0 ou 1 !")
    
    if choix:
        graine = int(input("Veuillez indiquer votre seed : "))
        numpy.random.seed(graine) ##Utilise une seed pour la génération des nombres aléatoire avec numpy
        for i in range (x - 1):
            print(i)
            tirage[f"Tirage {x + 1}"] = numpy.random.randint(1, 45 + 1, 5) ##Distribution uniforme discrète

    else:
        for i in range (x):
           tirage[f"Tirage {x + 1}"] = numpy.random.randint(1, 45 + 1, 5) ##Distribution uniforme discrète
    
    return print(tirage)

rejouer = True

while rejouer:
    loto()
    
    while True:
        rejouer = input("Voulez-vous rejouer ? (0 : non, 1 : oui) : ")
        test = True
        try:
            rejouer = int(rejouer)
        except ValueError:
            print("Désolé la valeur saisie n'est pas un nombre.")
            test = False
        
        if test:
            if rejouer == {0, 1}:
                bool(rejouer)
                break
        
            else:
                print("Veuillez entrer une valeur étant 0 ou 1 !")
