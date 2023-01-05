import random

sort = []

for i in range(random.randint(10, 20)):
    sort.append(random.randint(0, 100))
print(sort)

for i in range(len(sort) - 1, 1, -1):
    sorted = True
    for j in range(i):
        if sort[j + 1] < sort[j]:
            (sort[j + 1], sort[j]) = (sort[j], sort[j + 1])
            sorted = False
    if sorted:
        break

print(sort)