#!/bin/sh

options="Shutdown\nReboot\nSleep\nHibernate\nLock"

chosen=$(echo -e "$options" | rofi -dmenu -i -p ' ')

case "$chosen" in
    "Reboot") 
        systemctl reboot ;;
    "Shutdown") 
        systemctl poweroff ;;
    "Sleep") 
        systemctl sleep ;;
    "Hibernate")
        systemctl hibernate
    "Lock") 
        exec hyprlock ;;
esac
