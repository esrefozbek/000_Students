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



def menu_goster():
    os.system("cls" if os.name == "nt" else "clear")  # Terminal temizliği
    
    table = Table(title="🧠 [bold yellow]Öğrenci Sistemi Menüsü[/bold yellow]", box=boxStilim, expand=False)

    table.add_column("Seçim", justify="center", style="green", no_wrap=False)
    table.add_column(f"İşlem, [red]  Box Stili:[/red] [bold black]{(secim)}[/bold black]", style="white",no_wrap=False)

    table.add_row("1","➕ Öğrenci Ekle")
    table.add_row("2", "🔍 Öğrenci Bul")
    table.add_row("3", "❌ Öğrenci Sil")
    table.add_row("4", "💾 Kaydet ve Çık")
    table.add_row("5", "Ekranı resetle")
    table.add_row("6","✒️  Bir kaydı editleme") 
    table.add_row("7", "📋 Öğrencileri Listele (10 Dilimli)")
    table.add_row("77", "📋 Öğrencileri Listele (50 Dilimli)")
    table.add_row("33","Teknik menüye hicret et") 
    
    panel = Panel(table, title="[red]Ana Menü", border_style="blue", expand=False)
    console.print(panel)
    
# Menü oluşturuldu












def ekranTemizle():
    os.system('cls' if os.name == 'nt' else 'clear')