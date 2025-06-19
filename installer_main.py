import os

from modules.install_homefiles import install_homefiles
from modules.install_packages import install_packages
from modules.post_install import post_install
from tools.log_tools import clear_log, log_cmd, log_print
from tools.selection_tools import bool_selection, list_selection

clear_log()

log_print(r"""
          ___         _        _ _ _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __  __ _ _ _ _  _
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \/ _` | '_| || |
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\__,_|_|  \_,_|
                                         |___/  |_|
""")

log_cmd("sudo rm -rf ~/paru-bin")
log_cmd("git clone --depth 1 https://aur.archlinux.org/paru-bin.git")
log_cmd("makepkg -si --noconfirm", f"{os.path.expanduser('~')}/paru-bin")
log_cmd("sudo rm -rf paru-bin")

drivers = {
    "Nvidia": [
        "nvidia",
        "nvidia-utils",
        "lib32-nvidia-utils",
        "vulkan-icd-loader",
        "lib32-vulkan-icd-loader",
    ],
    "AMD": [
        "mesa",
        "lib32-mesa",
        "vulkan-radeon",
        "lib32-vulkan-radeon",
        "libva-mesa-driver",
        "lib32-libva-mesa-driver",
        "mesa-vdpau",
        "lib32-mesa-vdpau",
    ],
    "Intel": [
        "mesa",
        "lib32-mesa",
        "vulkan-intel",
        "lib32-vulkan-intel",
        "intel-media-sdk",
        "libva-intel-driver",
        "lib32-libva-intel-driver",
    ],
    "Do not install GPU driver": [],
}

selected_drivers = drivers[
    [x for x in drivers][list_selection("Select GPU drivers to install", drivers)]
]
do_backup = bool_selection("Do you want to backup config files?", True)
do_ly_dm = bool_selection("Do you want to install Ly DM?", True)
do_update_sysyem = bool_selection(
    "Do you want to update your system after install?", True
)
do_reboot = bool_selection("Do you want to reboot after install?", True)

log_print(r"""
          ___         _        _ _ _                           _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __  __ _ __| |____ _ __ _ ___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \/ _` / _| / / _` / _` / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\__,_\__|_\_\__,_\__, \___/__/
                                         |___/  |_|                    |___/
""")

install_packages(selected_drivers, do_ly_dm, do_update_sysyem)

log_print(r"""
          ___         _        _ _ _                _     _    __ _ _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   __| |___| |_ / _(_) |___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | / _` / _ \  _|  _| | / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | \__,_\___/\__|_| |_|_\___/__/
                                         |___/
""")

install_homefiles(do_backup)

log_print(r"""
          ___        _     _         _        _ _                           _
         | _ \___ __| |_  (_)_ _  __| |_ __ _| | |  _ __ _ _ ___  __ ___ __| |_  _ _ _ ___ ___
         |  _/ _ (_-<  _| | | ' \(_-<  _/ _` | | | | '_ \ '_/ _ \/ _/ -_) _` | || | '_/ -_|_-<
         |_| \___/__/\__| |_|_||_/__/\__\__,_|_|_| | .__/_| \___/\__\___\__,_|\_,_|_| \___/__/
                                                   |_|
""")

post_install(do_reboot, do_ly_dm)
