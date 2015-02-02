# Linux утилиты

## Установка
Для установки удобнее использовать программу
[stow](https://github.com/tierpod/dotfiles/wiki/stow):

```
sudo apt-get install stow
cd utils.git
stow dir #сделает символическую ссылку в домашнюю директорию
```

## Структура 3 директории, логически разделённые на модули.
В каждом из модулей
воссоздана структура каталогов, как файлы должны размещаться в домашней
директории

* [bin](#bin) - поддиректория bin (исполняемые файлы, утилиты) -> ~/bin/
* [kupfer-plugins](#kupfer-plugins) - плагины для kupfer
* [nautilus-scripts](#nautilus-scripts) - скрипты для nautilus

# bin

## dmenu-launcher.sh
Просто скрипт, обёртка над dmenu, позволяющая создавать подменю.

## check-host.sh
check-host.sh [-e] server
Пингует адрес (server) и в случае неудачи либо выводит сообщение с помощью
notify-send (если не указан параметр -e), либо выполняет комманду (переменная
EXEC_CMD).

Чтобы запускать скрипт по расписанию, нужно добавить его в cron:
* Запускает crontab -e
* Добавляем туда запись вида:

```bash
* * * * * /path/to/check-host.sh -e ipaddr
```

* Сохраняемся, выходим

### Примеры формата времени для cron

```bash
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

  *  *  *  *  * #каждую минуту
 */5 *  *  *  * #каждые 5 минут
  0 */5 *  *  * #каждые 5 часов
```

## backup-profile.sh
Создаёт резервную копию файлов, описанных внутри скрипта. Складывает архив в
~/Backup/minimal-profile/

* ~/.config/backup-profile.cfg переменные для bash, которые используются в
  скрипте (INCLUDE, EXCLUDE, ARC_FILE, ARC_FILE_P)
* Опции: -p|--password (создаёт 7z-архив, защищённый паролем)
* Зависимости: p7zip

## monitors.sh
Управление двумя мониторами (GUI).

## mount-gui.py
Подключение сетевого диска с использованием пароля (GUI).

### Использование
Добавить в /etc/fstab строку для подключения сетевого диска, например (заменить
USERNAME на имя учётной записи): 

```bash
//server/disk    /home/user/Disk   cifs    user,username=USERNAME,iocharset=utf8,noauto 0 0
```

Затем запустить mount-gui.py. В результате - отобразится окно ввода пароля,
используемого для подключения сетевого диска. Скрипт опробован в сети с Active
Directory для монтирования сетевого диска.

* Зависимости: zenity

## nmap_scan_net.py
Сканирование сети на наличие сетевого оборудования (компьютеров, принтеров и
прочего). Вызывает nmap -sP и форматирует вывод.

* Зависимости: nmap

## pidgin-sort-blist.py
Сортирует список контактов Pidgin-а (~/.purple/blist.xml) по имени и
сворачивает все группы. Перед использованием полностью выйти из pidgin-а, иначе
изменения не сохранятся.

## pidgin-start-conv.py
Получает всех пользователей из Pidgin (ключ -p), можно запустить беседу с
конкретным пользователем, указав его учётную запись сразу после скрипта. Можно
использовать с dmenu:

```bash
pidgin-start-conv.py "$(pidgin-start-conv.py -p | dmenu.xft -b -l 20 -i -fn 'UbuntuMono-12')"
```

## xfce-switch-theme.sh
Небольшой скрипт, позволяет переключаться между несколькими прописанными в
скрипте темами xfce, xfce-notifyd, xfwm, icons. Использую, чтобы переключаться
между дневной\ночной темой.

## pulseaudio-combined.sh
С помощью этого метода можно записать разговоры skype или других voip клиентов.
Ведётся запись как входящего с микрофона звука (ваша речь), так и исходящего со
звуковой карты звука (речь собеседника).

Создаёт виртуальное устройство, куда направляет исходящий и входящий звук.
Затем с виртуального устройства можно производить запись, например, с помощью
программы gtk-recordmydesktop.

* Рекомендуемые зависимости: pavucontrol, gtk-recordmydesktop

## flags-generate.sh
Генерирует картинки с текстом раскладок. Можно использовать в xfce, gnome и др.
для отображения текущей раскладки (так называемые флаги).

* Зависимости: imagemagick

# nautilus-scripts
Скрипты для nautilus. После установки появляются в nautilus по правой кнопке
мыши - сценарии.

## Установка всех скриптов

```bash
cd nautilus-scripts
for i in *; do ln -s "$(readlink -f "$i")" "$HOME/.gnome2/nautilus-scripts/"; done # Ubuntu 12.04
for i in *; do ln -s "$(readlink -f "$i")" "$HOME/.config/caja/scripts/"; done # Linux Mate 13
```

# kupfer-plugins
Плагины для лаунчера kupfer (http://engla.github.io/kupfer/).
Скопировать\сделать символическую ссылку в ~/.local/share/kupfer/plugins/

# resolution.sh
Добавляет разрешение экрана, отсутвующее в списке xrandr
