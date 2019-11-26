import unirest
import json
url = "https://twinword-sentiment-analysis.p.mashape.com/analyze/"
key = ""
content = "application/x-www-form-urlencoded"
accept = "application/json"
def sentiments(txt):
	response = unirest.post(url,
	  headers={
		"X-Mashape-Key": key,
		"Content-Type": content,
		"Accept": accept
	  },
	  params={
		"text": txt
	  }
	)
	data = json.loads(response.raw_body)
	print "The mood is %s " %(data["type"])
	

sentiments(raw_input("Enter the string to check the sentimenmts:"))