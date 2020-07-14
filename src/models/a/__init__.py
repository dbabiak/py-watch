from time import sleep
from utils import log

indent = 4 * ' '

log(indent + f'importing {__file__}')
sleep(2)
log(indent + f'Done with {__file__}')

def models_a():
    return 43

def A():
    return 3




def do_thing():
    from models.b import B
    return f"A: {A()} B: {B()}"
