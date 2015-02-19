#!/bin/bash

function checkForUpdate {
	localSHA=$(git rev-parse HEAD)
	remoteSHA=$(git ls-remote git://github.com/renzowesterbeek/drinkyowater.git HEAD)
	
	remoteSHA10=${remoteSHA:0:10}
	localSHA10=${localSHA:0:10}
	
	echo $localSHA10
	echo $remoteSHA10
	
	if [ "$localSHA10" != "$remoteSHA10" ]; then
		echo "Updating application..."
		mainPID=$(pidof python main.py)
		kill $mainPID
		cd ..
		rm -rf drinkyowater
		git clone https://github.com/renzowesterbeek/drinkyowater.git
	fi
}

function main {
	while true; do
		echo "Checking"
		checkForUpdate
		sleep 300
	done
}

main