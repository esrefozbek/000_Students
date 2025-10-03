from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

table = Table(title="Kriter ve Miktar", box=box.SQUARE)

table.add_column("Sıra", justify="center", style="bold yellow")
table.add_column("Aranan", justify="center", style="cyan")

# Örnek veri
liste = [
    {"kriter": "Matematik", "Id": 1},
    {"kriter": "Fizik", "Id": 2},
    {"kriter": "Kimya", "Id": 3},
]
miktarlar = [5, 12, 7]

for sıra_numarası, item in enumerate(liste, start=1):
    miktar = miktarlar[sıra_numarası-1]
    
    # Hücreyi renklendirmek için Text kullanalım
    cell_text = Text()
    cell_text.append(f"{item.get('kriter','')}\n", style="bold green")   # üst satır
    cell_text.append(f": {miktar} adet", style="bold magenta")          # alt satır
    
    table.add_row(
        str(sıra_numarası),
        cell_text
    )

console.print(table)
