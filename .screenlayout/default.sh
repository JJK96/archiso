#!/bin/sh
xrandr --output HDMI2 --off --output HDMI1 --off --output DP1 --off --output eDP1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP2 --off
ln -sf ~/Pictures/BSOL.png ~/Pictures/active_lockscreen
~/.screenlayout/refresh.sh
