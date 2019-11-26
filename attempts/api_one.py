from urllib2 import Request,urlopen,URLError
request = Request('http://www.google.com')
try:
	response = urlopen(request)
	data = response.read()
	print data
	kit = urlopen('http://placekitten.com/200/300')
	print kit.read()
	f = open('kitten.jpg','wb')
	f.write(kit.read())
	f.close()
	
except URLError,e:
	print "Oops!!!"
