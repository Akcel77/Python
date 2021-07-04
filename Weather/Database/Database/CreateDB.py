# CreateDB.py

import sqlite3

db_filename = "weather.db"

db = sqlite3.connect(db_filename)
	
db.close()
