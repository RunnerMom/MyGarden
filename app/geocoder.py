import requests

#This list will store all the distances calculated so that it can be passed onto Jinja
distances = []

def get_distance_from_addresses(buyer_address, seller_address):
	buyer_add = buyer_address.replace(" ","+")
	seller_add = seller_address.replace(" ","+")

	url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins="+buyer_add+"&destinations="+seller_add+"&units=imperial&language=en&sensor=false"
	results = requests.get(url)
	results_json = results.json()

	if results_json["rows"][0]["elements"][0]["status"] != "OK":
		distance = "No possible driving route!"
	else:
		distance = (results_json["rows"][0]["elements"][0]["distance"]["text"])
	distances.append(distance)

	# return distances
	#Now the distances list can be passed onto Jinja and where it can be iterated over