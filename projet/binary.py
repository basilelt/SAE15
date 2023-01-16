import os
import pandas

def run_save_b(tirage, test):
    name = input("Quel nom voulez-vous donner à votre fichier ? : ")
    path = os.path.join(__file__.replace("binary.py", ""), "save")

    if test:
        name = name + "_sorted.pkl"
        
    else:
        name = name + "_unsorted.pkl"

    files = os.listdir(path)
    for i in range(len(files)):
        if name in files[i]:
            name = input("Ce nom est déjà utilisé, réessayer : ")
            i = 0

    path = os.path.join(path, name)
    tirage.to_csv(path)

def run_read_b():
    path = os.path.join(__file__.replace("binary.py", ""), "save")
    print("Voici les fichiers disponibles : \n", os.listdir(path))

    test = True
    while test == True:
        name = input("Quel fichier voulez-vous ouvrir ? : ")
        name = os.path.join(path, name)
        
        if ".csv" in name:
            test = True
            print("Ce fichier est un fichier pickle et non un csv !\n")
        else:
            test = not os.path.exists(name)
            if test:
                print("Ce fichier n'existe pas !\n")

    tirage = pandas.read_pickle(name)

    return tirage
