from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/alkuluku/<number>')
def prime(number):
    number = int(number)
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                result = False
                break
        else:
            result = True
    else:
        result = False

    answer = {
        "Number": number,
        "isPrime": result
    }

    jsonvast = json.dumps(answer)
    return Response(response=jsonvast, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
