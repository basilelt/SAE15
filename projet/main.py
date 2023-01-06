from loto import run_loto
from stats import run_stats
from functions import list_loto

lst = list_loto()

tirage = run_loto(lst)
#print(tirage)

run_stats(lst)
