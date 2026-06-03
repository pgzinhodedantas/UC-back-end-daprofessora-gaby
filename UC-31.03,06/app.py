from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    nome = request.form['nome'].strip().title()
    email = request.form['email'].strip().lower()
    telefone = request.form['telefone'].replace('(','').replace(')','').replace(' ','').replace('-','')
    cpf = request.form['cpf'].replace('.','').replace('-','')
    cidade = request.form['cidade'].strip()
    estado = request.form['estado'].strip().upper()
    curso = request.form['curso'].strip()
    idade = request.form['idade']
    senha = request.form['senha']
    
    erros = []
    
    if len(nome) < 8: erros.append("Nome invalido")
    if '@' not in email or '.com' not in email: erros.append("Email invalido")
    if not telefone.isdigit() or len(telefone) != 11: erros.append("Telefone invalido")
    if not cpf.isdigit() or len(cpf) != 11: erros.append("CPF invalido")
    if len(cidade) < 3: erros.append("Cidade invalida")
    if len(estado) != 2: erros.append("Estado invalido")
    if curso == "": erros.append("Selecione um curso")
    if int(idade) < 16: erros.append("Idade minima 16 anos")
    if len(senha) < 8 or senha.isalpha() or senha.isdigit(): erros.append("Senha fraca")
    
    if erros:
        return render_template('index.html', erros=erros)
    
    return render_template('index.html', sucesso=True, nome=nome, email=email, telefone=telefone, cpf=cpf, cidade=cidade, estado=estado, curso=curso, idade=idade)

if __name__ == '__main__':
    app.run(debug=True)