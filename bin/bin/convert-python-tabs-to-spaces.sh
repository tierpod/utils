#!/usr/bin/env bash

function convert() {
	find -name "*.py" -print | xargs -n 1 sed -i 's/\t/    /g'
}

read -p "Convert all *.py tabs to spaces? " yn

case $yn in
	[Yy]*)
		convert
		;;
	[Nn]*)
		echo "Exit without convert"
		exit 0
		;;
	*)
		echo "Unknow answer: Y or N"
		exit 1
		;;
esac
