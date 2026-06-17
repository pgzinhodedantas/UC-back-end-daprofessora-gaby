from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'chave-secreta' 

@app.route("/contador")
def contador():
    if "contador" not in session:
        session["contador"] = 0
    session["contador"] += 1
@app.route("/contador/zerar", methods=["POST"])
def zerar_contador():
    session.pop("contador", None)
    return redirect(url_for("contador"))

if __name__ == '__main__':
    app.run(debug=True)