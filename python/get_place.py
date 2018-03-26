#t physical position of device with Python
import urllib2 #for Python2.x
GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
GOOGLE_PLACE_API_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

# Import the json library
import json
from pprint import pprint
from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyBR1eF3HsroTfmsJOse9B6plG6TtFzbiSk'

google_places = GooglePlaces(YOUR_API_KEY)
#print google_places

#print json.dumps(types.TYPE_FOOD,indent=4, sort_keys=True)
# You may prefer to use the text_search API, instead.
chonburi = {'lat': 13.3611431, 'lng': 100.9846717};
query_result = google_places.nearby_search(
		#lat_lng={'lat': 13.3622, 'lng': 100.9835},
		lat_lng= chonburi,
		location='Chonburi, Thailand', 
		keyword='food',
		type = [ 'restaurant' ]
       # radius=20000
	   )
# If types param contains only 1 item the request to Google Places API
# will be send as type param to fullfil:
# http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

if query_result.has_attributions:
    print query_result.html_attributions
   



for place in query_result.places:
    # Returned places from a query are place summaries.
	print "----------------"
	print place.place_id
	print place.get_details()
	pprint(vars(place))

	
	
	
	
	
	
	
	
	
	
	
	
'''
    print place.name
    print place.geo_location
    print place.place_id
    print place.rating
'''
    # The following method has to make a further API call.
    #place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    #print place.details # A dict matching the JSON response from Google.
    #print json.dumps(place,indent=4, sort_keys=True)
	#print place.local_phone_number
    #print place.international_phone_number
    #print place.website
    #print place.url
	

	
'''
    # Getting place photos

    for photo in place.photos:
        # 'maxheight' or 'maxwidth' is required
        photo.get(maxheight=500, maxwidth=500)
        # MIME-type, e.g. 'image/jpeg'
        photo.mimetype
        # Image URL
        photo.url
        # Original filename (optional)
        photo.filename
        # Raw image data
        photo.data
'''


'''
# Are there any additional pages of results?
if query_result.has_next_page_token:
    query_result_next_page = google_places.nearby_search(
            pagetoken=query_result.next_page_token)


# Adding and deleting a place
try:
    added_place = google_places.add_place(name='Mom and Pop local store',
            lat_lng={'lat': 51.501984, 'lng': -0.141792},
            accuracy=100,
            types=types.TYPE_HOME_GOODS_STORE,
            language=lang.ENGLISH_GREAT_BRITAIN)
    print added_place.place_id # The Google Places identifier - Important!
    print added_place.id

    # Delete the place that you've just added.
    google_places.delete_place(added_place.place_id)
except GooglePlacesError as error_detail:
    # You've passed in parameter values that the Places API doesn't like..
    print error_detail


'''





