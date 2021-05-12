import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "personalityType"
)

mycursor = db.cursor()

def readDb():
    query = "SELECT * FROM `typeTbl` LIMIT 1 "
    mycursor.execute(query)
    for x in mycursor:
        print(x)

# readDb()