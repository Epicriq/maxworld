import tkinter as tk
from tkinter import ttk
import uuid

def add_to_table():
    """Добавляем данные в таблицу с UUID и checkbox"""
    new_uuid = str(uuid.uuid4())
    name = name_entry.get()
    value = value_entry.get()
    
    # Добавляем checkbox в отдельный словарь
    var = tk.BooleanVar(value=False)
    checkbox_vars[new_uuid] = var
    
    # Вставляем данные в таблицу (checkbox отображается через '☐'/'☑')
    tree.insert("", "end", values=("☐", new_uuid, name, value), tags=(new_uuid,))
    
    name_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)

def toggle_checkbox(event):
    """Обработчик клика по checkbox в таблице"""
    region = tree.identify("region", event.x, event.y)
    if region != "cell": return
    
    column = tree.identify_column(event.x)
    if column != "#1": return  # Проверяем, что клик в колонке checkbox
    
    item = tree.focus()
    if item:
        item_uuid = tree.item(item, "tags")[0]
        var = checkbox_vars[item_uuid]
    
        # Меняем состояние
        var.set(not var.get())
        tree.set(item, "#1", "☑" if var.get() else "☐")

def delete_checked():
    """Удаляет отмеченные строки"""
    for item_uuid, var in list(checkbox_vars.items()):
        if var.get():
            # Находим и удаляем строку по tag (UUID)
            item = tree.tag_has(item_uuid)
            if item:
                tree.delete(item)
            del checkbox_vars[item_uuid]

# Создаем главное окно
root = tk.Tk()
root.title("Таблица с UUID и Checkbox")
root.geometry("900x500")

# Словарь для хранения состояний checkbox (по UUID)
checkbox_vars = {}

# Поля ввода
tk.Label(root, text="Имя:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

tk.Label(root, text="Значение:").pack(pady=5)
value_entry = tk.Entry(root, width=40)
value_entry.pack(pady=5)

# Кнопки
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Добавить", command=add_to_table)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Удалить отмеченные", command=delete_checked)
delete_button.pack(side=tk.LEFT, padx=5)

# Таблица
columns = ("checkbox", "uuid", "name", "value")
tree = ttk.Treeview(root, columns=columns, show="headings", selectmode="extended")

# Настройка колонок
tree.heading("checkbox", text="✓", anchor=tk.CENTER)
tree.heading("uuid", text="UUID")
tree.heading("name", text="Имя")
tree.heading("value", text="Значение")

tree.column("checkbox", width=30, anchor=tk.CENTER)
tree.column("uuid", width=300)
tree.column("name", width=200)
tree.column("value", width=200)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Привязываем обработчик клика
tree.bind("<Button-1>", toggle_checkbox)

# Полоса прокрутки
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

root.mainloop()