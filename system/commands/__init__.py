__version__ = '1.0.0'
__author__ = 'ASuslov'
__all__ = ['base_cmd', 'inventory_cmd', 'mapview_cmd', 'exit_cmd', 'nord_cmd', 'south_cmd', 'west_cmd', 'east_cmd']

from . import base_cmd
from . import inventory_cmd
from . import mapview_cmd
from . import exit_cmd
from . import nord_cmd
from . import south_cmd
from . import west_cmd
from . import east_cmd

def package_info():
    print(f"Package version: {__version__}, Author: {__author__}")
	
