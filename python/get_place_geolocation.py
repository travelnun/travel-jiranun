#t physical position of device with Python
import urllib2 #for Python2.x
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
GOOGLE_PLACE_API_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
#GOOGLE_PLACE_API_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'


# Import the json library
import json
import pprint
from googleplaces import GooglePlaces, types, lang

google_place_api_key = 'AIzaSyBR1eF3HsroTfmsJOse9B6plG6TtFzbiSk'
google_map_api_key  = 'AIzaSyCo44ypTsgocMpIqZWxcIqjhpVm5NLu1zE'

#print google_places
google_places = GooglePlaces(google_place_api_key) 

# You may prefer to use the text_search API, instead.
#chonburi = {'lat': 13.3611431, 'lng': 100.9846717};
chonburi = {'lat': 13.279921, 'lng': 100.945044};
#nearby_search
query_result = google_places.nearby_search(
		#lat_lng={'lat': 13.3622, 'lng': 100.9835},
		lat_lng= chonburi,
		location= ['Chonburi', 'Chon Buri', 'Chang Wat Chon Buri'], 
		#keyword='food',
		type = ['airport'                     ,
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
				'zoo'                          	],
        radius=200
	   )

	   
   
	   
# If types param contains only 1 item the request to Google Places API
# will be send as type param to fullfil:


if query_result.has_attributions:
    print query_result.html_attributions


index = 1            # Python's indexing starts at one

for place in query_result.places:
    # Returned places from a query are place summaries.
	print index
	print "----------------\n"
	place.get_details()
	#print place.details # A dict matching the JSON response from Google.
	
	#print place.place_id
	pprint.pprint(place.details, depth=5)
	
	#print place.place_id
	
	#pprint(vars(place))
	
	index += 1
	#file_chonburi.write("----------------\n")
	print "----------------\n"
	