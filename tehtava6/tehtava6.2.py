import random
def noppa(tahko):
    tulos = random.randint(1,tahko)
    return tulos

tahko = int(input("Syötä nopan tahkojen yhteismäärä: "))
tulos = 0
while tahko!=tulos:
    tulos = noppa(tahko)
    print(tulos)