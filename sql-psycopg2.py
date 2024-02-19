import psycopg2


#Connect to chinook db
connection = psycopg2.connect(database="chinook")

# build a cursor object of the DB
cursor = connection.cursor()
# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "aame" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_Id" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
#cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
#cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])
# fetch results(multiple)
results = cursor.fetchall()

# fetch results single
# results = cursor.fetchone()

#close connection
connection.close()


for result in results:
    print(result)