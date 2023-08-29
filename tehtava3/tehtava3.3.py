suku = str(input("Mikä on biologinen sukupuolesi?"))
hemo = int(input("Mikä on hemoglobiiniarvosi (g/l)?"))

if suku=="Nainen" or "nainen":
    if hemo>175:
        print("Hemoglobiiniarvosi on korkea.")
    elif hemo>=117:
        print("Hemoglobiiniarvosi on normaali")
    elif hemo<117:
        print("Hemoglobiiniarvosi on alhainen")

elif suku=="Mies" or "mies":
    if hemo>195:
        print("Hemoglobiiniarvosi on korkea.")
    elif hemo>=134:
        print("Hemoglobiiniarvosi on normaali")
    elif hemo<134:
        print("Hemoglobiiniarvosi on alhainen")