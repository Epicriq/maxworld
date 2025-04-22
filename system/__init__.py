__version__ = '1.0.0'
__author__ = 'ASuslov'
__all__ = ['cmd', 'map', 'mod', 'sys', 'ctx', 'gen', 'man']

from . import cmd
from . import map
from . import mod
from . import sys
from . import ctx 
from . import gen 
from . import man

def package_info():
    print(f"Package version: {__version__}, Author: {__author__}")