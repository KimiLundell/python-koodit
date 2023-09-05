def summa(lista):
    tulos = sum(lista)
    return tulos

lista = []
for s in range(5):
    luku = int(input("Syötä kokonaisluku: "))
    lista.append(luku)
tulos = summa(lista)
print("Listassa olevien lukujen summa on " + str(tulos))