from flask import Flask,render_template, url_for, request

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = "dev"
)

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
    amigos = ["Agustina","Franco","Leon"]
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

#Crear form con wtform

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField("Nombre de usuario: ", validators=[DataRequired(),Length(min=4,max=15)])
    password = PasswordField("Password: ",validators=[DataRequired(),Length(min=4,max=25)])
    submit = SubmitField ("Registrar:")


#Registrar Usuario
@app.route("/auth/register", methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"Nombre de usuario: {username}, Contraseña: {password}"

   # form = RegisterForm()
   # print(request.form)
   # if request.method== "POST":
   #     username = request.form["username"]
   #     password = request.form["password"]
   #     if len(username) >=4 and len(username) <=25 and len(password) >=6 and len(password) <=40:
   #         return f"Nombre de usuario: {username}, Contraseña: {password}"
   #     else:
   #         error= "El nombre de usuario debe tener entre 4 y 25 caracteres y la contraseña entre 4 y 25"
   #         return render_template("auth/register.html",form= form, error= error)
    return render_template("auth/register.html",form= form)