from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "segredo123"

cardapio = [
    {"id": 1, "nome": "Hambúrguer", "preco": 18.00},
    {"id": 2, "nome": "Pizza", "preco": 35.00},
    {"id": 3, "nome": "Batata Frita", "preco": 12.00},
    {"id": 4, "nome": "Refrigerante", "preco": 6.00},
    {"id": 5, "nome": "Sorvete", "preco": 8.00}
]

@app.route('/')
def inicio():
    if 'favoritos' not in session:
        session['favoritos'] = []

    return render_template(
        'index.html',
        cardapio=cardapio,
        favoritos=session['favoritos']
    )

@app.route('/favoritar/<int:id>')
def favoritar(id):
    favoritos = session.get('favoritos', [])

    for produto in cardapio:
        if produto['id'] == id:
            if produto['nome'] not in favoritos:
                favoritos.append(produto['nome'])

    session['favoritos'] = favoritos
    return redirect(url_for('inicio'))

@app.route('/remover/<nome>')
def remover(nome):
    favoritos = session.get('favoritos', [])

    if nome in favoritos:
        favoritos.remove(nome)

    session['favoritos'] = favoritos
    return redirect(url_for('inicio'))

@app.route('/zerar')
def zerar():
    session['favoritos'] = []
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)