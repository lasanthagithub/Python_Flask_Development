import MySQLdb

def connection():
	conn = MySQLdb.connect(host = "localhost",
							user = "root",
							passwd = "america",
							db = "python_flask")
	c = conn.cursor()
	return c, conn;