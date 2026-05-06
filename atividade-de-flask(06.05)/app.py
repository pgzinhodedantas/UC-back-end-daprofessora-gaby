from flask import Flask, render_template

app = Flask(__name__)


@app.route('/ola/<nome>')
def ola(maria):
    return "Olá, " + maria


@app.route('/ola/<nome>')
def ola(nome):
    return render_template("ola.html", nome=nome)


@app.route('/calculo/<int:n1>/<int:n2>')
def calculo(n1, n2):
    return str(n1 + n2)


@app.route('/idade/<nome>/<int:idade>')
def idade(joão, idade):
    if idade >= 18:
        return joão + " maior"

    else:
        return joão + " menor"



@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return nome + " custa " + str(preco)


@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    return (palavra + "") * vezes


app.run(debug=True)