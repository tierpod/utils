# Linux утилиты

## minimal-profile.sh
Создаёт резервную копию файлов, описанных внутри скрипта. Складывает архив в ~/Backup/minimal-profile/.
* Опции: -p|--password (создаёт 7z-архив, защищённый паролем)
* Зависимости: p7zip

## monitors.sh
Управление двумя мониторами (GUI).

## mount-gui.py
Подключение сетевого диска с использованием пароля (GUI).

### Использование
Добавить в /etc/fstab строку для подключения сетевого диска, например (заменить USERNAME на имя учётной записи):
```bash
//server/disk    /home/user/Disk   cifs    user,username=USERNAME,iocharset=utf8,noauto 0 0
```
Затем запустить mount-gui.py. В результате - отобразится окно ввода пароля, используемого для подключения сетевого диска. Скрипт опробован в сети с Active Directory для монтирования сетевого диска.
* Зависимости: zenity

## nmap_scan_net.py
Сканирование сети на наличие сетевого оборудования (компьютеров, принтеров и прочего). Вызывает nmap -sP и форматирует вывод.
* Зависимости: nmap

## pidgin-sort-blist.py
Сортирует список контактов Pidgin-а (~/.purple/blist.xml) по имени и сворачивает все группы. Перед использованием полностью выйти из pidgin-а, иначе изменения не сохранятся.

## xfce-switch-theme.sh
Небольшой скрипт, позволяет переключаться между несколькими прописанными в скрипте темами xfce, xfce-notifyd, xfwm, icons. Использую, чтобы переключаться между дневной\ночной темой.

## nautilus-scripts
Скрипты для nautilus. После установки появляются в nautilus по правой кнопке мыши - сценарии.

### Установка всех скриптов
```bash
cd nautilus-scripts
for i in *; do ln -s "$(readlink -f "$i")" "$HOME/.gnome2/nautilus-scripts/"; done
```

## pulseaudio-combined.sh
С помощью этого метода можно записать разговоры skype или других voip клиентов. Ведётся запись как входящего с микрофона звука (ваша речь), так и исходящего со звуковой карты звука (речь собеседника).

Создаёт виртуальное устройство, куда направляет исходящий и входящий звук. Затем с виртуального устройства можно производить запись, например, с помощью программы gtk-recordmydesktop.

* Рекомендуемые зависимости: pavucontrol, gtk-recordmydesktop

## flags-generate.sh
Генерирует картинки с текстом раскладок. Можно использовать в xfce, gnome и др. для отображения текущей раскладки (так называемые флаги).

* Зависимости: imagemagick
