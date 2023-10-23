class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matka=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka


auto = Auto("ABC-123", 142)
print(auto.rekkari, str(auto.huippunopeus) + " km/h " + str(auto.nopeus), str(auto.matka))