import matplotlib.pyplot as plt
import os

def run_hist(lst):
    path = os.path.join(__file__.replace("histogram.py", ""), "plot", "fig.svg")

    plt.hist(lst)
    plt.show()
    plt.savefig(path, format = "svg")

    print("Nous observons que lorsque le nombre de tirages est élevé les nombres de boules tirées par valeur sont à peu près égaux")
