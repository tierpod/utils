#!/usr/bin/env bash

PWD=$(pwd)
DMENU_CMD="dmenu.xft -b -l 20 -nb #CECECE -sb #398ee7 -nf #212121 -sf #212121 -fn UbuntuMono-12"
SUBMODULES="pidgin desktop-files run vnc test"

ACTION=$(for i in $SUBMODULES; do echo $i; done | $DMENU_CMD)

case "$ACTION" in
	pidgin)
		cd $PWD
		./pidgin-start-conv.py "$(./pidgin-start-conv.py -p | $DMENU_CMD)"
		;;
	desktop-files)
		cd /usr/share/applications/ && gnome-open $(ls /usr/share/applications/ | $DMENU_CMD)
		;;
	run)
		dmenu_run -b -l 20 -nb '#CECECE' -sb '#398ee7' -nf '#212121' -sf '#212121'
		;;
	vnc)
		echo '2'
		;;
	test)
		echo '3'
		;;
esac
