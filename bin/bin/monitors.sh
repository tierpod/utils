#!/bin/sh

TITLE='Управление мониторами'
GUI='Графическое меню'
PRIMARY='DVI-I-1'
SECONDARY='VGA-0'

# Режимы
MIRROR='Режим mirror'
PRIMARY_LEFT='Основной монитор слева'
PRIMARY_RIGHT='Основной монитор справа'
PRIMARY_OFF='Выключить основной экран'

# Переключение режимов
mirror() {
	xrandr --auto
	nofity-send -i 'display' "$TITLE" "Выключен монитор: <b>$MIRROR</b>"
}

primary_left() {
	xrandr --auto
	xrandr --output $PRIMARY --left-of $SECONDARY
	xrandr --output $PRIMARY --primary
	notify-send -i 'display' "$TITLE" "Включен режим: <b>$PRIMARY_LEFT</b>"
}

primary_right() {
	xrandr --auto
	xrandr --output $PRIMARY --right-of $SECONDARY
	xrandr --output $PRIMARY --primary
	notify-send -i 'display' "$TITLE" "Включен режим: <b>$PRIMARY_RIGHT</b>"
}

primary_off() {
	xrandr --auto
	xrandr --output $PRIMARY --off
	notify-send -i 'display' "$TITLE" "Выключен монитор: <b>$PRIMARY_OFF</b>"
}

# Основная часть
help() {
	echo "Usage: $0 [option] [--sleep]"
	echo " option: -m, -pl, -pr, -poff, -gui ($MIRROR, $PRIMARY_LEFT, $PRIMARY_RIGHT, $PRIMARY_OFF, $GUI)"
	echo " switch: --sleep"
}

case "$1" in
	-m)
		[ "$2" == '--sleep' ] && sleep 5
		mirror
		;;
	-pl)
		[ "$2" == '--sleep' ] && sleep 5
		primary_left
		;;
	-pr)
		[ "$2" == '--sleep' ] && sleep 5
		primary_right
		;;
	-poff)
		[ "$2" == '--sleep' ] && sleep 5
		primary_off
		;;
	-gui)
		MODE=$(zenity --list --title="$TITLE" \
			--text="Основной: <b>$PRIMARY</b>, дополнительный: <b>$SECONDARY</b>\nВыберите режим работы" \
			--column='№' --column='Режимы работы' \
			'1' "$MIRROR" '2' "$PRIMARY_LEFT" '3' "$PRIMARY_RIGHT" '4' "$PRIMARY_OFF")
		case "$MODE" in
			1) mirror ;;
			2) primary_left ;;
			3) primary_right ;;
			4) primary_off ;;
		esac
		;;
	*)
		help
		;;
esac
