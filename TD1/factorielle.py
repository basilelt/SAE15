n = int(input("Entrez un entier : "))
fact = 1

for i in range(n):
    fact = fact * (i + 1)

print(f"La factorielle de {n} est {fact}.")