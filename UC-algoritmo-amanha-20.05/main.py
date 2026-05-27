from flask import Flask, render_template, request 

app = Flask(__name__)
 
@app.route('/autenticar')
def autenticar():
    return render_template('autenticar.html')
 
@app.route('/recebedados', methods=['POST'])
def recebedados():
    usuario = request.form.get('username')
    email = request.form.get('email')
    return "{} e {}".format(usuario, email)

if __name__ == '__main__':
    app.run(debug=True)