#!/usr/bin/env bash

THEME=$(zenity --width="450" --height="200" --list \
		--title="Сменить тему" \
		--text="Выберите тему" \
		--column="Название" --column="Комментарий" \
		"Numix" "Тёмно-серая тема"\
		"Sky" "Светло-синяя тема" \
		"Numix-old" "Прежняя версия тёмно-серой темы" \
	)

EXITCODE=$?

case "$THEME" in
	Numix)
		xfconf-query -c xsettings -p /Net/ThemeName -s $THEME
		xfconf-query -c xsettings -p /Net/IconThemeName -s 'elementaryXubuntu'
		xfconf-query -c xfwm4 -p /general/theme -s $THEME
		xfconf-query -c xfce4-notifyd -p /theme -s $THEME
		;;
	Numix-old)
		xfconf-query -c xsettings -p /Net/ThemeName -s $THEME
		xfconf-query -c xsettings -p /Net/IconThemeName -s 'elementaryXubuntu'
		xfconf-query -c xfwm4 -p /general/theme -s $THEME
		xfconf-query -c xfce4-notifyd -p /theme -s $THEME
		;;
	Sky)
		xfconf-query -c xsettings -p /Net/ThemeName -s $THEME
		xfconf-query -c xsettings -p /Net/IconThemeName -s 'elementary-xfce'
		xfconf-query -c xfwm4 -p /general/theme -s $THEME
		xfconf-query -c xfce4-notifyd -p /theme -s $THEME
		;;
esac

[[ $EXITCODE == 0 ]] && notify-send -i "display" "Изменение темы" "Включена тема <b>$THEME</b>"
