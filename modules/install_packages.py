import subprocess

def cmdrun(command):
    return subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

def install_packages(selected_drivers, do_ly_dm):
	packages = {
		'Pacman': [
			'gtk3',
			'gtk4',
			'hyprland',
			'hyprpicker',
			'hyprpolkitagent',
			'hyprpaper',
			'hyprlock',
			'qt5-wayland',
			'qt6-wayland',
			'gnome-themes-extra',
			'firefox',
			'nano',
			'flatpak',
			'nautilus',
			'vim',
			'gnome-calculator',
			'gnome-disk-utility',
			'gnome-text-editor',
			'gnome-system-monitor',
			'waybar',
			'cliphist',
			'wl-clipboard',
			'rofi',
			'kitty',
			'python-pywal',
			'celluloid',
			'pavucontrol',
			'noto-fonts',
			'noto-fonts-emoji',
			'noto-fonts-extra',
			'ttf-liberation',
			'ttf-jetbrains-mono',
			'ttf-jetbrains-mono-nerd',
			'fastfetch',
			'xdg-desktop-portal',
			'xdg-desktop-portal-gtk',
			'xdg-desktop-portal-hyprland',  
			'swaync',
			'pipewire',
			'pipewire-pulse',
			'wireplumber',
			'iwd',
			'networkmanager',
			'network-manager-applet',
			'ntfs-3g',
			'dosfstools',
	
			'fuse',
			'ufw',
			'grim',
			'slurp',
			'swappy',
			'playerctl',
			'zsh',
			'zsh-syntax-highlighting',
			'zsh-autosuggestions'
		],

		'Aur': [
			'oh-my-posh-bin',
			'pinta',
			'nwg-look',
			'papirus-icon-theme',
			'papirus-folders',
			'bibata-cursor-theme-bin',
			'emote'
		]
	}

	packages['Pacman'] += selected_drivers

	if do_ly_dm:
		packages['Pacman'].append('ly')

	pacman_parsed = ' '.join(packages['Pacman'])
	aur_parsed = ' '.join(packages['Aur'])

	cmdrun(f'sudo pacman -Sy && sudo pacman -S --noconfirm --needed {pacman_parsed}')
	cmdrun(f'paru -Sy && paru -S --noconfirm --needed {aur_parsed}')