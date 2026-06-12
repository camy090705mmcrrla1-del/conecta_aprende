from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)


cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["conecta_aprende"]

usuarios = db["usuarios"]
encuestas = db["encuestas"]

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro', methods=['POST'])
def registro():

    usuario = request.form['usuario']
    contraseña = request.form['contraseña']

    usuarios.insert_one({
        "usuario": usuario,
        "contraseña": contraseña
    })

    return redirect('/login')

@app.route('/validar', methods=['POST'])
def validar():

    usuario = request.form['usuario']
    contraseña = request.form['contraseña']

    existe = usuarios.find_one({
        "usuario": usuario,
        "contraseña": contraseña
    })

    if existe:
        return redirect('/menu')

    return "Usuario o contraseña incorrectos"

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/modulo1')
def modulo1():
    return render_template('modulo1.html')

@app.route('/modulo2')
def modulo2():
    return render_template('modulo2.html')

@app.route('/modulo3')
def modulo3():
    return render_template('modulo3.html')

@app.route('/modulo4')
def modulo4():
    return render_template('modulo4.html')

@app.route('/modulo5')
def modulo5():
    return render_template('modulo5.html')


if __name__ == '__main__':
    app.run(debug=True)


