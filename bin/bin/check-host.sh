#!/bin/sh
# getopts tutorials:
# * http://wiki.bash-hackers.org/howto/getopts_tutorial
# * http://rsalveti.wordpress.com/2007/04/03/bash-parsing-arguments-with-getopts/

# Settings
EXEC=false
EXEC_CMD='echo service networking restart'
LOG_FILE='check-host.log'
SLEEP_TIME=10



# Functions
help() {
	echo "Usage: $0 [-e] hostname"
}

check_host_notify() {
	if ping -c 1 $HOST > /dev/null; then
		notify-send -i 'dialog-ok-apply' 'Host online' "Host $HOST online"
		break
	fi
}

check_host_exec() {
	DATE=$(date -R)
	if ping -c 1 $HOST > /dev/null; then
		# ping successfull
		echo "$DATE ping succesfull"
	else
		# ping failure
		echo "$DATE ping failure"
		$EXEC_CMD
	fi
}

# Parse arguments
while getopts ':he' OPT; do
	case $OPT in
		h)
			help
			exit 1
			;;
		e)
			echo "Enable command execution on ping failure: $EXEC_CMD"
			EXEC=true
			;;
		?)
			help
			exit 1
			;;
	esac
done

# Extract last argument
shift $(( OPTIND - 1 )) && HOST=$1

if [ -z "$HOST" ]; then
	help
	exit 1
fi

while true; do
	if $EXEC; then
		check_host_exec >> $LOG_FILE
	else
		check_host_notify
	fi
	sleep $SLEEP_TIME
done
