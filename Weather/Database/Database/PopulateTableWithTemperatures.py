# PopulateTableWithTemperatures.py

import sqlite3
import random

db_filename = "weather.db"
start_time = 1200
end_time = 60
increment = 5
min_temperature = 10
max_temperature = 12

db_connector = sqlite3.connect(db_filename)

hours = range(0, 24)

for hour in hours:
    
    for mins in range(0, 60, 10):
        
        reading_time = hour * 100 + mins
        random_reading = random.randint(min_temperature, max_temperature )
        # Funny weather that day ;-)
        db_connector.execute("INSERT INTO  Temperature (Time, Reading) VALUES ({}, {})".format(reading_time, random_reading))

        
db_connector.commit()
db_connector.close()

