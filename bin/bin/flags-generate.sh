#!/usr/bin/env bash
# Origin: http://www.linuxhub.ru/viewtopic.php?f=23&t=459&p=1865
# Author: ZEN

# Фон изображения
bg="transparent"
# Цвет текста
fg="#000000"
# Имя или полный путь к шрифту
font=/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf
# Размер шрифта
font_size=17
# Директорая назначения
dpath="/tmp"
# Размер картинки ( ширина и высота )
image_size="24x24"
# Список раскладок, для zz будет использован знак "?"
l_array=("ru" "us")
# Пробегаем в цикле по массиву
for i in ${l_array[@]} 
do 
	# Помещаем имя раскладки и делаем заглавным первую букву
	TEXT="${i[@]^}"
	# Создаем в директории $dpath картинку 
	convert -size $image_size xc:$bg \
		-font $font \
		-fill $fg -antialias -pointsize $font_size -gravity center \
		-draw "text 0,1 $TEXT" "$dpath/$i.png"
done

exit 0
