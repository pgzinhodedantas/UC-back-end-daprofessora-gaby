from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    message_type = None
    if request.method == 'POST':
        nickname = request.form.get('nickname', '').strip()
        game = request.form.get('game', '').strip()
        email = request.form.get('email', '').strip()
        rules = request.form.get('rules')

        if not nickname or len(nickname) < 4 or not game or not email or not rules:
            message = "Preencha todos os campos obrigatórios."
            message_type = "error"
        else:
            message = "Inscrição realizada com sucesso!"
            message_type = "success"

    return render_template('form.html', message=message, message_type=message_type)

if __name__ == '__main__':
    app.run(debug=True)
    
        # Regras de validação:
        # - todos os campos obrigatórios
        # - nickname pelo menos 4 caracteres
        # - jogo selecionado
        # - regras aceitas (checkbox)