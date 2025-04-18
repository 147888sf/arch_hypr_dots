import os
import subprocess
import pathlib

file_dir = pathlib.Path(__file__).parent.resolve()
home = os.getenv("HOME")

waybar_css = f'{home}/.config/waybar/style.css'
wallpapers_conf = f'{home}/.config/hypr/wallpapers.conf'
hyprpaper_conf = f'{home}/.config/hypr/hyprpaper.conf'
multilib_conf = '/etc/pacman.conf'



# Waybar config
if not os.access(waybar_css, os.R_OK | os.W_OK):
    os.system(f'sudo chown $USER:$USER {waybar_css} && chmod 644 {waybar_css}')

file = open(waybar_css, 'rb')
content = file.read().decode()
file.close()
file = open(waybar_css, 'wb')
file.write(content.replace('$HOME',home).encode())
file.close()



# Walpaper set
image = f'{home}/Wallpapers/wallpaper.jpg'

os.system(f'wal -i {image}')

if not os.access(wallpapers_conf, os.R_OK | os.W_OK):
    os.system(f'sudo chown $USER:$USER {wallpapers_conf} && chmod 644 {wallpapers_conf}')

file = open(wallpapers_conf,'wb')
file.write(f'$wallpaper = {image}'.encode())
file.close()

if not os.access(hyprpaper_conf, os.R_OK | os.W_OK):
    os.system(f'sudo chown $USER:$USER {hyprpaper_conf} && chmod 644 {hyprpaper_conf}')

file = open(hyprpaper_conf,'wb')
file.write(f'preload = {image}\nwallpaper = , {image}'.encode())
file.close()



# Multilib enable
try:
    if not os.access(multilib_conf, os.R_OK | os.W_OK):
        os.system(f'sudo chown $USER:$USER {multilib_conf} && chmod 644 {multilib_conf}')

    file = open(multilib_conf, 'rb')
    content = file.read().decode()
    file.close()
    file = open(multilib_conf, 'wb')
    file.write(content.replace('#[multilib]\n#Include = /etc/pacman.d/mirrorlist','[multilib]\nInclude = /etc/pacman.d/mirrorlist').encode())
    file.close()
except:
    pass



# Screenshare
os.system('systemctl --user enable --now pipewire pipewire-pulse wireplumber')



# Network manager
os.system('sudo systemctl enable NetworkManager.service')



# Reboot
dialog = input('Reboot? (recomended) [Y/n]: ')
if dialog == '' or dialog.lower() == 'y':
    os.system('sudo reboot')