import pathlib
import shutil
import os

def install_homefiles():
	file_dir = pathlib.Path(__file__).parent.parent.resolve()
	home = pathlib.Path(os.path.expanduser('~')).resolve()
	source_dir = file_dir / 'home'

	def copy_with_replace(src, dst):
		try:
			if src.is_dir():
				if not dst.exists():
					dst.mkdir(parents=True)
				for item in src.iterdir():
					copy_with_replace(item, dst / item.name)
			else:
				shutil.copy2(src, dst, follow_symlinks=False)
		except Exception as e:
			pass

	if source_dir.exists():
		for item in source_dir.iterdir():
			copy_with_replace(item, home / item.name)
		
		shutil.rmtree(source_dir, ignore_errors=True)

if __name__ == '__main__':
	install_homefiles()