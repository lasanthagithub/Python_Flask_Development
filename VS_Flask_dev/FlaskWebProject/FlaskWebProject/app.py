
from flask import Flask, render_template, flash, url_for, logging, session
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt

## Instance of flask class
app = Flask(__name__)

Articles = Articles()
#debug=True ## here or below. need to remoce when production

## Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app


@app.route('/')
def index():
    
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route("/article/<string:id>/")
def article(id):
   return render_template('article.html', id=id)
    

## Defining WTForm class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', 'message'='Password do not match')])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html', form=form)



if __name__ == '__main__':
    #import os
    #HOST = os.environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(os.environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)
    app.run(debug=True)
