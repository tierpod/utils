#!/usr/bin/env bash
# modes:
# * gtf 1920 1080 60
# * cvt 1920 1080 60
# * http://www.mythtv.org/wiki/Modeline_Database#EDID_Modelines_.28Data_from_your_Monitor.29

xrandr --newmode "1920x1080_cvt" 138.500 1920 1968 2000 2080 1080 1083 1088 1111 +hsync -vsync
xrandr --addmode VGA1 "1920x1080_cvt"
xrandr --output VGA1 --mode "1920x1080_cvt"
