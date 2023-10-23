class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matka=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdytä(self, muutos):
        raja = self.huippunopeus
        self.nopeus = self.nopeus + muutos
        if self.nopeus > raja:
            self.nopeus = raja
        elif self.nopeus < 0:
            self.nopeus = 0
        return

auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.kiihdytä(-200)
print(auto.rekkari, str(auto.huippunopeus) + " km/h " + str(auto.nopeus) + " km/h " + str(auto.matka))