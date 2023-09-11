nimi = input("Syötä nimi. Paina Enter lopettaaksesi: ")
nimet = set()
while nimi != "":
    if nimi not in nimet:
        print("Uusi nimi")
        nimet.add(nimi)
    else:
        print("Aiemmin syötetty nimi")
    nimi = input("Syötä nimi. Paina Enter lopettaaksesi: ")
for s in nimet:
    print(s)
