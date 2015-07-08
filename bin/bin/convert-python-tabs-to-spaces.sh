#!/bin/sh

convert() {
	find -name '*.py' -print | xargs -n 1 sed -i 's/\t/    /g'
}

read -p 'Convert all *.py tabs to spaces? ' answer

case "$answer" in
	[Yy]*)
		echo 'Convert tabs to spaces'
		convert
		;;
	*)
		echo 'Exit without convert'
		exit 1
		;;
esac
