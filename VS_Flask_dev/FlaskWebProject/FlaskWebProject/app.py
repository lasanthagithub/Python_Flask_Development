
from flask import Flask, render_template
from data import Articles

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
    #id = str(5)
    return render_template('article.html', id=id)
    # /<string:id>/


if __name__ == '__main__':
    #import os
    #HOST = os.environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(os.environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)
    app.run(debug=True)
