from pathlib import Path
import subprocess
import shutil

class SomethingWentWrong(Exception):
    ...

PROJECT_DIR = Path('/home', 'omdev', 'dev', 'moj', 'app')
CWD = Path(__file__).parent

SKIP = ['release.py', '.git']

def clean_curr_dir():
    for f in CWD.iterdir():
        f = f.relative_to(CWD)
        if str(f) in SKIP:
            continue
        print("DELETING", f)
        if f.is_dir():
            shutil.rmtree(f.absolute())
        else:
            f.unlink()

def copy_project_files():
    cmd = ['cp', '-r', str(PROJECT_DIR/'dist'), '.']
    print(" ".join(cmd))
    if subprocess.call(cmd, cwd=CWD) != 0:
        raise SomethingWentWrong

    dist_path = CWD / 'dist'
    for f in dist_path.iterdir():
        shutil.move(str(f), str(CWD))
    dist_path.rmdir()
    print("Success")


def main():
    clean_curr_dir()
    copy_project_files()

if __name__ == '__main__':
    main()


