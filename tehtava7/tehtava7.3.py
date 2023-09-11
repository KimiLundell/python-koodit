vastaus = input("Haluatko syöttää uuden lentoaseman(s) vai hakea jo syötetyn lentoaseman nimen(h)?"
                " Paina Enter lopettaaksesi: ")
lista = {}
while vastaus != "":
    if vastaus == "s":
        koodi = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lista[koodi] = nimi
    elif vastaus == "h":
        koodi = input("Syötä ICAO-koodi: ")
        if koodi in lista:
            print(lista[koodi])
    vastaus = input("Haluatko syöttää uuden lentoaseman(s) vai hakea jo syötetyn lentoaseman nimen(h)?"
                    " Paina Enter lopettaaksesi: ")
