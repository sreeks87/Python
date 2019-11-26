#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import smtplib
from data_onward import dataon
from data_onward import dataret
url="http://www.ksrtconline.com/KERALAOnline/advanceBooking.do"
cookies = {'JSESSIONID':''	}
def send_mail_now(send_msg_lst):
	try:
		fromaddr = 'removedaddress'
		toaddrs  = 'removedaddress'
		# msg = send_msg
		# Credentials (if needed)
		username = 'removedaddress'
		password = 'removedpassword'

		# The actual mail send
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(username,password)
		server.sendmail(fromaddr, toaddrs, send_msg_lst)
		server.quit()
		print("Mail sent with bus details successfully!!!")
	except Exception as e:
		print (e)
def onward():
	print('Processing inward')
	soup = BeautifulSoup(requests.post(url, data=dataon, cookies=cookies).content,'html.parser')
	process_soup(soup)
def ret():
	print('Processing return')
	soup = BeautifulSoup(requests.post(url, data=dataret, cookies=cookies).content,'html.parser')
	# print (soup.encode('cp437', errors='replace'))
	process_soup(soup)
def process_soup(soup):
	msg_array=""
	divTag = soup.find_all("a", {"class":"bookbtn"})
	# print(divTag)
	for tag in divTag:

		#print(tag.encode('cp437', errors='replace'))
		# for element in tag.find_all("li"):
		pData = str(tag.get('onclick'))
		params = pData.split('\'')
		available = params[5]
		if int(available) >0:
			req = params[1]
			req = req.split(",")
			bus_name = req[2]
			bus_time = req[5]
			bus_st = req[8]
			bus_des = req[9]
			bus_key = req[10]
			bus_src_time = req[12]
			send_msg = 'Tickets available for ' + bus_st + 'to '+ bus_des +'\n'
			msg_array = msg_array +"\n" +send_msg + "\n"
			msg_array = msg_array +"\n----------------------------------\n"
			send_msg2 = '''Details
			Bus Name: %s \n
			Bus time: %s \n
			Bus starting time : %s \n
			Destination : %s \n
			Key : %s \n
			Detination time : %s \n
			Seats Available : %s''' %(bus_name,bus_time,bus_st,bus_des,bus_key,bus_src_time,available)
			msg_array = msg_array + send_msg2
	if msg_array:
		send_mail_now(msg_array)
onward()
ret()
