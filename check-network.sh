#!/usr/bin/env bash

HOST='192.168.1.1'
FAIL_CMD='echo CMD PING ERROR'
DATE=$(date -R)

function check_network() {
	ping -c 1 $HOST > /dev/null
	if [[ $? == 0 ]]
	then
		# Пинг успешный
		echo "$DATE ping ok"
	else
		# Пинг неудачный
		echo "$DATE ping error"
		$FAIL_CMD
	fi
}

check_network >> /tmp/check_network.log
