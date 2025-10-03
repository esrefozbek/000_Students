from rich.console import Console; console = Console() 
from rich.table import Table
from rich.panel import Panel
from rich import print, box
import os, random
import Widgetler.SayacAnimasyon.spinner as SpinnersPY
import Widgetler.randomRenk as RR



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
     
     
     #^ bu  rastgele_box_stili()   metodu tekniMenü.py'de de  var.
    
def rastgele_box_stili():
    global secim
    secim=random.choice(box_turleri)
    box_objesi = getattr(box, secim)
    mesaj="Bugün hava kapalı olacak"
  #^  print(type(box_objesi))
    return secim,box_objesi,mesaj   #^ bu return, tuple olarak kabul edilir


# boxStilim=rastgele_box_stili()


def menu_goster():
    renk=RR.randomRENK()
   ####################################### os.system("cls" if os.name == "nt" else "clear")  # Terminal temizliği
    
    table = Table(title="", box=rastgele_box_stili()[1], expand=False,border_style=RR.randomRENK() )

    table.add_column(f"[{RR.randomRENK()}]Seçim[/]", justify="center", style=RR.randomRENK(), no_wrap=False)    
    table.add_column("", justify="center", style=RR.randomRENK(), no_wrap=False)    
    table.add_column(f"[{RR.randomRENK()}]İşlem[/], [{RR.randomRENK()}]Box Stili:[/][{RR.randomRENK()}]{rastgele_box_stili()[0]}[/]", style=RR.randomRENK(),no_wrap=True)

    table.add_row("1","➕",f"Öğrenci Ekle")
    table.add_row("2", "🔍","Öğrenci Bul")
    table.add_row("3", "❌","Öğrenci Sil")
    table.add_row("4", "💾","Kaydet ve Çık")
    table.add_row("5", ":thumbs_up:","Ekranı resetle")
    table.add_row("6",":thumbs_down:","Bir kaydı editleme") 
    table.add_row("7", "📋","Öğrencileri Listele (10 Dilimli)")
    table.add_row("77", "📋", "Öğrencileri Listele (50 Dilimli)")
    table.add_row("44","",f"Teknik menüye hicret et") 
    
    panel = Panel(table, title=f"[{RR.randomRENK()}] AnaMenü [/]", title_align="right", border_style=RR.randomRENK(), expand=False)
    console.print(panel)
    
# Menü oluşturuldu





