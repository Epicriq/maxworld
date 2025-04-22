from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.layout import Layout
from rich.box import *

md_text = """
# Заголовок
- Список
- Ещё пункт
"""
console = Console()
panel = Panel(Markdown(md_text), title="Информация", border_style="blue")
console.print(panel)

panel = Panel(Markdown("- Автоматический\r- размер"), box=MINIMAL)
console.print(panel)

panel = Panel("Содержимое панели", height=10)
console.print(panel)

layout = Layout()
layout.split(
    Layout(name="upper", size=10),
    Layout(name="lower")
)
layout["upper"].update(
    Panel("Верхняя панель", height=8)
)
layout["lower"].update(
    Panel("Нижняя панель")
)
console.print(layout)