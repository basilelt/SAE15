import os
import pandas
import path as p

def run_save_b(tirage, test):
    name = input("Quel nom voulez-vous donner à votre fichier ? : ")
    path = os.path.join(p.__file__.replace("/path.py", ""), "save")

    files = os.listdir(path)
    for i in range(len(files)):
        if name in files[i]:
            name = input("Ce nom est déjà utilisé, réessayer : ")
            i = 0
    
    if test:
        path = os.path.join(path, name + "_sorted.pkl")
        tirage.to_pickle(path)
        return
    else:
        path = os.path.join(path, name + "_unsorted.pkl")
        tirage.to_pickle(path)
        return

def run_read_b():
    path = os.path.join(p.__file__.replace("/path.py", ""), "save")
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
