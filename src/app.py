import os
from importlib import import_module, reload
from time import sleep
from typing import Dict

from utils import fpath_to_module_name


def use_thing_from_both():
    from models.a import do_thing

    s = do_thing()
    return f"do_thing: {s}"


def get_mtimes(root: str) -> Dict[str, float]:
    """
    Map of file path to most recent modified time
    """
    import os

    mtimes_by_file = {}

    with temp_cwd(root):
        for dirpath, dirnames, filenames in os.walk('.'):
            for f in filenames:
                fpath = os.path.join(dirpath, f)
                if f.endswith(".py"):
                    mtime = os.path.getmtime(fpath)
                    mtimes_by_file[fpath] = mtime
    return mtimes_by_file


# def run_task():
#     print(dt.utcnow().isoformat(sep=' '), use_thing_from_both(), end='\n' * 2)


def run_task():
    import pytest
    os.system('clear')
    pytest.main(args=[], plugins=None)


from contextlib import contextmanager


@contextmanager
def temp_cwd(s):
    import os

    old_dir = os.getcwd()
    try:
        os.chdir(s)
        yield
    finally:
        os.chdir(old_dir)


def main():
    # root should be e.g. money-srv/src or something
    import sys

    # _, src_root = sys.argv
    src_root = '.'

    old_mtimes = {}

    try:
        while True:
            new_mtimes = get_mtimes(src_root)

            # have any files been updated?
            changed_fps = [
                fp for fp, mtime in new_mtimes.items() if mtime != old_mtimes.get(fp)
            ]

            # reload the modules for any updated files
            if changed_fps:
                with temp_cwd(src_root):
                    for fp in changed_fps:
                        module_name = fpath_to_module_name(fp)
                        module = import_module(module_name)
                        reload(module)

                old_mtimes = new_mtimes

                # re-run whatever our task is
                run_task()

            # zzz
            sleep(.5)
    except Exception as err:
        print(err)
        breakpoint()
        print(42)


if __name__ == "__main__":
    main()
