from rich.console import Console; console = Console() 
from rich.table import Table
from rich.panel import Panel
from rich import print, box
import os, random


box_turleri = [
    "ASCII",
    "ASCII2",
    "DOUBLE",
    "HEAVY",
    "HEAVY_EDGE",
    "HORIZONTALS",
    "MINIMAL",
    "MINIMAL_DOUBLE_HEAD",
    "MINIMAL_HEAVY_HEAD",
    "ROUNDED",
    "SIMPLE",
    "SIMPLE_HEAD",
    "SQUARE"
]


def rastgele_box_stili():
    global secim
    secim=random.choice(box_turleri)
    box_objesi = getattr(box, secim)
    print(type(box_objesi))
    return box_objesi

boxStilim=rastgele_box_stili()





def teknikMenü():
    os.system("cls" if os.name == "nt" else "clear")  # Terminal temizliği
    
    table = Table(title="🧠 [bold yellow]Teknik Bakım Menüsü[/bold yellow]", box=boxStilim, expand=False)

    table.add_column("Seçim", justify="center", style="green", no_wrap=False)
    table.add_column(f"İşlem, [red]  Box Stili:[/red] [bold black]{(secim)}[/bold black]", style="white",no_wrap=False)

    table.add_row("1", "Yeni Eklenen Öğrenci Listesi")
    table.add_row("2", "Silinen Öğrenci Listesi")
    table.add_row("3", "JSON'dan okuma(Tupleli liste oluşturma)")
    table.add_row("4", "Tupleli Liste")
    table.add_row("5", "Tupleli Listeyi Sözlükleştirme")
    table.add_row("6", "Sözlüklü Liste")
    table.add_row("7", "Listeyi JSON yap ve Dosyaya kaydet")
    table.add_row("8", "Ekranı resetle")
    table.add_row("9", "TupleliListe_yi sıfırla")
    table.add_row("10", "SözlüklüListe_yi sıfırla")
    table.add_row("11", "TupleListeyi Dilimle")
    table.add_row("12", "SORGU(eğer yoksa jsondan tuple yap.)")
    table.add_row("13", "256 [italic]Renk Paleti[/]")
    table.add_row("44", "Ana Menüye hicret et")
    
    panel = Panel(table, title="[red]Alt Menü", border_style="blue", expand=False)
    console.print(panel)
    

















def ekranTemizle():
    os.system('cls' if os.name == 'nt' else 'clear')