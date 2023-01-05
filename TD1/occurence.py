import random
import numpy

tab = []
count = []

for i in range(random.randint(10, 20)):
    tab.append(random.randint(0, 10))
    count.append(0)

for i in range(len(tab)):
    for j in tab:
        if tab[i] == j:
            count[i] += 1

array = numpy.array((tab,count))

print(array)
