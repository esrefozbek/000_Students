
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold green")

# 🔹 Sol sütun: Sabit bir değer alacak (örneğin "Sınıf 5A")
table.add_column("Sınıf", justify="center")

# 🔹 Sağ sütunlar: Alt alta çoklu veri içerecek
table.add_column("Adlar", justify="left")
table.add_column("Numaralar", justify="left")

# 🔹 Çok satırlı hücreler için '\n' ile satır atlatılır
adlar = "\n".join(["Zeynep", "Ali", "Elif", "Mehmet"])
numaralar = "\n".join(["123", "124", "125", "126"])

# 🔹 Tüm veri aynı satırda olacak
table.add_row("5A", adlar, numaralar)

console.print(table)


