from dbconnect import connection
from passlib.hash import sha256_crypt

def register__(name_, email_,username_, password_):

    #form = RegisterForm(request.form)  ## creating an object instance from RegisterForm class
    
    
    if True:
        cur, conn = connection()
        name = name_
        email = email_
        username = username_
        password = sha256_crypt.encrypt(str(password_))
        

        ## Create a curser
        #cur = mysql.connection.cursor()

        ## Execute quarry''''''
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", 
                    (name, email, username, password))
        ## Comit to db
        conn.commit()
        ## Close connection
        cur.close()
