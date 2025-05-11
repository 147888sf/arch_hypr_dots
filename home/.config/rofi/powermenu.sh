#!/bin/sh

options="Shutdown\nReboot\nSuspend\nHibernate\nLock"

chosen=$(echo -e "$options" | rofi -dmenu -i -p ' ')

case "$chosen" in
    "Reboot") 
        systemctl reboot ;;
    "Shutdown") 
        systemctl poweroff ;;
    "Suspend") 
        systemctl suspend ;;
    "Hibernate")
        systemctl hibernate ;;
    "Lock") 
        exec hyprlock ;;
esac
