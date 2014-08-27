#!/usr/bin/env bash
# Try using getopts:
# * http://wiki.bash-hackers.org/howto/getopts_tutorial
# * http://rsalveti.wordpress.com/2007/04/03/bash-parsing-arguments-with-getopts/

# Start settings
EXEC="0"
EXEC_CMD="echo running exec command"
LOG_FILE="/var/log/check-host.log"

# Functions
function help() {
	echo "Usage: check-host.sh [-e] server"
}

function check_host() {
	ping -c 1 $1 > /dev/null
	if [[ $? == 0 ]]; then
		notify-send -i "dialog-ok-apply" "Host online" "Host $1 online"
		break
	fi
}

function check_host_exec() {
	DATE=$(date -R)
	ping -c 1 $1 > /dev/null
	if [[ $? == 0 ]]; then
		# Пинг успешный
		echo "$DATE ping succesfull"
	else
		# Пинг неудачный
		echo "$DATE ping failure"
		$EXEC_CMD
	fi
}

# Parse arguments
while getopts ":he" OPT; do
	case $OPT in
		h)
			help
			exit 1
			;;
		e)
			echo "Enable exec cmd"
			EXEC=1
			;;
		?)
			help
			exit 1
			;;
	esac
done

# Extract last argument
shift $(( OPTIND - 1 )) && SERVER=$1
echo $SERVER
echo $EXEC


# Main function
if [[ -n $SERVER ]]; then
	if [[ $EXEC == "0" ]]; then
		while true; do
			check_host $SERVER
			sleep 60
		done
	else
		check_host_exec $SERVER $EXEC_CMD >> $LOG_FILE
	fi
fi
