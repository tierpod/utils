# Linux утилиты

## Установка
Для установки удобнее использовать программу
[stow](https://github.com/tierpod/dotfiles/wiki/stow):

```
sudo apt-get install stow
cd utils
stow dir #сделает символическую ссылку в домашнюю директорию
```

# bin

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

## pulseaudio-combined.sh
С помощью этого метода можно записать разговоры skype или других voip клиентов.
Ведётся запись как входящего с микрофона звука (ваша речь), так и исходящего со
звуковой карты звука (речь собеседника).

Создаёт виртуальное устройство, куда направляет исходящий и входящий звук.
Затем с виртуального устройства можно производить запись, например, с помощью
программы gtk-recordmydesktop.

* Рекомендуемые зависимости: pavucontrol, gtk-recordmydesktop

## resolution.sh
Добавляет разрешение экрана, отсутвующее в списке xrandr. Можно использовать
вместе с lightdm на этапе его запуска.

## git-change-email.sh
Взято [тут](https://help.github.com/articles/changing-author-info/). Изменяет старый
email на новый во всей истории в проекте. Использовать __крайне__ осторожно и только
в экстренных случаях - вся совместная работа над репозеторием будет потеряна, всем
нужно будет заново скачивать репозиторий.



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



# squid-scripts
Вспомогательные скрипты для парсинга логов squid-а.
