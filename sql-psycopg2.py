import psycopg2


#Connect to chinook db
connection = psycopg2.connect(database="chinook")

# build a cursor object of the DB
cursor = connection.cursor()
#Query 1 selsect all records from artist table
#cursor.execute('SELECT * FROM "artist"')

#Query get only the name column from artist table
cursor.execute('SELECT "name" FROM "artist"')
# fetch results(multiple)
results = cursor.fetchall()

# fetch results single
# results = cursor.fetchone()

#close connection
connection.close()


for result in results:
    print(result)