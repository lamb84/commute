import googlemaps
from datetime import datetime
import json

gmaps = googlemaps.Client(key='AIzaSyBknqIxQcdcDMT-po3pNYat7dj0yH7fLeE')

time = datetime.now()
home = '418 Beachview Drive, North Vancouver, BC'
work = '138 East 7th Avenue, Vancouver, BC'
commute_json = gmaps.distance_matrix(origins = home, destinations = work, departure_time = time)
print commute_json
#commute = json.load(commute_json)
#geocode_home = gmaps.geocode('418 Beachview Drive, North Vancouver, BC')
#geocode_work = gmaps.geocode('138 East 7th Avenue, Vancouver, BC')
#print geocode_home
#print geocode_work




#directions_result = gmaps.directions("Sydney Town Hall","Parramatta, NSW",mode="transit",departure_time=now)


#print(geocode_result)
#print(directions_result)
