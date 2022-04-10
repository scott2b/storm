from .db import Container
from . import crud

DEFAULT_MODULES = [crud]

def wire(modules=None):
    if modules is None:
        modules = DEFAULT_MODULES
    container = Container()
    container.init_resources()
    container.wire(modules=modules)
