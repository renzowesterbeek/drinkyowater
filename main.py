#!/usr/bin/python
import datetime, time, urllib, urllib2
import socket, sys

# Sends yo to all subscribed accounts with DRINKYOWATER account
def yo_all():
	api_token = "b931eed2-1c90-4a53-8415-2263c48322ff"
	data = urllib.urlencode({'api_token': api_token})
	request = urllib2.Request("http://api.justyo.co/yoall/", data)
	response = urllib2.urlopen(request)
	return 0

# Returns list with times based on day
def get_list_of_the_day():
	w = time.strftime("%w")
	if w == "0" or w == "6": # Weekend
		return ["10:30", "12:30", "13:30", "14:30", "16:30", "18:30", "20:30", "21:30"]
	else: # Weekday
		return ["07:20", "07:30", "11:10", "13:10", "15:12", "16:12", "17:00", "19:00",  "20:00",  "21:00",  "21:30"]

# Gets current time in HH-MM format (20:22)
def current_time():
	return time.strftime("%H:%M")

# Main program loop
def main():
	last_time_check = ""
	
	while True:
		if current_time() != last_time_check:	
			if current_time() in get_list_of_the_day():
				print yo_all()
				last_time_check = current_time()
		
		time.sleep(20)
	return 0

# Main loop for debugging
def main_debug():
	# last_time_check = ""
	
	while True:
		print current_time()
		if current_time() != "last_time_check":	
			if current_time(): # in get_list_of_the_day():
				print "yo_all()"
				# last_time_check = current_time()
		
		print get_list_of_the_day()
		time.sleep(3)
	return 0

# Runs debug loop on OSX (local) machine, main loop on LINUX (remote)	
if sys.platform == "darwin":
	main_debug()
else:
	main()