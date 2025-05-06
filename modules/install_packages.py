import os

def install_packages(selected_drivers, do_ly_dm):
	packages = {
		'Pacman': [
			'gtk3',
			'gtk4',
			'hyprland',
			'xdg-desktop-portal-hyprland',
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
			'gnome-music',
			'eog',
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
			'libnotify',
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

	os.system(f'sudo pacman -Sy && sudo pacman -S --noconfirm --needed {pacman_parsed}')
	os.system(f'paru -Sy && paru -S --noconfirm --needed {aur_parsed}')