from loto import run_loto
from stats import run_stats
from functions import list_loto, test_trichoix, test_bool
from cocktail import run_cocktail
from insertion import run_insertion
from fusion import run_fusion
from dicho import run_dicho

lst = list_loto()

tirage = run_loto(lst)

print()
run_stats(lst)

print("\nVoici le(s) tirage(s) non-trié(s) : \n", tirage)

tri_choix = test_trichoix(input("Quel tri voulez-vous utiliser ? (cocktail : 1, insertion : 2, fusion : 3) : "))
if tri_choix == 1:
    tirage = run_cocktail(tirage)

elif tri_choix == 2:
    tirage = run_insertion(tirage)

else:
    tirage = run_fusion(tirage)

print("\nVoici le(s) tirage(s) trié(s) : \n", tirage)

search = test_bool(input("\nVoulez-vous chercher si une valeur présente dans le(s) tirage(s) ? (0 : non, 1 : oui) : "))
if search:
    tirage_search = run_dicho(tirage)
