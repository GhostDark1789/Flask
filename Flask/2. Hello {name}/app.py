from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Stranger"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize() #Función para devolver la cadena de texto con mayúscula inicial.
    return f"Hello, {name}"
