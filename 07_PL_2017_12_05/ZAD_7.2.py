# Napisz program, który po wejściu na adres /current-status
# metodą POST ustawi aktualny status na podstawie przekazanego w zapytaniu JSON-a
# (np. {"status": "starting"}), a po wejściu na ten sam adres metodą GET zwróci aktualny status.

from flask import Flask, request

app = Flask(__name__)

@app.route("/current-status", methods=["POST", "GET", "PUT"])
def save():
    global status
    if request.method == "GET":
        status = "starting"

    if request.method == "POST":
        status = "Patataj"

    else:
        data = request.get_json()
        status = data["status"]
        # return "Saved status: {}".format(status)
        status = 'Blabla'

    return status

# @app.route("/read", methods=["GET"])
# def read():
#     return saved

app.run(debug=True)