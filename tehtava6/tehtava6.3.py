def muunnos(bensa):
    gs = bensa * 3.785
    return gs

bensa = float(input("Syötä gallonamäärä: "))
while bensa>-1:
    tulos = muunnos(bensa)
    print(str(tulos) + " litraa")
    bensa = float(input("Syötä gallonamäärä: "))