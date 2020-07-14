from datetime import datetime as dt, datetime
from time import sleep


def log(s: str):
    now = dt.utcnow()
    now: datetime = (
        now.replace(microsecond=now.microsecond//1000*1000)
    )
    print(now.time().isoformat()[:-3], '::', s)


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


log(f'  {__name__} SLEEPING')
sleep(0.5)
log(f'  {__name__} IMPORTED')

