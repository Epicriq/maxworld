__version__ = '1.0.0'
__author__ = 'ASuslov'
__all__ = ['info', 'state', 'characteristics', 'abilities', 'skills', 'spells', 'inventory', 'item']

from . import info
from . import state
from . import characteristics
from . import abilities
from . import skills
from . import spells
from . import inventory
from . import item

def package_info():
    print(f"Package version: {__version__}, Author: {__author__}")
	
