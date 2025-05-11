#!/bin/sh

options="Shutdown\nReboot\nSuspend\nHibernate\nLock"

chosen=$(echo -e "$options" | rofi -dmenu -i -p ' ')

case "$chosen" in
    "Reboot") 
        systemctl reboot ;;
    "Shutdown") 
        systemctl poweroff ;;
    "Sleep") 
        systemctl sleep ;;
    "Suspend")
        systemctl suspend ;;
    "Lock") 
        exec hyprlock ;;
esac
