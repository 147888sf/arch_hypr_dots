#!/bin/sh

options="Shutdown\nReboot\nSleep\nLock"

chosen=$(echo -e "$options" | rofi -dmenu -i -p ' ')

case "$chosen" in
    "Reboot") 
        systemctl reboot ;;
    "Shutdown") 
        systemctl poweroff ;;
    "Sleep") 
        systemctl sleep ;;
    "Lock") 
        exec hyprlock ;;
esac
