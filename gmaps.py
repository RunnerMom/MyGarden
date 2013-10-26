from urllib2 import urlopen
import json 
'''
This module is part of the MyGarden app for LinkedIn DevelopHer hackday 10/25/13.
It sends an http request to the Google Maps API and retrieves a JSON object showing the distance 
between the buyer and the seller
'''


def get_distance(buyer_address, seller_address):
	url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&units=imperial&sensor=false"
	% (buyer_address, seller_address)
	f = urlopen(url) 
	json_string = f.read() 
	parsed_json = json.loads(json_string) 
	distance = parsed_json['current_observation']['temp_f'] 

	print "Current temperature in %s, %s is: %s" % (city, state, temp_f) 
	f.close()

def forecast10(city, state):	#10-day forecast (starting today)for given city, state
	f = urlopen('http://api.wunderground.com/api/fbec2cc984499b31/forecast10day/q/%s/%s.json' % (state, city)) 
	json_string = f.read() 
	parsed_json = json.loads(json_string) 
	tenDayList=parsed_json['forecast']['simpleforecast']['forecastday'] 
	high_list=[]
	low_list=[]
	for i in range(len(tenDayList)):
		high_list.append(int(tenDayList[i]['high']['fahrenheit']))
		low_list.append(int(tenDayList[i]['low']['fahrenheit']))
	avg_high = sum(high_list)/len(high_list)
	avg_low = sum(low_list)/len(low_list) 
	return {"avgHigh":avg_high,
			"avgLow": avg_low}
	f.close()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()