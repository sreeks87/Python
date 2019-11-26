import unirest
import json
def find_weather(loc):
	response = unirest.get("https://george-vustrey-weather.p.mashape.com/api.php?",
	  headers={
		"X-Mashape-Key": "",
		"Accept": "application/json"
	  },
	  params={ "location": loc}
	)
	#print response.code
	#print response.headers
	#print response.body
	#data =  response.raw_body
	data = json.loads(response.raw_body)
	#print json.loads(response.raw_body)
	for item in data:
		print"---------------------------------------------------------------------"
		print "For %s day" %item["day_of_week"]
		print "The maximum temperature is %s celsius"%item["high_celsius"]
		print "The minimum temperature is %s celsius"%item["low_celsius"]
		print "The condition is : %s"%item["condition"]

find_weather(raw_input("Enter a location to fetch weather report: "))
	
	
