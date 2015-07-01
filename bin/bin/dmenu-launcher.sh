#!/usr/bin/env bash

DMENU_CMD='dmenu.xft -b -l 20 -nb #CECECE -sb #398ee7 -nf #212121 -sf #212121 -fn Cuprum-12'
SUBMODULES=(pidgin desktop-files run clibpoard test)

ACTION=$(for i in ${SUBMODULES[*]}; do echo $i; done | $DMENU_CMD)

case "$ACTION" in
	${SUBMODULES[0]})
		pidgin-start-conv.py "$(pidgin-start-conv.py -p | $DMENU_CMD -p $ACTION)"
		;;
	${SUBMODULES[1]})
		cd /usr/share/applications/
		gnome-open $(ls /usr/share/applications/ | $DMENU_CMD -p $ACTION)
		;;
	${SUBMODULES[2]})
		IFS=:
		BIN=$(stest -flx $PATH | sort -u)
		IFS=' '
		echo $BIN | $DMENU_CMD -p $ACTION | /bin/sh &
		;;
	${SUBMODULES[3]})
		cat $HOME/.config/phrases.conf | $DMENU_CMD -p $ACTION
		;;
	${SUBMODULES[4]})
		echo '3'
		;;
esac
