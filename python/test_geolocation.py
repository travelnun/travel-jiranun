import googlemaps
# Import the json library
import json
import pprint
from datetime import datetime
from googleplaces import GooglePlaces, types, lang

google_place_api_key = 'AIzaSyBR1eF3HsroTfmsJOse9B6plG6TtFzbiSk'
google_places = GooglePlaces(google_place_api_key) 
#print google_places

gmaps = googlemaps.Client(key='AIzaSyCo44ypTsgocMpIqZWxcIqjhpVm5NLu1zE')


#Weather api
import requests
OpenWeatherMap_API_KEY = 'ad7ebe6e90d42cfe747205fc1b703528'
OpenWeatherMap_API_URL = 'http://api.openweathermap.org/data/2.5/weather'
API_ENDPOINT = OpenWeatherMap_API_URL

# Geocoding an address

data_country = [
'ChonBuri'
]
'''
'ChonBuri',
'Chanthaburi',
'Chachoengsao',
'Trat',
'Rayong',
'Prachinburi'
'''

'''
'airport'                  ,
'amusement_park'              ,
'aquarium'                    ,
'art_gallery'                 ,
'atm'                         ,
'bakery'                      ,
'bank'                        ,
'bar'                         ,
'book_store'                  ,
'bowling_alley'               ,
'bus_station'                 ,
'cafe'                        ,
'campground'                  ,
'casino'                      ,
'cemetery'                    ,
'church'                      ,
'city_hall'                   ,
'clothing_store'              ,
'convenience_store'           ,
'gas_station'                 ,
'gym'                         ,
'hindu_temple'                ,
'hospital'                    ,
'laundry'                     ,
'library'                     ,
'liquor_store'                ,
'lodging'                     ,
'meal_delivery'               ,
'meal_takeaway'               ,
'mosque'                      ,
'movie_rental'                ,
'movie_theater'               ,
'museum'                      ,
'night_club'                  ,
'park'                        ,
'parking'                     ,
'pharmacy'                    ,
'police'                      ,
'restaurant'                  ,
'rv_park'                     ,
'shoe_store'                  ,
'shopping_mall'               ,
'spa'                         ,
'stadium'                     ,
'store'                      ,
'subway_station'              ,
'supermarket'                 ,
'synagogue'                   ,
'taxi_stand'                  ,
'train_station'               ,
'transit_station'             ,
'zoo'                         	
'''


geocode = [
		{
		"Aumpore" : "Ko Chan",
		"Ko Chan":
			[	
				{"district":"Ko Chan"},
				{"district":"Tha Bun Mi"}
			]
		},
		{
		"Aumpore" : "Ko Si Chang",
		"Ko Si Chang":
			[	
				{"district":"Tha Thewa Wong"}
			]
		},
		{
		"Aumpore" : "Mueang Chon Buri",
		"Mueang Chon Buri":
			[
				{"district":"Bang Pla Soi"},
				{"district":"Makham Yong"},
				{"district":"Ban Khot"},
				{"district":"Saen Suk"},
				{"district":"Ban Suan"},
				{"district":"Nong Ri"},
				{"district":"Na Pa"},
				{"district":"Nong Khang Khok"},
				{"district":"Don Hua Lo"},
				{"district":"Nong Mai Daeng"},
				{"district":"Bang Sai"},
				{"district":"Khlong Tamru"},
				{"district":"Mueang"},
				{"district":"Ban Puek"},
				{"district":"Ban Huai Kapi"},
				{"district":"Samet"},
				{"district":"Ang Sila"},
				{"district":"Samnak Bok"}
			]
		},
		
		{
		"Aumpore" : "Bo Thong",
		"Bo Thong":
			[	
				{"district":"Kaset Suwan"},
				{"district":"That Thong"},
				{"district":"Bo Kwang Thong"},
				{"district":"Bo Thong"},
				#{"district":"Phluang Thong"},
				{"district":"Wat Suwan"}
			]
		},
		{
		"Aumpore" : "Bang Lamung",
		"Bang Lamung":
			[	
				{"district":"Khao Mai Kaeo"},
				{"district":"Pong"},
				{"district":"Takhian Tia"},
				{"district":"Na Kluea"},
				{"district":"Bang Lamung"},
				{"district":"Nong Prue"},
				{"district":"Nong Pla Lai"},
				{"district":"Huai Yai"}
			]
		},
		{
		"Aumpore" : "Ban Bueng",
		"Ban Bueng":
			[	
				{"district":"Khlong Kio"},
				{"district":"Ban Bueng"},
				{"district":"Map Phai"},
				{"district":"Nong Phai Kaeo"},
				{"district":"Nong Chak"},
				{"district":"Nong Samsak"},
				{"district":"Nong Bon Daeng"},
				{"district":"Nong Irun"}
			]
		},
		{
		"Aumpore" : "Phanat Nikhom",
		"Phanat Nikhom":
			[	
				{"district":"Khok Phlo"},
				{"district":"Rai Lak Thong"},
				{"district":"Kut Ngong"},
				{"district":"Tha Kham"},
				{"district":"Thung Khwang"},
				{"district":"Na Roek"},
				{"district":"Na Matum"},
				{"district":"Na Wang Hin"},
				{"district":"Ban Soet"},
				{"district":"Ban Chang"},
				{"district":"Phanat Nikhom"},
				{"district":"Wat Bot"},
				{"district":"Wat Luang"},
				{"district":"Sa Si Liam"},
				{"district":"Nong Hiang"},
				{"district":"Nong Khayat"},
				{"district":"Nong Prue"},
				{"district":"Na Phrathat"},
				{"district":"Mon Nang"},
				{"district":"Hua Thanon"}
			]
		},
		{
		"Aumpore" : "Phan Thong",
		"Phan Thong":
			[	
				{"district":"Ko Loi"},
				{"district":"Khok Khi Non"},
				{"district":"Bang Nang"},
				{"district":"Bang Hak"},
				{"district":"Ban Kao"},
				{"district":"Phan Thong"},
				{"district":"Map Pong"},
				{"district":"Nong Kakha"},
				{"district":"Nong Tamlueng"},
				{"district":"Nong Hong"},
				{"district":"Na Pradu"}
			]
		},
		{
		"Aumpore" : "Si Racha",
		"Si Racha":
			[	
				{"district":"Khao Khansong"},
				{"district":"Thung Sukhla"},
				{"district":"Bo Win"},
				{"district":"Bang Phra"},
				{"district":"Bueng"},
				{"district":"Si Racha"},
				{"district":"Surasak"},
				{"district":"Nong Kham"}
			]
		},
		{
		"Aumpore" : "Sattahip",
		"Sattahip":
			[	
				{"district":"Samaesan"},
				{"district":"Na Chom Thian"},
				{"district":"Bang Sare"},
				{"district":"Phlu Ta Luang"},
				{"district":"Sattahip"}
			]
		},
		{
		"Aumpore" : "Nong Yai",
		"Nong Yai":
			[	
				{"district":"Khao Sok"},
				{"district":"Khlong Phlu"},
				{"district":"Nong Suea Chang"},
				{"district":"Nong Yai"},
				{"district":"Hang Sung"}
			]
		}
		
		 
	]

