from flask import Flask,render_template, url_for

app = Flask(__name__)

@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')
@app.add_template_global
def repeat(s,n):
    return s*n

from datetime import datetime

@app.route("/")
def index():
    print(url_for("index"))
    print(url_for("hello",name = "Santiago",age=27))
    print(url_for("code", code = 'print("Hola")'))
    name = "Santiago"
    amigos = ["Agustina","Pedro","Leon"]
    date = datetime.now()
    return render_template("index.html",
    name=name,
    amigos=amigos,
    date = date
    )

@app.route("/hello")
@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/<int:age>")
@app.route("/hello/<string:name>/<int:age>/<string:email>")


def hello(name= None,age= None, email=None):
    my_data={
        'name': name,
        'age' : age,
        'email' : email
    }
    return render_template('hello.html',data = my_data)

from markupsafe import escape
@app.route("/code/<path:code>")
def code(code):
    return f"<code>{escape(code)}</code>"

