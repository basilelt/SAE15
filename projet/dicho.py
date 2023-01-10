from functions import test_bool, test_45int
import pandas

def dicho(tirage_drop, tirage, value):
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

def dicho_rec(value, t):
    n = len(t)
    if n == 1:
        if t[0] == value:
            return True
        
        else:
            return False
    
    m = n // 2
    if t[m] == value:
        return True
    
    elif t[m] > value:
        return dicho_rec(value, t[:m])
        
    else:
        return dicho_rec(value, t[m:])

def run_dicho(tirage):
    value = test_45int(input("Quel nombre voulez-vous rechercher dans le(s) tirage(s) ? (entre 1 et 45) : "))
    rec = test_bool(input("Quel algorithme voulez-vous utiliser pour cette recherche ? (0 : itératif, 1 : récursif) : "))
    tirage_drop = pandas.DataFrame()

    if rec:
        for i in range(tirage.shape[1]):
            test = False
            j = 0
            t = tirage.iloc[:, i].tolist()

            test = dicho_rec(value, t)
            
            if test:
                tirage_drop.insert(j, tirage.columns[i], tirage.iloc[:, i])
                j += 1
        
    
    else:
        tirage_drop = dicho(tirage_drop, tirage, value)
    
    return tirage_drop