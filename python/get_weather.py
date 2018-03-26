#t physical position of device with Python
import urllib2 #for Python2.x
GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
GOOGLE_PLACE_API_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

# Import the json library
import json

#!/usr/bin/env python
#import pywapi
import string
from pprint import pprint
'''
#The Google Weather API has been discontinued as of September 2012.
#google_result = pywapi.get_weather_from_google('10001')
#'error': 'Could not connect to Yahoo! Weather'
#yahoo_result = pywapi.get_weather_from_yahoo('10001')
noaa_result = pywapi.get_weather_from_noaa('KJFK')

print json.dumps(noaa_result,indent=4, sort_keys=True)

print "-----------------------------------------------"

'''

import requests #to get data as JSON from a website
#from weather import Weather, Unit
#weather = Weather(unit=Unit.CELSIUS)

from googleplaces import GooglePlaces, types, lang
GOOGLE_MAPS_API_KEY = 'AIzaSyBR1eF3HsroTfmsJOse9B6plG6TtFzbiSk'
google_places = GooglePlaces(GOOGLE_MAPS_API_KEY)

#--------------------------------------------------
#city = raw_input("Enter city name: ")
 
#--this will give you a dictionary of all cities in the world with this city's name Be specific (city, country)!
#lookup = pywapi.get_location_ids(city)
#print lookup


#--workaround to access last item of dictionary
#for i in lookup:
#    location_id = i
#print i
 
import requests
OpenWeatherMap_API_KEY = 'ad7ebe6e90d42cfe747205fc1b703528'
OpenWeatherMap_API_URL = 'http://api.openweathermap.org/data/2.5/weather'
#API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
API_ENDPOINT = OpenWeatherMap_API_URL
 
#place = raw_input("Enter your city name:")
 
params = {
			#'q':place,
			'lat':13.3622,
			'lon':100.9835,
			'appid':OpenWeatherMap_API_KEY,
			'mode':'json'
         }
myData = requests.get(API_ENDPOINT, params = params)
myweather = myData.json()
print json.dumps(myweather,indent=4, sort_keys=True)


'''

query_result = google_places.nearby_search(
		lat_lng={'lat': 13.3622, 'lng': 100.9835},
        location='Chonburi, Thailand', 
		keyword='food',
        radius=10000
	   )
	 
if query_result.has_attributions:
    print query_result.html_attributions
   

for place in query_result.places:
    # Returned places from a query are place summaries.
	print "---------------------------------------------------------"
	#print place.place_id
	print place.geo_location
	lat = place.geo_location["lat"]
	lng = place.geo_location["lng"]

	#nav_request = "lat={}&log={}&appid={}".format(lat,lng,OpenWeatherMap_API_KEY)
	nav_request = "lat={"+lat+"}&log={"+lng+"}&appid={"+OpenWeatherMap_API_KEY+"}"
	request_weather = OpenWeatherMap_API_URL + nav_request
	response = requests.get(request_weather)
	weather_json = response.json()
	print weather_json
	
	#pprint(vars(place))  
	#forecast = Week(lat,lon,options)
	#location_id now contains the city's code
	#weather_com_result = pywapi.get_weather_from_weather_com(location_id)
	#print weather_com_result
	
	
'''	
	
	
'''	
lat = 13.3622
lng =100.9835
request = requests.get(place.geo_location)
location = json.loads(request.text)
'''
	 
'''
	nav_request = "lat={}&lng={}&appid={}".format(lat,lng,OpenWeatherMap_API_KEY)
	request_weather = OpenWeatherMap_API_URL + nav_request
	response = urllib2.urlopen(request_weather).read() #for Python2.x
	mydata = json.loads(response)
	print mydata
'''
print "---------------------------------------------------------"

	
	
	
'''
for place in query_result.places:
	print place.vicinity
	# Lookup via location name.
	location = weather.lookup_by_location(place.vicinity)
	condition = location.condition()
	print(condition.text())
'''


	
	
'''
# Get weather forecasts for the upcoming days.

forecasts = location.forecast()
for forecast in forecasts:
    #print(forecast.text())
	#print(forecast.date())
    #print(forecast.high())
    #print(forecast.low())
	pprint(vars(forecast))

print "-----------------------------------------------"
'''