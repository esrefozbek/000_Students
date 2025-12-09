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






def random_BoxStili():
    global secim
    secim=random.choice(box_turleri)
    box_objesi = getattr(box, secim)
    mesaj="Bugün hava kapalı olacak"
  #^  print(type(box_objesi))
    return secim,box_objesi,mesaj


boxStilim=random_BoxStili()[1]
boxStili_adi=random_BoxStili()[0]






def teknikMenü():
    global boxStilim,boxStili_adi
    boxStilim=random_BoxStili()[1]
    boxStili_adi=random_BoxStili()[0]  
    

    os.system("cls" if os.name == "nt" else "clear")  # Terminal temizliği
    
    table = Table(title=":thumbs_up: [yellow]Teknik Bakım Menüsü[/yellow]:thumbs_up:", box=boxStilim, expand=False)

    table.add_column("Seçim", justify="center", style="light_goldenrod1", no_wrap=False)
    table.add_column(f"İşlem, [red]  Box Stili:[/red] boxStilim1 [yellow]{boxStili_adi}[/yellow]", style="white",no_wrap=False)

    table.add_row("1", "Veri.yeniEklenenlerListesi_")
    table.add_row("0", "Veri.SozlukluListe_")
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
    table.add_row("14", "[bold yellow]FakeMaker[/]")
    
    table.add_row("33", "Ana Menüye hicret et   ESC ile ")
    
    boxStilim2=random_BoxStili()[1]
    boxStili_adi2=random_BoxStili()[0]
    panel = Panel(table, title="[red]Alt Menü", box=boxStilim2, border_style="light_goldenrod2", expand=False, subtitle=f"boxStilim2 :{boxStili_adi2}")
    console.print(panel)
    

















def ekranTemizle():
    os.system('cls' if os.name == 'nt' else 'clear')