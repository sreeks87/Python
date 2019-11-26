import requests,os,hashlib,sys
from bs4 import BeautifulSoup as Soup
from urllib.parse import unquote
def get_hash(name):
	readsize = 64 * 1024
	with open(name, 'rb') as f:
	    size = os.path.getsize(name)
	    data = f.read(readsize)
	    f.seek(-readsize, os.SEEK_END)
	    data += f.read(readsize)
	return hashlib.md5(data).hexdigest()
def downloadSub(full_path,filename):
	unq_path = unquote(full_path)
	header = {'user-agent': 'SubDB/1.0 (subtitler/0.1)'}
	dwl_url = "http://api.thesubdb.com/?action=download&hash="+get_hash(unq_path)+"&language=en"
	#dwl_url = "http://api.thesubdb.com/?action=download&hash=f22f52be15d20caca01e518346873daf&language=en"
	#print(dwl_url)
	r = requests.get(dwl_url,headers=header)
	if r.status_code == 200:
		if not (os.path.isfile((os.path.dirname(unq_path)+"\\"+ filename+".srt"))):
			with open(os.path.dirname(unq_path)+"\\"+ filename+".srt", "wb") as subtitle:
				subtitle.write(r.content)
			print(filename+".srt " + "subtitle file saved at " + (os.path.dirname(unq_path)))
		else:
			raise Exception("[Err 03]:Subtitle file already exist")
def getInfo():
	try:
		s = requests.Session()
		s.auth = ('', 'password')# Username is blank, just provide the password
		'''r = s.get('http://localhost:8080/requests/status.xml', verify=False)
	    #print(r.text)	
	    soup = Soup(r.text,"html.parser")
	    for tag in soup.find_all('info'):
	    	if (tag.get('name') == "filename"):
	    		filename = tag.string
	    		print(filename)'''
		p = s.get('http://localhost:8080/requests/playlist.xml', verify=False)
		play = Soup(p.text,"html.parser")
		for leaf in play.find_all('leaf'):
			if (leaf.get('current') == "current"):
				full_path = leaf.get('uri')
				filename = leaf.get('name')
		if (full_path and filename):
			downloadSub(full_path[8:],filename)
		else:
			raise Exception("[Err 02]:Filename can't be null. Please make sure VLC is playing video.") 
	except Exception as e:
		print("Error occured -\n"+str(e))
		sys.exit(0)
getInfo()