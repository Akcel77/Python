# CreateTable.py

import sqlite3

db_filename = "weather.db"

db = sqlite3.connect(db_filename)

db.execute("Create Table Temperature \
         (Time int Primary Key Not Null, \
         Reading int);")
	
db.close()
