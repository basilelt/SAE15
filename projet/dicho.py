from functions import test_bool, test_45int
import pandas

def dicho(tirage, value):
    tirage_drop = pandas.DataFrame()
    for i in range(tirage.shape[1]):
        test = False
        j = 0
        t = tirage.iloc[:, i].tolist()
        
        a = 0
        b = len(t)
        
        while True:
            m = (a + b) // 2
        
            if a == m:
                test = t[a] == value
                break
            
            if t[m] > value:
                b = m
            else:
                a = m
        
        if test:
            tirage_drop.insert(j, tirage.columns[i], tirage.iloc[:, i])
            j += 1
    
    return tirage_drop

def dicho_rec(value, t, a, b):
    if a == b : 
        return a
    if b == - 1 : 
        b = len(t) - 1
    m = (a + b) // 2
    if t[m] == value :
        return m
    elif t[m] > value :
        return dicho_rec(value, t, a, m-1)
    else :
        return dicho_rec(value, t, m+1, b)
    
    return tirage

def run_dicho(tirage):
    value = test_45int(input("Quel nombre voulez-vous rechercher dans le(s) tirage(s) ? (entre 1 et 45) : "))
    rec = test_bool(input("Quel algorithme voulez-vous utiliser pour cette recherche ? (0 : itératif, 1 : récursif) : "))
    
    if rec:
        tirage_drop = pandas.DataFrame()
        for i in range(tirage.shape[1]):
            test = False
            j = 0
            t = tirage.iloc[:, i].tolist()

            test = dicho_rec(value, t, 0, -1)
            
            if test:
                tirage_drop.insert(j, tirage.columns[i], tirage.iloc[:, i])
                j += 1
        
    
    else:
        tirage = dicho(tirage, value)
    
    return print(f"Les tirages comportant le nombre {value} sont :\n",
                tirage)