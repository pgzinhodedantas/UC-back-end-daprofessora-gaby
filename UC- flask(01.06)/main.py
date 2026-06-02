from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
     
     mensagem = ""
     
     if request.method == 'POST':
         nome = request.form.get('nome')
         if not nome:
             mensagem = "O campo nome é obrigatório."
         else:
             mensagem = f"cadastro de {nome} realizado com sucesso!"
             
     return render_template('cadastro.html', mensagem=mensagem)
      
@app.route('/')
def formulario():
    return render_template('cadastro.html')
      
@app.route('/validacao', methods=['POST'])
def cadastro():
    
    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    cidade = request.form.get('cidade', '').strip().title()

    return f"""
    nome: {nome}<br>
    email: {email}<br>
    cidade: {cidade}
    """
    
if __name__ == '__main__':
    app.run(debug=True)