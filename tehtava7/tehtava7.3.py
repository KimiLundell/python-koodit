vastaus = input("Haluatko syöttää uuden lentoaseman(syöttö) vai hakea jo syötetyn lentoaseman nimen(haku)?"
                " Paina Enter lopettaaksesi: ")
lista = {}
while vastaus != "":
    if vastaus == "syöttö":
        koodi = input("Syötä uusi lentoaseman ICAO-koodi: ")
        nimi = input("Syötä uusi lentoaseman nimi: ")
        lista[koodi] = nimi
    elif vastaus == "haku":
        koodi = input("Syötä ICAO-koodi: ")
        if koodi in lista:
            print(lista[koodi])
    vastaus = input("Haluatko syöttää uuden lentoaseman(syöttö) vai hakea jo syötetyn lentoaseman nimen(haku)?"
                    " Paina Enter lopettaaksesi: ")
