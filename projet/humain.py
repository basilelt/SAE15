import os
import pandas
from functions import test_bool

def run_save_h(tirage, test):
    
    choice = test_bool(input("Quel type de fichier voulez-vous utiliser ? (0 : csv, 1 : stata) : "))
    
    if choice:
        name = input("Quel nom voulez-vous donner à votre fichier ? : ")
        path = os.path.join(__file__.replace("humain.py", ""), "save")

        if test:
            name = name + "_sorted.dta"
            
        else:
            name = name + "_unsorted.dta"

        files = os.listdir(path)
        for i in range(len(files)):
            if name in files[i]:
                name = input("Ce nom est déjà utilisé, réessayer : ")
                
                if test:
                    name = name + "_sorted.dta"
                        
                else:
                    name = name + "_unsorted.dta"

                i = 0

        path = os.path.join(path, name)
        tirage.to_stata(path, write_index = False)

    else:
        name = input("Quel nom voulez-vous donner à votre fichier ? : ")
        path = os.path.join(__file__.replace("humain.py", ""), "save")

        if test:
            name = name + "_sorted.csv"
            
        else:
            name = name + "_unsorted.csv"

        files = os.listdir(path)
        for i in range(len(files)):
            if name in files[i]:
                name = input("Ce nom est déjà utilisé, réessayer : ")
                
                if test:
                    name = name + "_sorted.csv"
                        
                else:
                    name = name + "_unsorted.csv"

                i = 0

        path = os.path.join(path, name)
        tirage.to_csv(path, index = False)

def run_read_h():
    path = os.path.join(__file__.replace("humain.py", ""), "save")
    print("Voici les fichiers disponibles : \n", os.listdir(path))
    
    choice = test_bool(input("Quel type de fichier voulez-vous utiliser ? (0 : csv, 1 : stata) : "))
    test = True

    if choice:
        while test == True:
            name = input("Quel fichier voulez-vous ouvrir ? : ")
            name = os.path.join(path, name)
            
            if ".dta" in name:
                test = not os.path.exists(name)
                if test:
                    print("Ce fichier n'existe pas !\n")

            else:
                test = True
                print("Ce fichier n'est pas un dta !\n")

        tirage = pandas.read_stata(name)
        return tirage

    else:
        while test == True:
            name = input("Quel fichier voulez-vous ouvrir ? : ")
            name = os.path.join(path, name)
            
            if ".csv" in name:
                test = not os.path.exists(name)
                if test:
                    print("Ce fichier n'existe pas !\n")

            else:
                test = True
                print("Ce fichier n'est pas un csv !\n")

        tirage = pandas.read_csv(name, sep = ",", delimiter = None)
        return tirage
