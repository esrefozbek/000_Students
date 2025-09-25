from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

console = Console()

# Örnek listeler (senin EMPTY_LISTS objenden geliyor gibi varsaydım)
hatalilar = ["Ahmet", "Mehmet"]
hatasizlar = ["Zeynep", "Elif"]

# Panel'leri tanımla
panel1 = Panel.fit(
    "\n".join(hatalilar),
    title="  hatalı girişler  ",
    style="grey89"
)

panel2 = Panel.fit(
    "\n".join(hatasizlar),
    title=" hatasizSecimleriniz ",
    style="grey39"
)

# Yan yana göstermek için Columns kullan
console.print(Columns([panel1, panel2], equal=True, expand=False))