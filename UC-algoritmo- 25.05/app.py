from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

if __name__ == "__main__":
    app.run(debug=True) 