from functions import facto

def esperance(lst, p):
    e = 0
    
    for i in range(len(lst)):
        e += p * lst[i] # Somme des p_i * x_i

    return e

def run_stats(lst):
    p = 1 / 45
    e = (45 + 1) / 2
    c = 1 / (facto(45) / (facto(5) * facto(45 - 5)))
    
    esp = esperance(lst, p)

    print("La probabilité d'un évenement aléatoire parmis 45, provenants d'une loi uniforme discrète, est 1 / 45 = ",
        "{:.3f}".format(round(p, 3)), "\n",
        "L'espérance de cette variable aléatoire est donc (45 + 1) / 2 = ",
        "{:.3f}".format(round(e, 3)), "\n",
        f"La probabilité d'avoir une combinaison spécifique (peut importe l'ordre) est : 1 / 45_C_5 = ",
        "{:.9f}".format(round(c, 9)), "\n",
        "L'espérance de notre set de tirage est = ", "{:.3f}".format(round(esp, 3)))
