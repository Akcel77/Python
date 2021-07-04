# SimplePopulateTable.py

import sqlite3

db_filename = "weather.db"

db_connector = sqlite3.connect(db_filename)

db_connector.execute("INSERT INTO  Temperature (Time, Reading) VALUES (1,2)")
db_connector.commit()
db_connector.close()
