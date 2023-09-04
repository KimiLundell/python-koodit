luku = input("Syötä luku. Paina Enter lopettaaksesi: ")
luvut = []

while luku!=(""):
    luvut.append(int(luku))
    luku = input("Syötä luku. Paina Enter lopettaaksesi: ")
luvut.sort(reverse=True)
print(luvut[0:5])