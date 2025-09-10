from rich.console import Console; console = Console() 
from rich.table import Table
from rich.panel import Panel
from rich import print, box
import os, random


box_turleri = [
   "ASCII",
        "ASCII2",
        "ASCII_DOUBLE_HEAD",
        "SQUARE",
        "SQUARE_DOUBLE_HEAD",
        "MINIMAL",
        "MINIMAL_HEAVY_HEAD",
        "MINIMAL_DOUBLE_HEAD",
        "SIMPLE",
        "SIMPLE_HEAD",
        "SIMPLE_HEAVY",
        "HORIZONTALS",
        "ROUNDED",
        "HEAVY",
        "HEAVY_EDGE",
        "HEAVY_HEAD",
        "DOUBLE",
        "DOUBLE_EDGE",
        "MARKDOWN",
]

def ekranTemizle():
     os.system('cls' if os.name == 'nt' else 'clear')
    
def rastgele_box_stili():
    global secim
    secim=random.choice(box_turleri)
    box_objesi = getattr(box, secim)
    mesaj="Bugün hava kapalı olacak"
    print(type(box_objesi))
    return secim,box_objesi,mesaj   #^ bu return, tuple olarak kabul edilir


# boxStilim=rastgele_box_stili()


def menu_goster():
   ####################################### os.system("cls" if os.name == "nt" else "clear")  # Terminal temizliği
    
    table = Table(title="🧠 [bold yellow]Öğrenci Sistemi Menüsü[/bold yellow]", box=rastgele_box_stili()[1], expand=False)

    table.add_column("Seçim", justify="center", style="green", no_wrap=False)    
    table.add_column("Sembol", justify="center", style="green", no_wrap=False)    
    table.add_column(f"İşlem, [grey46]  Box Stili:[/][bold turquoise2]{rastgele_box_stili()[0]}[/]", style="white",no_wrap=False)

    table.add_row("1","➕","Öğrenci Ekle")
    table.add_row("2", "🔍","Öğrenci Bul")
    table.add_row("3", "❌","Öğrenci Sil")
    table.add_row("4", "💾","Kaydet ve Çık")
    table.add_row("5", ":thumbs_up:","Ekranı resetle")
    table.add_row("6",":thumbs_down:","Bir kaydı editleme") 
    table.add_row("7", "📋","Öğrencileri Listele (10 Dilimli)")
    table.add_row("77", "📋", "Öğrencileri Listele (50 Dilimli)")
    table.add_row("33","","Teknik menüye hicret et") 
    
    panel = Panel(table, title="[red]Ana Menü", border_style="blue", expand=False)
    console.print(panel)
    
# Menü oluşturuldu





