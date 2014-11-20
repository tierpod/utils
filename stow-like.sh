#!/usr/bin/env bash

CFG='.stowrc'

function parse_cfg() {
	if [[ -e $CFG ]]; then
		VERBOSE=$(grep 'verbose' $CFG)
		TARGET=$(awk -F "=" '/target/ {print $2}' $CFG)
	else
		VERBOSE=""
		TARGET=""
		echo "$CFG not found"
	fi
}

function copy_files() {
	echo cp -R $1 $2 $3
}

if [[ "$1" != "" ]]; then
	parse_cfg
	for DIR in *
	do
		copy_files $VERBOSE $1/$DIR $TARGET
	done
else
	echo "Select subdirectory"
fi