#pprint.pprint(geocode,  depth=5)
#print geocode[0]


loop_country = 0
for country in data_country:	
	for address in geocode:	
		ampore = address["Aumpore"]	
		#tambon = address[ampore]	
		#pprint.pprint(tambon,  depth=5)
		loop_tambon = 0
		for tambon in address[ampore]:	
			pprint.pprint(tambon,  depth=5)
			tambon = tambon["district"]
			#print tambon
			
			search_address = tambon + ", " + country + ", Thailand"
			print search_address
			geocode_result = gmaps.geocode(search_address)
			#pprint.pprint(geocode_result, depth=7)
			
			name = geocode_result[0]["address_components"][0]["long_name"]
			lat = geocode_result[0]["geometry"]["location"]["lat"]
			lng = geocode_result[0]["geometry"]["location"]["lng"]
			#test - print results
			print "===============" + name + "==============="
			result_lat_lng = {'lat': lat, 'lng': lng}
			print result_lat_lng
			
			#exit(0)
			
			place_keyword = ['food','cafe']
			print ">>>> google_places api"
			#nearby_search
			for keyword in place_keyword:
				print "********************************"
				print "********" + keyword + "*********"
				query_result = google_places.nearby_search(
						lat_lng= result_lat_lng,
						location= [address], 
						keyword=[keyword],
						type=['street_address'],
						radius=5000
					   )

				#Foreach place
				print "----------------\n"
				index = 1            # Python's indexing starts at one	   
				if query_result.has_attributions:
					print query_result.html_attributions

				print(len(query_result.places))
				if len(query_result.places) >0:
				
					for place in query_result.places:
						# Returned places from a query are place summaries.
						print "#place seq. " + str(index)
						place.get_details()
						#print place.details # A dict matching the JSON response from Google.
						#pprint.pprint(place.details, depth=5)			
						
						print "	place_id: " + place.place_id
						print "	place_name: " + place.name
						print "	place_types: " + place.types[0]
						print "	place_rating: " + str(place.rating)
						print "	place_address: " + place.vicinity

						index += 1
					else:
						print "don't found places for: " + search_address 
				
				'''
				print ">>>> distance_matrix api"
				driving_result = gmaps.distance_matrix(origins="Bangkok", destinations=name)
				#mode='driving' (default)
				pprint.pprint(driving_result, depth=6)
				print ">>>> distance_matrix api : Travel mode"
				now = datetime.now()
				origin_location = "13.7563309 , 100.50176510000006" #Bangkok location
				target_location = str(lat) + ", " + str(lng)
				directions_result = gmaps.directions(origin_location,
												 target_location,
												 mode="driving",
												 avoid="tolls",
												 departure_time=now
												)

				pprint.pprint(directions_result[0], depth=7)
				#print(directions_result[0]['legs'][0]['distance']['text'])
				#print(directions_result[0]['legs'][0]['duration']['text'])


				
				print ">>>> directions api"	
				directions = gmaps.directions("Bangkok", name)
				pprint.pprint(directions, depth=7)
				
				for step in directions[0]['legs'][0]['steps']:
					print step['html_instructions']
				
						
				# Weather	
				print ">>>> Weather api"	
				params = {
							#'q':place,
							'lat':lat,
							'lon':lng,
							'appid':OpenWeatherMap_API_KEY,
							'mode':'json'
						 }
				myData = requests.get(API_ENDPOINT, params = params)
				myweather = myData.json()
				print json.dumps(myweather,indent=4, sort_keys=True)
				
				# Lookup via location name.
				'''
				print "------ end " + tambon + " ------"
				loop_tambon += 1	
			
			print "------ end " + country + " ------"
			loop_country += 1			
	
print "++++++++++++++++++++++++++++++++"

	

	
'''
pprint.pprint(geocode_result2, depth=5)
pprint.pprint(geocode_result3, depth=5)
pprint.pprint(geocode_result4, depth=5)
pprint.pprint(geocode_result5, depth=5)
pprint.pprint(geocode_result6, depth=5)
'''