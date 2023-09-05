import random
def noppa():
    tulos = random.randint(1,6)
    return tulos

tulos = 0
while tulos!=6:
    tulos = noppa()
    print(tulos)