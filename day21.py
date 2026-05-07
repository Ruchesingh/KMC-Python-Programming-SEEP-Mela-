""""import mysql.connector

db=mysql.connector.connect(
host="localhost",
username="root",
)
print(db)"""

import sqlite3
connection=sqlite3.connect('students.sqlite3')

terminal=connection.cursor()

# insert query 
query='insert into students (id,name ,course,marks,email) into values (3,"Ruchee","BCA",45,"sing5778@gamil.com")'
terminal.execute(query)
connection.commit()
print(connection)
