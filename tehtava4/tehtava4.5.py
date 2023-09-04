tunnus1 = input("Kerro käyttäjätunnus: ")
sana1 = input("Kerro salasana: ")
tunnus = "python"
sana = "rules"
kerrat = 1
while tunnus1!=tunnus or sana1!=sana:
    kerrat = kerrat + 1
    tunnus1 = input("Kerro käyttäjätunnus: ")
    sana1 = input("Kerro salasana: ")
    if kerrat==5:
        print("Pääsy evätty")
        break
else:
    print("Tervetuloa")