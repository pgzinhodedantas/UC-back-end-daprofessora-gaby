from flask import Flask, render_template

app = Flask(__name__)

# Produtos do cardápio.
produtos = {
    "combo-frango": {
        "nome": "Combo Franguinho Crocante",
        "preco": "R$ 32,90",
        "descricao": "Sanduíche de frango crocante, batata pequena e um refri bem gelado.",
        "imagem": "combo.jpg",
        "destaque": "Boa pedida para quem quer almoçar sem gastar muito."
    },
    "esfiha": {
        "nome": "Esfiha da Hora",
        "preco": "R$ 11,90",
        "descricao": "Esfiha aberta com carne temperada, queijo derretido e cheirinho verde.",
        "imagem": "esfiha.jpg",
        "destaque": "Sai bastante no fim da tarde, principalmente com suco."
    },
    "pastel": {
        "nome": "Pastel de Feira",
        "preco": "R$ 14,50",
        "descricao": "Pastel grande, frito na hora e bem recheado, daquele jeito de feira mesmo.",
        "imagem": "pastel.jpg",
        "destaque": "Crocante por fora e com bastante recheio por dentro."
    },
    "suco": {
        "nome": "Suco Natural Gelado",
        "preco": "R$ 8,90",
        "descricao": "Suco natural feito com fruta de verdade. Simples, gelado e refrescante.",
        "imagem": "suco.jpg",
        "destaque": "Combina com qualquer lanche do cardápio."
    },
    "brownie": {
        "nome": "Brownie Caseiro",
        "preco": "R$ 10,00",
        "descricao": "Brownie macio por dentro, com casquinha por fora e sabor bem chocolatudo.",
        "imagem": "brownie.jpg",
        "destaque": "Para fechar o pedido com sobremesa."
    }
}

# Pedidos fictícios 
pedidos = [
    {"cliente": "Rafaela", "pedido": "Combo Franguinho Crocante", "valor": "R$ 32,90", "status": "Preparando"},
    {"cliente": "João", "pedido": "Pastel de Feira", "valor": "R$ 14,50", "status": "Saiu para entrega"},
    {"cliente": "Bianca", "pedido": "Esfiha da Hora", "valor": "R$ 11,90", "status": "Pedido recebido"},
    {"cliente": "Caio", "pedido": "Suco Natural Gelado", "valor": "R$ 8,90", "status": "Finalizado"},
    {"cliente": "Nina", "pedido": "Brownie Caseiro", "valor": "R$ 10,00", "status": "Separando"},
]


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html", produtos=produtos)


@app.route("/produto/<codigo>")
def produto(codigo):
    item = produtos.get(codigo.lower())
    return render_template("produto.html", codigo=codigo, item=item)


@app.route("/pedidos")
def lista_pedidos():
    return render_template("pedidos.html", pedidos=pedidos)


@app.route("/cliente/<nome>/<bairro>")
def cliente(nome, bairro):
    bairros_atendidos = ["centro", "alecrim", "ponta-negra", "tirol"]
    atende_bairro = bairro.lower() in bairros_atendidos

    return render_template(
        "cliente.html",
        nome=nome,
        bairro=bairro,
        atende_bairro=atende_bairro
    )


@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)