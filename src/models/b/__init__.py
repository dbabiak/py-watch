from time import sleep
from utils import log

indent = 8 * ' '
log(indent + f'importing {__file__}')
sleep(2)
log(indent + f'Done with {__file__}')

def models_b():
    return __file__


def B():
    return 2

