# Our website

http://79.134.218.62:5000/
Here you can find more details about the project

# For users

## What is this project?

This is my project of Arch Linux rice installer made using Python, Shell and my config files.

## Features of the project

- **Easy installation**: just run script, select how you like to use your system and wait.
- **Compatibility**: Works great on any PC or Laptop with Nvidia/Intel/Radeon GPU and any username
- **Modular stucture**: Everything works in separate files, that makes maintain a lot faster.

## Screenshot gallery

![linux_brainrot](https://images2.imgbox.com/17/72/TDNyHzEz_o.png)
![clear](https://images2.imgbox.com/d3/0a/UpxFgZjj_o.png)
![drun](https://images2.imgbox.com/ed/78/35UuRqLG_o.png)
![kitty](https://images2.imgbox.com/c8/4a/TxEgMWUz_o.png)
![hyprlock](https://images2.imgbox.com/77/26/ABvAF4QF_o.png)
![nvim](https://images2.imgbox.com/99/80/1FxfEXs3_o.png)
![powermenu](https://images2.imgbox.com/08/11/qRBCBrEa_o.png)
![swaync](https://images2.imgbox.com/22/a8/nDRZPMDO_o.png)

## Main components

- **Window manager**: Hyprland
- **Display manager**: Ly
- **Terminal**: Kitty
- **Shell**: Zsh
- **Lock screen**: Hyprlock
- **Walpaper backend**: Hyprpaper
- **Colorpicker**: Hyprpicker
- **Screenshot**: Grim + Slurp + Swappy
- **File manager**: Nautilus
- **Power menu, app launcher**: Rofi
- **Taskbar**: Waybar
- **Notifications**: Swaync
- **Fetch**: Fastfetch

## Compatibility

### Linux distribution

As for now, this installer is only made for Arch and its-based distributions. Support of any other distributions is not planned yet.

### Device type

- Desktop ✅
- Laptop ✅

### GPU vendor

- AMD ✅ (not tested)
- Nvidia ✅
- Intel ✅ (not tested)

## How to install

> Installation can take from 10 to 30 minutes with archinstall or 5 to 15 without

### 1. Install Git

```
sudo pacman -S git
```

### 2. Сlone repository

```
git clone https://github.com/147888sf/arch_hypr_dots.git
```

Or DEV branch (Very unstable! Usually outddated!)

```
git clone --branch dev https://github.com/147888sf/arch_hypr_dots.git
```

### 3. Run install script

```
sh arch_hypr_dots/install.sh
```

Then you should enter your password around two times, then select installer preferences and wait.

# For developers

## How it works overall

`install.sh` script installs python and libs for other scripts. Then it starts `installv2.py` script which installs [Paru-bin](https://aur.archlinux.org/packages/paru-bin]) aur helper, then asks questions and starts script modules one by one: `modules/install_packages.py`, `modules/install_homefiles.py`, `modules/post_install.py`.

The `modules/install_packages.py` script install all required packages like hyprland, waybar, gtk and etc. It aslo install GPU drivers.

The `modules/install_homefiles.py` script copying files from `home` to `~/`

The `modules/post_install.py` script enables things like DM, fixing user names in config files, enables pipewire and etc

## Where I can find X

- `install.sh`: python and python libs; initilizng installv2.py.
- `installv2.py`: driver list and selection, install parameters, installing paru, initilizing other scripts.
- `tools/selection_tools.py`: full screen install parameters selection module.
- `tools/log_tools.py`: Logging tools for other scripts
- `modules/install_packages.py`: list of all packages, installing it.
- `modules/install_homefiles.py`: copying files from `home` to `~`
- `modules/post_install.py`: fixing waybar CSS home path, enabling multilib, setting wallapeprs, pipewire & wireplumber services, network manager service, GTK settings, DM enabling, reboot after install

## How to make your own installer

### 1. Fork this repo

On the main page press **Fork** button

### 2. Clone forked repo

```
git clone https://github.com/*username*/*repo_name*
```

### 3. Fix, create or change

Using any code editor like VSCode or NeoVim change and test everything you want to.

E.G. i want to use Chromium instead of Firefox. I open `modules/install_packages.py` file with VSCode, change 'firfox' to 'chromium' and save.

### 4. Stage, commit and push

Then, to confirm file changes open terminal in your project and exec:

```
git config --global user.name "Your username for git"
git config --global user.email "Your email for git"

git add . # Add changes to commit
git commit -m "Change log" # commit with description of changes
git push # Push changes to github.
```

> ^ This thing will ask for username and passowrd. You should enter your login and github [Personal Acces Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

# Credits

Vova_4104 (AKA 147888sf) - Author, ricer, developer

1nkognit (AKA 1nkognit2) - Co-author, tester
