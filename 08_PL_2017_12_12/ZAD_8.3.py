from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def show_name():
    return render_template(
        'yourname.html',
        naglowek='Twoje imię',
        yourName=request.args.get('name', ''),
        link=True
    )

app.run(debug=True)