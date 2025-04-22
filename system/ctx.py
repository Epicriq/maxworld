import os
import platform
from config import LOG
import logging

class Context:
    # Настройка логирования
    @staticmethod
    def init_logger(classname):
        logging.basicConfig(
            filename=LOG["filename"],
            level=LOG["level"],
            format=LOG["format"],
            datefmt=LOG["datefmt"]
        )        
        return logging.getLogger(classname)
    # Примеры записей
    #logger.debug("Это сообщение уровня DEBUG (не выведется)")
    #logger.info("Информационное сообщение")
    #logger.warning("Предупреждение!")
    #logger.error("Ошибка!")
    #logger.critical("Критическая ошибка!")
    
    @classmethod
    def __new__(cls, *args, **kwargs):
        raise TypeError("Нельзя создавать экземпляры этого класса")

# Очистка экрана
def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:  # Linux, MacOS
        os.system('clear')

def print_logo():
    print()
    print(" ███╗   ███╗ █████╗ ██╗  ██╗██╗    ██╗ ██████╗  ██████╗ ██████╗ ██╗     ██████╗ ")
    print(" ████╗ ████║██╔══██╗╚██╗██╔╝██║    ██║██╔═══██╗██╔═══██╗██╔══██╗██║     ██╔══██╗")
    print(" ██╔████╔██║███████║ ╚███╔╝ ██║ █╗ ██║██║   ██║██║   ██║██████╔╝██║     ██║  ██║")
    print(" ██║╚██╔╝██║██╔══██║ ██╔██╗ ██║███╗██║██║   ██║██║   ██║██╔══██╗██║     ██║  ██║")
    print(" ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗╚███╔███╔╝╚██████╔╝╚██████╔╝██║  ██║███████╗██████╔╝")
    print(" ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ")
