# QueryRemoteDB.py

import urllib.request
import json
import ssl

# Handle self signed cert
ssl._create_default_https_context = ssl._create_unverified_context

hour = 11
url = "https://192.168.1.70:5000/?reqd=temperature&hour=" +str(hour)

requested_data = urllib.request.urlopen(url)

json_data = requested_data.read()
dict_data = json.loads(json_data)

average = dict_data["average"]
highest = dict_data["highest"]
lowest = dict_data["lowest"]

start_time = hour * 100
end_time = start_time + 50

print("The average temperature between {} and {} was {:.2f} degrees.".format(start_time, end_time, average))
print("The lowest temperature was {} and the highest was {}.".format(lowest, highest))



