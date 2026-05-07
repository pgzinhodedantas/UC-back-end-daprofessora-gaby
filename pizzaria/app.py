from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pizzaria/<sabor>')
def pizzaria(sabor):

    pizzas = {
        "calabresa": {
            "nome": "Pizza de Calabresa",
            "imagem": "imagens/calabresa.jpg"
        },

        "margherita": {
            "nome": "Pizza de Margherita",
            "imagem": "imagens/margherita.jpg"
        },

        "frango": {
            "nome": "Pizza de Frango",
            "imagem": "imagens/frango.jpg"
        }
    }

    if sabor in pizzas:
        return render_template(
            'pizza.html',
            nome=pizzas[sabor]["nome"],
            imagem=pizzas[sabor]["imagem"]
        )

    return render_template('erro.html')

if __name__ == '__main__':
    app.run(debug=True)
# rota vai ser /pizzaria/calabresa, /pizzaria/margherita ou /pizzaria/frango para mostrar a pizza correspondente. Se o sabor não for encontrado, será exibida uma página de erro.
