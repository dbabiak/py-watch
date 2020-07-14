from datetime import datetime as dt
from time import sleep
from typing import Dict
from importlib import import_module, reload


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

    for dirpath, dirnames, filenames in  os.walk(root):
        for f in filenames:
            fpath = os.path.join(dirpath, f)
            if f.endswith('.py'):
                mtime = os.path.getmtime(fpath)
                mtimes_by_file[fpath] = mtime
    return mtimes_by_file


def fpath_to_module_name(s: str) -> str:
    """
    Turn a file path into a python import path (?)
    """
    s = s.lstrip('./')

    if s.endswith('.py'):
        s = s[:-len('.py')]

    if s.endswith('/__init__'):
        s = s[:-len('/__init__')]

    return s.replace('/', '.')


def test_fpath_to_module():
    assert fpath_to_module_name('./models/b/__init__.py') == 'models.b'
    assert fpath_to_module_name('models') == 'models'
    assert fpath_to_module_name('models/b/c.py') == 'models.b.c'
    assert fpath_to_module_name('models.b.c') == 'models.b.c'


def main():
    # root should be e.g. money-srv/src or something
    import sys
    import os

    root = '.' if len(sys.argv) == 1 else sys.argv[1]
    os.chdir(root)


    old_mtimes = {}

    try:
        while True:
            new_mtimes = get_mtimes('.')

            # have any files been updated?
            changed_fps = [
                fp
                for fp, mtime in new_mtimes.items()
                if mtime != old_mtimes.get(fp)
            ]

            # reload the modules for any updated files
            if changed_fps:
                for fp in changed_fps:
                    module_name = fpath_to_module_name(fp)
                    module = import_module(module_name)
                    reload(module)
                old_mtimes = new_mtimes

                # re-run whatever our task is
                print(dt.utcnow().isoformat(sep=' '), use_thing_from_both(), end='\n'*2)

            # zzz
            sleep(.2)
    except Exception as err:
        breakpoint()


if __name__ == '__main__':
    main()
