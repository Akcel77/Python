# QueryDB.py

import sqlite3

db_filename = "weather.db"

db_connector = sqlite3.connect(db_filename)

db_cursor = db_connector.cursor()

db_cursor.execute("Select Reading From Temperature Where Time >= 1200 and Time < 1300")
# db_cursor.execute("Select Time, Reading From Temperature")
the_data = db_cursor.fetchall()

# Use list comprehension to reduce the list of tuples to a list of ints
temperatures = [i[0] for i in the_data]

highest = sorted(temperatures, reverse = True)[0]
lowest = sorted(temperatures)[0]
average = sum(temperatures) / len(temperatures)

print(temperatures)

print(highest)
print(lowest)
print(average)


    
db_connector.close()
