n = int(input("Entrez un entier : "))
n_init = n

def facto(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * facto(n - 1)

fact = facto(n)

print(f"La factorielle de {n_init} est {fact}.")