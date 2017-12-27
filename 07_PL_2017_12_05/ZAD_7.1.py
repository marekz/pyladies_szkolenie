# Napisz program, który po wejściu na adres: /add/<liczba1>/<liczba2> odpowie sumą podanych liczb.
# Przykład: wejście na /add/3/5 powinno zwrócić "8".

from flask import Flask

app = Flask(__name__);

@app.route("/add/<liczba1>/<liczba2>")
def test(liczba1, liczba2):

    l1 = int(liczba1)
    l2 = int(liczba2)

    suma = str(l1 + l2)

    return suma

app.run(debug=True)