# SimpleDBquery.py

import sqlite3

db_filename = "weather.db"

db_connector = sqlite3.connect(db_filename)

db_cursor = db_connector.cursor()

db_cursor.execute("Select Time, Reading From Temperature Where Time >= 1200 and Time < 1300")
the_data = db_cursor.fetchall()
print(the_data)
    
db_connector.close()
