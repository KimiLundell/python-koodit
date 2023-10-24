class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros
    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        print("Olet kerroksessa: " + str(self.kerros))
        return
    def kerros_alas(self):
        self.kerros = self.kerros - 1
        print("Olet kerroksessa: " + str(self.kerros))
        return
    def siirry_kerrokseen(self, kohde):
        self.kohde = kohde
        while self.kohde > self.kerros:
            self.kerros_ylös()
        while self.kohde < self.kerros:
            self.kerros_alas()
        return

h = Hissi(1,10)
syöte = input("Mihin kerrokseen haluat mennä? Paina enter lopettaaksesi: ")
while syöte !="":
    syöte = int(syöte)
    h.siirry_kerrokseen(syöte)
    syöte = input("Mihin kerrokseen haluat mennä? Paina enter lopettaaksesi: ")
