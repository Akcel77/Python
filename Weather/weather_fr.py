# GetNZCity.py
import json

import json
import urllib.request
filename = "city.list.json"

fr_data = {}

with open(filename, encoding='utf-8') as json_file:  
    json_data = json.load(json_file)
    for entry in json_data:
         if entry["country"] == "FR":

            # Extract required values
            city = entry["name"].title()
            city_id = entry["id"]
            longitude = entry["coord"]["lon"]
            latitude = entry["coord"]["lat"]

            # Populate the subset dictionary
            fr_data.update({city : {
                    "city_id" : city_id,
                    "longitude" : longitude,
                    "latitude" : latitude
                    }})

def get_weather_data(weather_url):
    weather_request = urllib.request.urlopen(weather_url)
    json_data = weather_request.read().decode("utf-8")
    weather_dict = json.loads(json_data)
    weather_request.close()

    return(weather_dict) 

### Show the NZ data sorted by "city" name
for city_key, city_value in sorted(fr_data.items()):
    print("{:30} {:8} {:11} {:11}".format(city_key, city_value["city_id"], city_value["longitude"], city_value["latitude"]))

##city_id = "7910036" 
##user_api = "d0d782f766cc708deff54da947e5ece1"  
##unit = "metric"  
##url = "http://api.openweathermap.org/data/2.5/weather?id=" + city_id + "&mode=json&units=" + unit + "&APPID=" + user_api
##    
##weather_data = get_weather_data(url)
##
### print(weather_data)
##
##print("Location: {}".format(weather_data.get("name")))
##print("Current temperature: {}".format(weather_data["main"]["temp"]) )
##print("Wind Speed: {} direction: {:03} degrees".format(weather_data["wind"]["speed"], weather_data["wind"]["deg"]))
##print("Humidity: {}".format(weather_data["main"]["humidity"]))
##print("Pressure: {}".format(weather_data["main"]["pressure"]))

