# Start Flask

from flask import Flask, request, render_template, abort, redirect, url_for
from json import dumps

app = Flask(__name__, static_folder='static', template_folder='templates')


# code

@app.route("/")
@app.route("/index")
def index():
    x = 30 
    y = 10

    query = request.args.to_dict()
    return render_template('modelo.html', x=x, y=y, query=query)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        if request.form['nome'] == "admin" and request.form['senha'] == "admin":
            res = request.form.to_dict()
            return redirect("sucesso/%s" % res['nome'], code=302)
            
        else: 
            abort(401)
    else:
        return abort(403)

@app.route("/sucesso/<name>")
def sucesso(name):
    return "<h1> Bem Vindo %s </h1>" % name


if __name__ == '__main__':
    app.run(debug=True)
