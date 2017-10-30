
from flask import Flask, render_template, flash, url_for, logging, session, request, redirect
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators, TextAreaField
from passlib.hash import sha256_crypt
from functools import wraps
#from data import DatabaseCon

## Instance of flask class
app = Flask(__name__)

## Congigure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'america1200'
app.config['MYSQL_DB'] = 'python_flask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

## Initilize MySQL
#mysql = DatabaseCon(app)
mysql = MySQL(app)

#Articles = Articles()


#debug=True ## here or below. need to remoce when production

## Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app

## Root or Home or Index page
@app.route('/')
def index():    
    return render_template('home.html')


## About page
@app.route('/about')
def about():
    return render_template('about.html')


## Articles page
@app.route('/articles')
def articles():
    ## Create cursor
    cur = mysql.connection.cursor()

    ## Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall() ## get all the articles to a dictionary list

    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No articles found'
        return render_template('articles.html', msg=msg)
    cur.close()





## Get individual items
@app.route('/article/<string:id>/')
def article(id):
    ## Create cursor
    cur = mysql.connection.cursor()

    ## Get articles
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone() ## get one article

    return render_template('article.html', article=article)
    

## Registration Form
## Defining WTForm class
class RegisterForm(Form): ## object is request.form type
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')])
    confirm = PasswordField('Confirm Password')



## New user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)  ## creating an object instance from RegisterForm class
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        ## Create a curser
        cur = mysql.connection.cursor()

        ## Execute quarry
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", 
                    (name, email, username, password))

        ## Comit to db
        mysql.connection.commit()

        ## Close connection
        cur.close()

        flash('Your are now registered and can log in', 'Success')
        return redirect(url_for('index'))

    return render_template('register.html', form=form)


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ## Get form fields
        username = request.form['username']
        password_candidate = request.form['password']

        ## Create a curser
        cur = mysql.connection.cursor()

        ## Get user by user name
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            ## Get stored hash
            data = cur.fetchone()
            password = data['password']

            ## compare passwords
            if sha256_crypt.verify(password_candidate, password):
                ## if passed create a session
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            ## close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')




## Check if user logged in. 
## When use this function, the particular action is only allowed if logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


## Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    ## Create cursor
    cur = mysql.connection.cursor()

    ## Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall() ## get all the articles to a dictionary

    if result > 0:
        return render_template('dashboard.html', articles=articles)
    else:
        msg = 'No articles found'
        return render_template('dashboard.html', msg=msg)
    cur.close()







## Articles Form class
## Defining WTForm class
class ArticlerForm(Form): ## object is request.form type
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])


## ADD article
@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticlerForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        ## Create cursor
        cur = mysql.connection.cursor()

        ## SQL codes for creating a table
        ### CREATE TABLE articles (id INT(11) PRIMARY KEY auto_increment, title varchar(255), 
        #author varchar(100), body text, create_date timestamp default current_timestamp);
        
        ## Execute
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)", 
                    (title, body, session['username']))

        ## Commit to DB
        mysql.connection.commit()

        ## Close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))
    return render_template('add_article.html', form=form)


## Edit article
@app.route('/edit_article/<string:id>/', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    ## Create cursor
    cur = mysql.connection.cursor()

    ## Get article by id
    result = cur.execute('SELECT * FROM articles WHERE id = %s', [id])
    article = cur.fetchone()

    form = ArticlerForm(request.form)

    ## Populate article from fields
    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']
        
        ## Execute
        cur.execute("UPDATE articles SET title = %s, body = %s WHERE id = %s", 
                    (title, body, id))

        ## Commit to DB
        mysql.connection.commit()

        ## Close connection
        cur.close()

        flash('Article Edited', 'success')

        return redirect(url_for('dashboard'))
    return render_template('edit_article.html', form=form)

## Delete articla
@app.route('/delete_article/<string:id>/', methods = ['POST'])
@is_logged_in
def delete_article(id):
    ## create cursor
    cur = mysql.connection.cursor()

    ## Get article by id
    result = cur.execute('DELETE FROM articles WHERE id = %s', [id])

    ## Commit to DB
    mysql.connection.commit()

    ## close cursor
    cur.close()

    flash('Article Deleted', 'success')
    return redirect(url_for('dashboard'))



## Log out
@app.route('/logout')
@is_logged_in
def logput():   
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))



if __name__ == '__main__':
    #import os
    #HOST = os.environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(os.environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)
    app.secret_key = 'secret123'
    app.run(debug=True)
