#!/usr/bin/env bash

function check_host() {
	ping -c 1 $1 > /dev/null
	if [[ $? == 0 ]]; then
		notify-send -i "dialog-ok-apply" "Host online" "Host $1 online"
		break
	fi
}

if [[ -n "$1" ]]; then
	while true; do
		check_host $1
		sleep 60
	done
fi
