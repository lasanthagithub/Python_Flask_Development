from dbconnect import connection
from MySQLdb import escape_string as thwart
import gc
## Insert registration data into database
def register__(name_, email_,username_, password_):

    if True:
        ## Create a curser
        cur, conn = connection()
   
        ## Execute quarry
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",(thwart(name_), thwart(email_), thwart(username_), thwart(password_)))

        ## Comit to db
        conn.commit()

        ## Close connection
        cur.close()
        conn.close()
        gc.collect()

## Get user info from the database
def get_user(username_):

    ## Create a curser
    cur, conn = connection()  
    
    ## Execute quarry
    user = cur.execute("SELECT username, password FROM users WHERE username = (%s)", (thwart(username_),)) ## Important ','
    result = cur.fetchall()
    ## Close connection
    cur.close()
    conn.close()
    gc.collect()  
    
    return result #cur, conn, user


## Check user
def is_user(username_):

    ## Create a curser
    cur, conn = connection()  
    
    ## Execute quarry
    user = cur.execute("SELECT * FROM users WHERE username = (%s)", (thwart(username_),)) ## Important ','

    ## Close connection
    cur.close()
    conn.close()
    gc.collect()  
    
    return user