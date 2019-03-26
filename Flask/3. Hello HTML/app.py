from flask import Flask, render_template #importaamos la lbreria de renderizar un modelo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:name>")
def headline(name):
    name = name.capitalize()
    return render_template("headline.html", name=name) #renderizamos nuestro archivo "index.html" de nuestra carpeta "templates"
