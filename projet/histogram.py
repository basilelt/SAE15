import matplotlib.pyplot as plt
import os

def run_hist(lst):
    print(lst)
    path = os.path.join(__file__.replace("histogram.py", ""), "plot", "fig.svg")

    plt.bar(range(1, len(lst) + 1), lst)
    plt.xlabel("Numéro de la boule")
    plt.ylabel("Fréquence")
    plt.title("Nombre de boule par numéro")
    plt.show()
    plt.savefig(path, format = "svg")

    print("\nNous observons que lorsque le nombre de tirages est élevé les nombres de boules tirées par valeur sont à peu près égaux")
  