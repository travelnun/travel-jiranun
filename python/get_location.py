#!/usr/bin/python

import urllib2 #for Python2.x
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
# Import the json library
import json

api_key  = 'AIzaSyCW42gam9T6jGNnEeaj1vsjYLs5363KcJo'

print "========== get  location =========="
origin = raw_input("Where are you?: ").replace(" ","+") #raw_input() for Python2.x but input() for python3.x
destination = raw_input("Where do you want to go?: ").replace(" ","+")
#print(origin)
#print(destination)
nav_request = "origin={}&destination={}&key={}".format(origin,destination,api_key)

request = endpoint+ nav_request
response = urllib2.urlopen(request).read() #for Python2.x
directions = json.loads(response)

print json.dumps(directions,indent=4, sort_keys=True)
