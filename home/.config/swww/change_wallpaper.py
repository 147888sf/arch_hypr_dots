import os
import random
import subprocess
import time

WALLPAPER_DIR = os.path.expanduser("~/Wallpapers")
INTERVAL_SECONDS = 600

IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp"]

previous_wallpaper = None


def get_random_wallpaper(previous):
    files = [
        f
        for f in os.listdir(WALLPAPER_DIR)
        if any(f.lower().endswith(ext) for ext in IMAGE_EXTENSIONS)
    ]

    if not files:
        return None

    if len(files) == 1:
        return os.path.join(WALLPAPER_DIR, files[0])

    choices = [f for f in files if os.path.join(WALLPAPER_DIR, f) != previous]
    chosen = random.choice(choices)
    return os.path.join(WALLPAPER_DIR, chosen)


def set_wallpaper(image_path):
    subprocess.run(
        [
            "swww",
            "img",
            image_path,
            "--transition-type",
            "wipe",
            "--transition-angle",
            "30",
            "--transition-fps",
            "60",
        ]
    )

    subprocess.run(["wal", "-i", image_path, "-q"])

    subprocess.run(
        [
            "killall",
            "waybar",
        ]
    )

    subprocess.Popen(["waybar"])


def main():
    global previous_wallpaper

    subprocess.Popen(["swww-daemon"])

    while True:
        wallpaper = get_random_wallpaper(previous_wallpaper)
        if wallpaper:
            print(f"Setting wallpaper: {wallpaper}")
            set_wallpaper(wallpaper)
            previous_wallpaper = wallpaper
        else:
            print("No valid wallpapers found.")
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
