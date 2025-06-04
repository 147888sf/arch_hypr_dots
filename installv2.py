from modules.install_packages import install_packages
from modules.install_homefiles import install_homefiles
from modules.post_install import post_install
from tools.selecttools import bool_selection, list_selection
import os
import subprocess

log_file = open('log.txt', 'w')
log_file.write('')
log_file.close()

def log(str):
    log_file = open('log.txt', 'ab')
    log_file.write((str+'\n').encode())
    log_file.close()

def lprint(str):
    print(str)
    log(str)

def cmdrun(command, cwd):
    try:
        output = subprocess.run(command, shell=True, cwd=cwd, check=True, text=True, capture_output=True)
        log(output.stdout)
    except subprocess.CalledProcessError:
        pass

lprint(r'''
          ___         _        _ _ _                                 
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __  __ _ _ _ _  _ 
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \/ _` | '_| || |
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\__,_|_|  \_,_|
                                         |___/  |_|                  
''')

# cmdrun('sudo rm -rf ~/paru-bin', os.path.expanduser('~'))
# cmdrun('git clone --depth 1 https://aur.archlinux.org/paru-bin.git', os.path.expanduser('~'))
# cmdrun('makepkg -si --noconfirm', f'{os.path.expanduser('~')}/paru-bin')
# cmdrun('sudo rm -rf paru-bin', os.path.expanduser('~'))

drivers = {
    'Nvidia': [
        'nvidia',
        'nvidia-utils',
        'lib32-nvidia-utils',
        'vulkan-icd-loader',
        'lib32-vulkan-icd-loader'
    ],

    'AMD' : [
        'mesa',
        'lib32-mesa',
        'vulkan-radeon',
        'lib32-vulkan-radeon',
        'libva-mesa-driver',
        'lib32-libva-mesa-driver',
        'mesa-vdpau',
        'lib32-mesa-vdpau'
    ],

    'Intel': [
        'mesa',
        'lib32-mesa',
        'vulkan-intel',
        'lib32-vulkan-intel',
        'intel-media-sdk',
        'libva-intel-driver',
        'lib32-libva-intel-driver'
    ],
    
    'Do not install GPU driver': [

    ]
}

selected_drivers = drivers[[x for x in drivers][list_selection('Select GPU drivers to install', drivers)]]
do_ly_dm = bool_selection('Do you want to install Ly DM?', True)
do_reboot = bool_selection('Do you want to reboot after install?', True)

lprint(r'''
          ___         _        _ _ _                           _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __  __ _ __| |____ _ __ _ ___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \/ _` / _| / / _` / _` / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\__,_\__|_\_\__,_\__, \___/__/
                                         |___/  |_|                    |___/
''')

install_packages(selected_drivers, do_ly_dm)

lprint(r'''
          ___         _        _ _ _                _     _    __ _ _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   __| |___| |_ / _(_) |___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | / _` / _ \  _|  _| | / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | \__,_\___/\__|_| |_|_\___/__/
                                         |___/
''' )

install_homefiles()

lprint(r'''
          ___        _     _         _        _ _                           _
         | _ \___ __| |_  (_)_ _  __| |_ __ _| | |  _ __ _ _ ___  __ ___ __| |_  _ _ _ ___ ___
         |  _/ _ (_-<  _| | | ' \(_-<  _/ _` | | | | '_ \ '_/ _ \/ _/ -_) _` | || | '_/ -_|_-<
         |_| \___/__/\__| |_|_||_/__/\__\__,_|_|_| | .__/_| \___/\__\___\__,_|\_,_|_| \___/__/
                                                   |_|
''')

post_install(do_reboot, do_ly_dm)

cmdrun('echo z', os.path.expanduser('~'))
