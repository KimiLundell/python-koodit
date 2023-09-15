import mysql.connector

def haku(koodi):
    sql = "select name, municipality from airport"
    sql += " where ident='" + koodi + "'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(rivi)
    return
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="Servermaster20!",
    autocommit=True
    )

koodi = input("Syötä lentoaseman ICAO-koodi: ")
haku(koodi)
