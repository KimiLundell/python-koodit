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
        self.matka = self.nopeus * self.aika
        return
lista = []
for i in range(10):


#print(f"Rekisterinumero = {auto.rekkari}, huippunopeus = {auto.huippunopeus:d} km/h, tämänhetkinen nopeus ="
      #f" {auto.nopeus:d} km/h, kuljettu matka = {auto.matka} km.")