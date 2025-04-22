from rich import print
class BaseManager():
    def __init__(self):
        print(f"[bold white]Загрузка модуля: \"{self.__class__.__module__}\"[/bold white]")
