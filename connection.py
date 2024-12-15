import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = "",
    database = "hangman"
)

cursor_object = db.cursor()

