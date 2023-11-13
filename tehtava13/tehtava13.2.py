from flask import Flask, Response
import json
import mysql.connector


def sqlyhteys(psw):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password=psw,
        autocommit=True
    )
    return yhteys


yhteys = sqlyhteys("Servermaster20!")
kursori = yhteys.cursor()

app = Flask(__name__)


@app.route('/kenttä/<koodi>')
def kenttä(koodi):
    sql = "SELECT name FROM airport WHERE ident ='"+koodi+"'"
    kursori.execute(sql)
    airport = kursori.fetchall()[0][0]
    sql = "SELECT municipality FROM airport WHERE ident ='"+koodi+"'"
    kursori.execute(sql)
    city = kursori.fetchall()[0][0]
    answer = {
        "ICAO": koodi,
        "Name": airport,
        "Municipality": city
    }

    jsonvast = json.dumps(answer)
    return Response(response=jsonvast, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
