import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    username = "root",
    passwd = "Hier muss mein root password rein,
    database = "Produkte"
)

cursor = db.cursor()

# ## defining the Query
# query = "INSERT INTO Produkte (marke, name) VALUES (%s, %s)"

# ## storing values in a variable
# values = ("Acer", "Acer Aspire 5")

# ## executing the query with values
# cursor.execute(query, values)


# ##Inserting
# query = "SELECT * FROM Produkte"
# cursor.execute(query)
# ## fetching all records from the 'cursor' object
# records = cursor.fetchall()

# ## Showing the data
# for record in records:
#     print(record)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "record inserted")