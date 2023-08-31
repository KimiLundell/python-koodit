luku = str(input("Anna luku. Syötä tyhjä merkkijono lopettaaksesi."))
isoin = 0
pienin = luku
while luku!=" ":
    luku = int(luku)
    if luku>isoin:
        isoin = luku
    elif luku<pienin:
        pienin = luku
    luku = str(input("Anna luku. Syötä tyhjä merkkijono lopettaaksesi."))
print("Luvuista suurin on " + str(isoin))
print("Luvuista pienin on " + str(pienin))
