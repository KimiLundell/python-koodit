def paritonlista(lista):
    paritonlista = []
    for s in lista:
        if s % 2 !=0:
            paritonlista.append(s)
    tulos = paritonlista
    return tulos

lista = []
for s in range(5):
    luku = int(input("Syötä kokonaisluku: "))
    lista.append(luku)
tulos = paritonlista(lista)
print(lista)
print(tulos)
