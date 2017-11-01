class DatabaseCon(object):
    """This class make connection to MySQL database"""
    from flask_mysqldb import MySQL 
    def __init__(self, app):
        ## Congigure MySQL
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'america1200'
        app.config['MYSQL_DB'] = 'python_flask'
        app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

        ## Initilize MySQL             
        return MySQL(app)