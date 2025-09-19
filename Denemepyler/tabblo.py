from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")

# 🔹 1. Sütun: Ortalanmış ve tek satırlık (ya da normal)
table.add_column("ID", justify="center")

# 🔹 2. ve 3. Sütunlar: Sol hizalı, çok satırlı destekler
table.add_column("Ad", justify="left", overflow="fold")
table.add_column("Açıklama", justify="left", overflow="fold", max_width=40)

# 🔹 Örnek veriler
table.add_row("1", "Zeynep", "Bu açıklama çok uzun bir metindir ve otomatik olarak alt satıra geçer.")
table.add_row("2", "Fahrettin", "Kısa açıklama.")
table.add_row("3", "Mehmet Ali", "Bu da başka bir çok satırlı açıklamadır.\nEk satır burada başlar.")

console.print(table)
