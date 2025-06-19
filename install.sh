cat << "EOF"
  _____           _        _ _
 |_   _|         | |      | | |
   | |  _ __  ___| |_ __ _| | | ___ _ __
   | | | '_ \/ __| __/ _` | | |/ _ \ '__|
  _| |_| | | \__ \ || (_| | | |  __/ |
 |_____|_| |_|___/\__\__,_|_|_|\___|_|
    Made by Vova_4104

EOF

script_dir=$(dirname "$(realpath "$0")")

sudo -v

(
    while true; do
        sleep 600
        sudo -v
    done
) &
PID=$!

cat << "EOF"
          ___         _        _ _ _                       _   _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __ _  _| |_| |_  ___ _ _
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \ || |  _| ' \/ _ \ ' \
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\_, |\__|_||_\___/_||_|
                                         |___/  |_|   |__/
EOF
sudo pacman -S --noconfirm python python-colorama
python "$script_dir/installer_main.py"
