from flask import Flask, render_template

app = Flask(__name__)

@app.route('/filme/<genero>')
def filme(genero):

    if genero == "acao":
        dados = {
            "titulo": "Filmes de Ação",
            "imagem": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba",
            "descricao": "Esse não está disponível no sistema."
        }

    elif genero == "comedia":
        dados = {
            "titulo": "Filmes de Comédia",
            "imagem": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c",
            "descricao": "Esse não está disponível no sistema."
        }

    elif genero == "terror":
        dados = {
            "titulo": "Filmes de Terror",
            "imagem": "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb",
            "descricao": "Esse não está disponível no sistema."
        }

    else:
        dados = {
            "titulo": "Gênero não encontrado",
            "imagem": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1",
            "descricao": "Esse gênero não está disponível no sistema."
        }

    return render_template("filme.html", dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
    
# pip install flask e python app.py pra rodar o servidor.