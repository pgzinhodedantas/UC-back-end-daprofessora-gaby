from flask import Flask, render_template

app = Flask(__name__)

@app.route("/usuario")
def usuario():
    usuario ={
        'nome': 'paulo',
        'sobrenome': 'guilherme'
    }
    return render_template('contato.html', title = 'pagina inicial', usuario=usuario)

@app.route('/')
@app.route('/contato')
def contato():
   return render_template('contato.html', usuario=None, nome=None, title='Home')

@app.route('/semestre/<int:x>')
def semestre(x):
    return f'Você está no semestre' + str(x)

@app.route('/pagamento/<float:valor>')
def pagamento(valor):
    return 'voce pagou:' + str(valor)

@app.route('/somar', defaults={'n1': "0", "n2": "0"})
@app.route('/somar/<int:n1>/<int:n2>')
def somar(n1, n2):
    resultado = n1 + n2
    return str(resultado)  


@app.route('/soma', defaults={'n1': "0", "n2": "0"})
@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    resultado = n1 + n2
    return render_template('soma.html', n1=n1, n2=n2, resultado=resultado)


@app.route('arearestrita/,int:id>')
def arearestrita(id):
    if id == 1:
        return ' Acesso bloqueado'
    else:
        return ' Acesso liberado'
    
    
@app.route("/")
def contato():
    nome = "paulo"
    return render_template('contato.html', title = 'pagina inicial', nome=nome)

@app.route("/home")
def home():
    return render_template('contato.html')


@app.route('/dados', defaults={'nome': 'visitante'})
@app.route('/dados/<nome>')
def dadosc(nome):
    return f'olá, {nome}!'

if __name__ == "__main__":
    app.run(debug=True)

