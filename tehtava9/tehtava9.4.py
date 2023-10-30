import random
class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matka=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdytä(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
        return
    def kulje(self, aika):
        self.aika = aika
        self.matka = self.matka + (self.nopeus * self.aika)
        return
lista = []
for i in range(10):
    rekkari = "ABC-" + str(i)
    huippunopeus = random.randint(100,200)
    auto = Auto(rekkari, huippunopeus)
    lista.append(auto)

jatka = True
while jatka:
    for auto in lista:
        if auto.matka > 10000:
            jatka = False
        auto.kiihdytä(random.randint(-10,15))
        auto.kulje(1)

for auto in lista:
    print(f"Rekisterinumero = {auto.rekkari}, huippunopeus = {auto.huippunopeus:d} km/h, tämänhetkinen nopeus ="
          f" {auto.nopeus:d} km/h, kuljettu matka = {auto.matka} km.")
