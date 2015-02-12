#!/usr/bin/python
import datetime, time, urllib, urllib2
import socket

# Sends yo to all subscribed accounts
def yo_all():
	api_token = "b931eed2-1c90-4a53-8415-2263c48322ff"
	data = urllib.urlencode({'api_token': api_token})
	request = urllib2.Request("http://api.justyo.co/yoall/", data)
	response = urllib2.urlopen(request)
	return 0

# Gets current time in HH-MM format (20:22)
def currentTime():
	return time.strftime("%H:%M")

# Main program loop
def main():
	notificationTimes = ["07:20", "07:30" "11:10", "13:10", "15:12", "16:12", "17:00", "19:00",  "20:00",  "21:00",  "21:30"]
	lastCheck = ""
	
	while True:
		print currentTime()
		
		if currentTime() != lastCheck:	
			if currentTime() in notificationTimes:
				print yo_all()
				lastCheck = currentTime()
		
		time.sleep(20)

# Main loop for debugging
def main_debug():
	# notificationTimes = ["7:20", "7:30" "11:10", "13:10", "15:12", "16:12", "17:00", "19:00",  "20:00",  "21:00",  "21:30"]
	# lastCheck = ""
	
	while True:
		print currentTime()
		
		if currentTime() != "hello":	
			if currentTime(): # in notificationTimes:
				print "yo_all()"
				# lastCheck = currentTime()
		
		time.sleep(3)
		
if socket.gethostname() == "Renzos-MacBook-Pro.local":
	main_debug()
else:
	main()