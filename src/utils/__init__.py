from datetime import datetime as dt, datetime
from time import sleep


def log(s: str):
    now = dt.utcnow()
    now: datetime = (
        now.replace(microsecond=now.microsecond//1000*1000)
    )
    print(now.time().isoformat()[:-3], '::', s)

log(f'  {__name__} SLEEPING')
sleep(0.5)
log(f'  {__name__} IMPORTED')
