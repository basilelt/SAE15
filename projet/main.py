def facto(n):
    if n <= 1:
        return 1
    
    return n * facto(n - 1)

print("La probabilité d'un évenement aléatoire parmis 45, provenants d'une loi uniforme discrète, est 1 / 45 = ", "{:.3f}".format(round(1 / 45, 3)), "\n",
    "L'espérance de cette variable aléatoire est donc (45 + 1) / 2 = ", "{:.3f}".format(round((45 + 1) / 2, 3)), "\n",
    f"La probabilité d'avoir une combinaison spécifique (peut importe l'ordre) est : 1 / 45C5 = ", "{:.9f}".format(round(1 / (facto(45) / (facto(5) * facto(45 - 5))), 9)))

import loto

tirage = loto.run_loto()
print(tirage)