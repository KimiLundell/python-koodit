import random
luku = int(input("Syötä arpakuutioiden lukumäärä: "))
arvat = []

for s in range(luku):
    luku = random.randint(1,6)
    arvat.append(luku)
summa = sum(arvat)
print(summa)