from flask import Flask, render_template

app = Flask(__name__)

@app.route("/zespoly")
def lista_zespolow():
    return render_template(
        'zespoly.html',
        naglowek='Zespoły',
        zespoly=['Pink Floyd', 'Queen', 'Led Zeppelin'],
        link=True
    )

app.run(debug=True)