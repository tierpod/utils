#!/bin/sh

THEME=$(zenity --width='450' --height='200' --list \
		--title='Сменить тему' \
		--text='Выберите тему' \
		--column='Название' --column='Комментарий' \
		'Numix' 'Тёмно-серая тема' \
		'Sky' 'Светло-синяя тема' \
		'Numix-old' 'Прежняя версия тёмно-серой темы' \
		'greybird-mod' 'Новая тема' \
	)

RC=$?

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
	greybird-mod)
		xfconf-query -c xsettings -p /Net/ThemeName -s $THEME
		xfconf-query -c xsettings -p /Net/IconThemeName -s 'evolvere'
		xfconf-query -c xfwm4 -p /general/theme -s $THEME
		xfconf-query -c xfce4-notifyd -p /theme -s $THEME
esac

[ "$RC" -eq 0 ] && notify-send -i 'display' 'Изменение темы' "Включена тема <b>$THEME</b>"
