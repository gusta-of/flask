# Start Flask

from flask import Flask, request, render_template, abort, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os, json

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
# code


@app.route("/")
@app.route("/index")
def index():
    x = 30
    y = 10

    query = request.args.to_dict()
    return render_template('modelo.html', x=x, y=y, query=query)

# ------ INICIO UPLOAD

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            return redirect(request.url)

        files = request.files.getlist('files[]')
        for file in files:
            if file and allowed_file(file.filename):
                savePhat = os.path.join(
                    UPLOAD_FOLDER, secure_filename(file.filename))
                file.save(savePhat)
    
    return render_template('upload/uploads.html')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ------ FIM UPLOAD

@app.route("/calculo", methods=['POST'])
def calculo():
    array = [int(v) for v in request.form.to_dict().values()]
    nota = sum(array) / len(array)
    return render_template('teste1/calculo.html', nota=nota)


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
