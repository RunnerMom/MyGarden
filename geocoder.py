from pygeocoder import Geocoder
import requests

buyer = "400 Magnolia Street, Orangeburg, SC, 29115"
buyer_add = buyer.replace(" ","+")


sellers = ["110 Castro St, Mountain View, CA", "2 Moneta Ct, San Francisco, CA"]
for seller in sellers:
	seller_add = seller.replace(" ","+")
	url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins="+buyer_add+"&destinations="+seller_add+"&units=imperial&language=en&sensor=false"

	results = requests.get(url)
	results_json = results.json()

	distance = (results_json["rows"][0]["elements"][0]["distance"]["text"]).replace(",",".")
	print distance





#Why doesn't the code work with lat and long?

# buyer_gcode = Geocoder.geocode(buyer)
# buyer_lat = buyer_gcode[0].coordinates[0]
# buyer_lng = buyer_gcode[0].coordinates[1]

	# results = Geocoder.geocode(seller)
	# lat = results[0].coordinates[0]
	# lng = results[0].coordinates[1]

	# print lat
	# print lng
	# url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%r,%r&destinations=%r,%r&language=fr-FR&sensor=false" % (buyer_lat, buyer_lat, lat, lng)

	
