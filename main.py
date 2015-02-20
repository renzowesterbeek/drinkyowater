#!/usr/bin/python
import datetime, time, urllib, urllib2
import socket

# Sends yo to all subscribed accounts with DRINKYOWATER account
def yo_all():
	api_token = "b931eed2-1c90-4a53-8415-2263c48322ff"
	data = urllib.urlencode({'api_token': api_token})
	request = urllib2.Request("http://api.justyo.co/yoall/", data)
	response = urllib2.urlopen(request)
	return 0

# Returns list with times based on day
def getListOfTheDay():
	w = time.strftime("%w")
	if w == 0 or w == 6: # Weekend
		return ["10:30", "12:30", "13:30", "14:30", "16:30", "18:30", "20:30", "21:30"]
	else: # Weekday
		return ["07:20", "07:30", "11:10", "13:10", "15:12", "16:12", "17:00", "19:00",  "20:00",  "21:00",  "21:30"]

# Gets current time in HH-MM format (20:22)
def currentTime():
	return time.strftime("%H:%M")

# Main program loop
def main():
	lastCheck = ""
	
	while True:
		print currentTime()
		
		if currentTime() != lastCheck:	
			if currentTime() in getListOfTheDay():
				print yo_all()
				lastCheck = currentTime()
		
		time.sleep(20)
	
	return 0

# Main loop for debugging
def main_debug():
	# lastCheck = ""
	
	while True:
		print currentTime()
		
		if currentTime() != "lastCheck":	
			if currentTime(): # in getListOfTheDay():
				print "yo_all()"
				# lastCheck = currentTime()
		
		print getListOfTheDay()
		time.sleep(3)
	
	return 0

# Runs debug loop on local machine, main loop on remote		
if socket.gethostname() == "Renzos-MacBook-Pro.local":
	main_debug()
else:
	main()