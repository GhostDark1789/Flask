import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/navidad")
def navidad():
    now = datetime.datetime.now()
    dia = now.month == 12 and now.day == 24
    return render_template("condition.html", dia=dia)

@app.route("/año_nuevo")
def new_year():
    now = datetime.datetime.now()
    dia = now.month == 1 and now.day == 1
    return render_template("condition.html", dia=dia)

@app.route("/hoy")
def hoy():
    now = datetime.datetime.now()
    dia = now.month == now.month and now.day == now.day
    return render_template("condition.html", dia=dia)
