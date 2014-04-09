# Утилиты общего назначения
Для упрощения работы с linux

## minimal-profile.sh
Минимальный backup профиля. Архивирует указанные директории в ~/Backup/minimal-profile/

Опции: -p|--password

Зависимости: p7zip

## monitors.sh
Управление двумя мониторами.

## mount-gui.py
Подключение сетевого диска с использованием пароля.

Использование: добавить в /etc/fstab строку для подключения сетевого диска, например (заменить USERNAME на имя учётной записи):
```shell
//server/disk    /home/user/Disk   cifs    user,username=USERNAME,iocharset=utf8,noauto 0 0
```
Затем запустить mount-gui.py. В результате - отобразится окно ввода пароля, используемый для подключения сетевого диска. Скрипт опробован в сети с Active Directory для монтирования сетевого диска.

Зависимости: zenity

## nmap_scan_net.py
Надстройка над nmap -sP - форматирует вывод в удобный формат.

Зависимости: nmap

## pidgin-sort-blist.py
Сортирует ~/.purple/blist.xml и сворачивает все группы.

## xfce-switch-theme.sh

## nautilus-scripts
Скрипты для nautilus (после установки появляются в nautilus по правой кнопке мыши - сценарии)

Установить все скрипты:
```shell
cd nautilus-scripts
for i in *; do ln -s "$(readlink -f "$i")" "$HOME/.gnome2/nautilus-scripts/"; done
```
