'''This program is working. But improvements are going on for followings
    ## TODO
    ## Add a layer to only allow to delete own content
    ## Display a conformation messege before deletion completion
    ## Prevent users from registering several accounts
    ## Prevent duplications
    ## Break app.py to several modules for diffrent tasks
    ## Add company to registration form

'''

import gc
import os
from flask import Flask, render_template, flash, url_for, logging, session, request, redirect
#from data import Articles
#from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators, TextAreaField, BooleanField
from passlib.hash import sha256_crypt
from functools import wraps
#from data import DatabaseCon

#from dbconnect import connection
from MySQLdb import escape_string as thwart
import dbhandle
#from data import dbhandle
from Cover_Descriptions import cover_discription

## Instance of flask class
app = Flask(__name__)




"""

#debug=True ## here or below. need to remoce when production

## Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app

"""
#####################################################################################
## Root or Home or Index page
@app.route('/')
def index():
    return render_template('home.html')

#####################################################################################
## About page
@app.route('/about')
def about():
    return render_template('about.html')

#####################################################################################
## Myaccount info
@app.route('/myaccount')
def myaccount():
    return render_template('myaccount.html')

#####################################################################################
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




#####################################################################################
## Get individual items
@app.route('/article/<string:id>/')
def article(id):
    ## Create cursor
    cur = mysql.connection.cursor()

    ## Get articles
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone() ## get one article

    return render_template('article.html', article=article)
    
#####################################################################################
## Registration Form
## Defining WTForm class
class RegisterForm(Form): ## object is request.form type
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Username/Password do not match')])
    confirm = PasswordField('Confirm Password')
    accept_tos = BooleanField('I accept the <a href="/tos/">Terms of Service</a> and the\
                     <a href="/privacynotice/">Privacy Notice</a>. Last updater Oct 2017', [validators.DataRequired()])


#####################################################################################
## New user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        form = RegisterForm(request.form)  ## creating an object instance from RegisterForm class   
    
        if request.method == 'POST' and form.validate():
       
            name = form.name.data
            email = form.email.data
            username = form.username.data
            password = sha256_crypt.encrypt(str(form.password.data))

            if dbhandle.is_user(username) > 0: ## return value is an integer
                flash("The username is already tacken, please choose another.")
                return render_template('register.html', form=form)
            else:
                dbhandle.register__(name, email, username, password)

                flash('Your are now registered. Please log in', 'success')
                return redirect(url_for('login'))
        return render_template('register.html', form=form)  
    ## Activate only for debugging process
    #except Exception as e:
    #    return(str(e))
    except:
            return('Eroor 404')

    


