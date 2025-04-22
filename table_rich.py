from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Персонажи")
table.add_column("Имя", style="cyan")
table.add_column("Класс", style="magenta")
table.add_column("Уровень", style="green")

table.add_row("Арагорн", "Воин", "10")
table.add_row("Гэндальф", "Маг", "99")

console.print(table)