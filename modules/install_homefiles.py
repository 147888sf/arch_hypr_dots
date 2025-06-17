import os
import pathlib
import shutil

from tools.log_tools import err_log


def install_homefiles(do_backup):
    file_dir = pathlib.Path(__file__).parent.parent.resolve()
    home = pathlib.Path(os.path.expanduser("~")).resolve()
    source_dir = file_dir / "home"

    def copy_with_replace(src, dst):
        try:
            if src.is_dir():
                if not dst.exists():
                    dst.mkdir(parents=True)
                for item in src.iterdir():
                    copy_with_replace(item, dst / item.name)
            else:
                if src.name == "custom.conf" and dst.is_file():
                    pass
                else:
                    if do_backup:
                        if dst.is_file():
                            os.rename(dst, str(dst) + ".backup")
                    shutil.copy2(src, dst, follow_symlinks=False)
        except Exception as e:
            err_log(e)

    copy_with_replace(source_dir, home)


if __name__ == "__main__":
    install_homefiles()
