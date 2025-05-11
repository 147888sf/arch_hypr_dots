import subprocess
import os

def cmdrun(command, cwd):
    try:
        return subprocess.run(command, shell=True, cwd=cwd, check=True, text=True)
    except subprocess.CalledProcessError:
        pass

def install_packages(selected_drivers, do_ly_dm):
	packages = {
		'Pacman': [
			'hyprland',
			'hyprpicker',
			'hyprpolkitagent',
			'hyprpaper',
			'hyprlock',
            'hypridle',
            'gtk3',
			'gtk4',
			'qt5-wayland',
			'qt6-wayland',
			'gnome-themes-extra',
			'firefox',
			'nano',
			'flatpak',
			'nautilus',
			'neovim',
            'pyright',
			'npm',
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
			'zsh-autosuggestions',
            
			'discord',
            'telegram-desktop',
            'qbittorrent',
            'lutris',
            'steam',
            'vine'
		],

		'Aur': [
			'oh-my-posh-bin',
			'pinta',
			'nwg-look',
			'papirus-icon-theme',
			'papirus-folders',
			'bibata-cursor-theme-bin',
			'emote',
            
            'via-bin',
            'visual-studio-code-bin'
		]
	}

	packages['Pacman'] += selected_drivers

	if do_ly_dm:
		packages['Pacman'].append('ly')

	pacman_parsed = ' '.join(packages['Pacman'])
	aur_parsed = ' '.join(packages['Aur'])

	cmdrun(f'sudo pacman -Sy && sudo pacman -S --noconfirm --needed {pacman_parsed}', os.path.expanduser('~'))
	cmdrun(f'paru -Sy && paru -S --noconfirm --needed {aur_parsed}', os.path.expanduser('~'))
	cmdrun('flatpak install -y flathub org.vinegarhq.Sober')