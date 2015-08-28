import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
import sqlite3

@newrelic.agent.background_task()
def caller():
	db = sqlite3.connect('example.db')

	cursor = db.cursor()

	name1 = 'John'
	phone1 = '5555555'
	email1 = 'john@example.com'
	password1 = 'password'

	name2 = 'Jane'
	phone2 = '5551111'
	email2 = 'jane@example.net'
	password2 = '1234'

	# Create table
	cursor.execute('''CREATE TABLE users
		            (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')

	# Insert a row of data
	cursor.execute('''INSERT INTO users(name,phone,email,password)
		                VALUES(?,?,?,?)''',(name1,phone1,email1,password1))
	print "First user inserted"

	cursor.execute('''INSERT INTO users(name,phone,email,password)
		                VALUES(?,?,?,?)''',(name2,phone2,email2,password2))

	print "Second user inserted"

	#Save (commit) the changes
	db.commit()

	for row in cursor.execute('SELECT * FROM users ORDER BY name'):
	  print row           

	#If done with the connection, can close it.
	#Be sure any changes have been committed or they will be lost
	db.close()

caller()