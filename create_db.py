import sqlite3

connection = sqlite3.connect('site_db.sqlite')
cursor = connection.cursor()
with open('create_db.sql', 'r') as f:
    text = f.read()
cursor.executescript(text)
cursor.close()
connection.close()