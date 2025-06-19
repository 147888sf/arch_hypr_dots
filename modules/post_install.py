import os

from tools.log_tools import log_cmd


def post_install(do_reboot, do_ly_dm):
    home = os.getenv("HOME")

    waybar_css = f"{home}/.config/waybar/style.css"
    wallpapers_conf = f"{home}/.config/hypr/wallpapers.conf"
    hyprpaper_conf = f"{home}/.config/hypr/hyprpaper.conf"
    multilib_conf = "/etc/pacman.conf"

    # Waybar config
    if not os.access(waybar_css, os.R_OK | os.W_OK):
        log_cmd(f"sudo chown $USER:$USER {waybar_css} && chmod 644 {waybar_css}")

    file = open(waybar_css, "rb")
    content = file.read().decode()
    file.close()
    file = open(waybar_css, "wb")
    file.write(content.replace("$HOME", home).encode())
    file.close()

    # Walpaper set
    image = f"{home}/Wallpapers/urban.png"

    log_cmd(f"wal -i {image}")

    if not os.access(wallpapers_conf, os.R_OK | os.W_OK):
        log_cmd(
            f"sudo chown $USER:$USER {wallpapers_conf} && chmod 644 {wallpapers_conf}"
        )

    file = open(wallpapers_conf, "wb")
    file.write(f"$wallpaper = {image}".encode())
    file.close()

    if not os.access(hyprpaper_conf, os.R_OK | os.W_OK):
        log_cmd(
            f"sudo chown $USER:$USER {hyprpaper_conf} && chmod 644 {hyprpaper_conf}"
        )

    file = open(hyprpaper_conf, "wb")
    file.write(f"preload = {image}\nwallpaper = , {image}".encode())
    file.close()

    # Multilib enable
    try:
        if not os.access(multilib_conf, os.R_OK | os.W_OK):
            os.system(
                f"sudo chown $USER:$USER {multilib_conf} && chmod 644 {multilib_conf}"
            )

        file = open(multilib_conf, "rb")
        content = file.read().decode()
        file.close()
        file = open(multilib_conf, "wb")
        file.write(
            content.replace(
                "#[multilib]\n#Include = /etc/pacman.d/mirrorlist",
                "[multilib]\nInclude = /etc/pacman.d/mirrorlist",
            ).encode()
        )
        file.close()
    except Exception:
        pass

    # Screenshare & audio
    log_cmd("sudo systemctl --user enable --now pipewire pipewire-pulse wireplumber")

    # Network manager
    log_cmd("sudo systemctl enable NetworkManager.service")

    # Default dark mode
    log_cmd("gsettings set org.gnome.desktop.interface gtk-theme Adwaita-dark")
    log_cmd("gsettings set org.gnome.desktop.interface color-scheme prefer-dark")
    log_cmd("gsettings set org.gnome.desktop.interface icon-theme Papirus")
    log_cmd(
        "gsettings set org.gnome.desktop.interface font-name 'Noto Sans Regular 11'"
    )

    # Ly dm
    if do_ly_dm:
        log_cmd("sudo systemctl enable ly")

    # Reboot
    if do_reboot:
        log_cmd("sudo reboot")
