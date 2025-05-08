from modules.install_packages import install_packages
from modules.install_homefiles import install_homefiles
from modules.post_install import post_install
import os
import subprocess

def cmdrun(command, cwd):
    try:
        if cwd:
            return subprocess.run(command, shell=True, cwd=cwd, check=True, text=True)
        else:
            return subprocess.run(command, shell=True, check=True, text=True)
    except subprocess.CalledProcessError:
        pass

def dialog(text: str, default_true: bool):
    dialog = input(f'{text} ({'Y/n' if default_true else 'y/N'}): ')
    if dialog.lower() == 'y':
        return True
    elif dialog == '':
        if default_true:
            return True
        else:
            return False
    else:
        return False

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

for i, x in enumerate(drivers):
    print(f'{i+1}: {x}')

while 1:
    try:
        gpu_type = int(input('Enter your GPU manifacturer to install drivers: '))
        if gpu_type-1 in [i for i, x in enumerate(drivers)]:
            selected_drivers = drivers[[x for i, x in enumerate(drivers)][gpu_type-1]]
            break
    except:
        pass

do_ly_dm = dialog('Do you want to install Ly DM?', True)
do_reboot = dialog('Do you want to reboot after install?', True)


print(r'''
          ___         _        _ _ _                                 
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __  __ _ _ _ _  _ 
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \/ _` | '_| || |
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\__,_|_|  \_,_|
                                         |___/  |_|                  
''')

cmdrun('git clone --depth 1 https://aur.archlinux.org/paru-bin.git', os.path.expanduser('~'))
cmdrun('makepkg -si --noconfirm', f'{os.path.expanduser('~')}/paru-bin')
cmdrun('sudo rm -rf ~/paru-bin')

print(r'''
          ___         _        _ _ _                           _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __  __ _ __| |____ _ __ _ ___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \/ _` / _| / / _` / _` / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\__,_\__|_\_\__,_\__, \___/__/
                                         |___/  |_|                    |___/
''')

install_packages(selected_drivers, do_ly_dm)

print(r'''
          ___         _        _ _ _                _     _    __ _ _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   __| |___| |_ / _(_) |___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | / _` / _ \  _|  _| | / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | \__,_\___/\__|_| |_|_\___/__/
                                         |___/
''' )

install_homefiles()

print(r'''
          ___        _     _         _        _ _                           _
         | _ \___ __| |_  (_)_ _  __| |_ __ _| | |  _ __ _ _ ___  __ ___ __| |_  _ _ _ ___ ___
         |  _/ _ (_-<  _| | | ' \(_-<  _/ _` | | | | '_ \ '_/ _ \/ _/ -_) _` | || | '_/ -_|_-<
         |_| \___/__/\__| |_|_||_/__/\__\__,_|_|_| | .__/_| \___/\__\___\__,_|\_,_|_| \___/__/
                                                   |_|
''')

post_install(do_reboot, do_ly_dm)
