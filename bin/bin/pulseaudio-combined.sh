#!/bin/bash
# * Создаём виртуальное null-sink устройство с названием combined (для того, чтобы в него перенаправить исходящий и входящий звук и уже потом записывать с него)
# * Через модуль loopback подключаем к этому виртуальному устройству:
#   * Монитор исходящего звука - для записи всего звука, что воспроизводит компьютер - браузер, скайп
#   * Источник входящего звука - для записи всего звука, что мы говорим а микрофон
# * Зайходим в pavucontrol, на вкладке Запись выбираем для программы gtk-recordmydesktop Monitor of null - чтобы записывать весь звук с виртуального устройства null
# 
# Смотрим все возможные output и input устройства:
# pactl list short | grep "output" | awk '{ print $2 }'
# pactl list short | grep "input"  | awk '{ print $2 }'

pactl load-module module-null-sink sink_name=combined
pactl load-module module-loopback sink=combined source=alsa_output.pci-0000_00_1b.0.analog-stereo.monitor
pactl load-module module-loopback sink=combined source=alsa_input.usb-046d_0825_A0DC4C60-02-U0x46d0x825.analog-mono