#####################################################################################
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ## Get form fields
        username = request.form['username']
        password_candidate = request.form['password']
        try:
            ## Create a curser
            ## Get user by user name
            result = dbhandle.get_user(username)

        ## Activate only for debugging process
        #except Exception as e:
        #    return(str(e))
        except:
            return('Eroor 404')

        if len(result) > 0:
            ## Get stored hash
            #data = cur.fetchone()
            #password = data['password']
            password = result[0][1]

            ## compare passwords
            if sha256_crypt.verify(password_candidate, password):
                ## if passed create a session
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                #return redirect(url_for('dashboard'))
                return redirect(url_for('show_cover_description'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            ### close connection
            #cur.close()
            #conn.close()
            #gc.collect() 
        else:
            error = 'Username not found. Please register!'
            return render_template('login.html', error=error)

    return render_template('login.html')
    ## Check for the duplicates



#####################################################################################
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

#####################################################################################
## Main analysis page
@app.route('/analysis_main')
@is_logged_in
def analysis_main():
    return render_template('analysis_main.html')


#####################################################################################
## Main analysis page
@app.route('/analysis_tool_landing')
@is_logged_in
def analysis_tool_landing():
    return render_template('analysis_tool_landing.html')


#####################################################################################
## CN computation
@app.route('/cn_computation', methods=['GET', 'POST'])
@is_logged_in
def cn_computation():
        
    ## Import the CN items dictionary
    cover_dict, titles = cover_discription()

    session['cn_preference_3'] = None
    session['cn_preference_3'] = None
    session['cn_preference_3'] = None

    if request.method == 'POST' and request.form['disc_sel'] == 'Save pref. 1...':
        ## Get values form checkboxes
        values = request.form.getlist('cover_des_check')
        if values:
            session['cn_preference_1'] = values
            flash('CN computation "Preference 1" is saved for this session.', 'success')
        else:
            flash('Please select items for Preference 1.', 'warning')

    if request.method == 'POST' and request.form['disc_sel'] == 'Save pref. 2...':
        ## Get values form checkboxes
        values = request.form.getlist('cover_des_check')
        if values:
            session['cn_preference_2'] = values
            flash('CN computation "Preference 2" is saved for this session.', 'success')
        else:
            flash('Please select items for Preference 2.', 'warning')

    if request.method == 'POST' and request.form['disc_sel'] == 'Save pref. 3...':
        ## Get values form checkboxes
        values = request.form.getlist('cover_des_check')
        if values:
            session['cn_preference_3'] = values
            flash('CN computation "Preference 3" is saved for this session.', 'success')
        else:
            flash('Please select items for Preference 3.', 'warning')

    return render_template('cn_computation.html', covers = cover_dict)



#####################################################################################
## Edit CN preferences
@app.route('/cn_preferences_edit')
@is_logged_in
def cn_preferences_edit():
    return render_template('cn_preferences_edit.html')


#####################################################################################
## Edit CN preferences
@app.route('/to_add')
@is_logged_in
def to_add():
    return render_template('to_add.html')



#####################################################################################
## Cover description
@app.route('/show_cover_description', methods=['GET', 'POST'])
@is_logged_in
def show_cover_description():
    from Cover_Descriptions import cover_discription
    cover_dict, titles = cover_discription()

    if request.method == 'POST' and request.form['disc_sel'] == 'Save_pref1':
        ## Get values form checkboxes
        values = request.form.getlist('cover_des_check')
        flash(values, 'success')
    #elif request.method == 'POST' and request.form['disc_sel'] == 'Add to Selection 2':
    #    ## Get values form checkboxes
    #    values = request.form.getlist('cover_des_check')
    #    flash(values, 'success')

    #elif request.method == 'POST' and request.form['disc_sel'] == 'Add to Selection 3':
    #    ## Get values form checkboxes
    #    values = request.form.getlist('cover_des_check')
    #    flash(values, 'success')
    #    #return render_template('selection1.html', values = values)    


    return render_template('show_cover_description.html', covers = cover_dict)



#####################################################################################
## Cover description
@app.route('/select_cover_description', methods=['GET', 'POST'])
@is_logged_in
def select_cover_description():
    from Cover_Descriptions import cover_discription
    cover_dict, titles = cover_discription()

    if request.method == 'POST' and request.form['disc_sel'] == 'Save_pref1':
        ## Get values form checkboxes
        values = request.form.getlist('cover_des_check')
        flash(values, 'success')
    #elif request.method == 'POST' and request.form['disc_sel'] == 'Add to Selection 2':
    #    ## Get values form checkboxes
    #    values = request.form.getlist('cover_des_check')
    #    flash(values, 'success')

    #elif request.method == 'POST' and request.form['disc_sel'] == 'Add to Selection 3':
    #    ## Get values form checkboxes
    #    values = request.form.getlist('cover_des_check')
    #    flash(values, 'success')
    #    #return render_template('selection1.html', values = values)    


    return render_template('cover_description.html', covers = cover_dict)






#####################################################################################
## Selection1
@app.route('/selection1', methods=['GET', 'POST'])
@is_logged_in
def selection1():
    selection = request.form.getlist('cover_des_check')
    if request.method == 'POST':
        #if request.method == 'POST' and request.form['discr_sel'] == 'Preference 1':
        #    values = request.form.getlist('cover_des_check')
        flash(selection, 'success')
        return redirect(url_for('selection1'), selection = selection)




#####################################################################################
## Log out
@app.route('/logout')
@is_logged_in
def logput():   
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))



"""	
#####################################################################################
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






#####################################################################################
## Articles Form class
## Defining WTForm class
class ArticlerForm(Form): ## object is request.form type
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])

#####################################################################################
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

#####################################################################################
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

#####################################################################################
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




"""
#####################################################################################
if __name__ == '__main__':
    #import os
    #HOST = os.environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(os.environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)
    app.secret_key = 'datamanagement'

    #app.secret_key = os.urandom(59) ## moved to top
    app.run(debug=True)
