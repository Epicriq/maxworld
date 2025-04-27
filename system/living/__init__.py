__version__ = '1.0.0'
__author__ = 'ASuslov'
__all__ = ['characters', 'player', 'monster', 'monsters']

from . import characters
from . import player
from . import monster
from . import monsters

def package_info():
    print(f"Package version: {__version__}, Author: {__author__}")
	
