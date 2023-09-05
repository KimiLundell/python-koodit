def muunnos(maara):
    gs = maara * 3.785
    return gs

maara = float(input("Syötä gallonamäärä: "))
while maara>-1:
    tulos = muunnos(maara)
    print(str(tulos) + " litraa")
    maara = float(input("Syötä gallonamäärä: "))