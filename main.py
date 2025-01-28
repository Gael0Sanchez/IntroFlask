from flask import Flask

app = Flask(__name__)  

@app.route('/')
def index():
    return "Hola mundo!!"

@app.route("/hola")
def hola():
    return "Hola!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Número: {}".format(n)

@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre: {user} id: {id}!!!"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es {}!!!".format(n1 + n2)

if _name_ == "_main_":
    app.run(debug=True)