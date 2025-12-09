from rich.console import Console; console = Console() 
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import print, box
import os, random
import Widgetler.SayacAnimasyon.spinner as SpinnersPY
import Widgetler.randomRenk as RENK



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
    
def random_BoxStili():
    global secim
    secim=random.choice(box_turleri)
    box_objesi = getattr(box, secim)
    mesaj="Bugün hava kapalı olacak"
  #^  print(type(box_objesi))
    return secim,box_objesi,mesaj   #^ bu return, tuple olarak kabul edilir, [0] ile seçim, [1] ile box objesi, [2] ile mesaj alınır.


boxStilim=random_BoxStili()


def menu_goster():
    renk=RENK.randomRENK()
    box_stili=random_BoxStili()[1]
    box_stili_adi=random_BoxStili()[0]
   ####################################### os.system("cls" if os.name == "nt" else "clear")  # Terminal temizliği
    
    table = Table(title="Çikolata Yer misin?", box=box_stili, border_style=renk, show_edge=True,title_style=f"bold {renk}", caption_style=f"bold {renk}", header_style=f"bold {renk}", row_styles=[f"none", f"dim"], safe_box=False,padding = (0, 1), collapse_padding= False, pad_edge= True, expand= False, show_header= True, show_footer= False, show_lines = False, leading = 0,)

    table.add_column(f"[{RENK.randomRENK()}]Seçim[/]", justify="center", style=RENK.randomRENK(), no_wrap=False)
    table.add_column("", justify="center", style=RENK.randomRENK(), no_wrap=False)
    table.add_column(f"[{RENK.randomRENK()}]İşlem --> BoxStyle:  {box_stili_adi}[/]",  style=RENK.randomRENK(),no_wrap=True)

    table.add_row("1","➕",f"[{RENK.randomRENK()}]Öğrenci Ekle")
    table.add_row("2", "🔍",f"[{RENK.randomRENK()}]Öğrenci Bul")
    table.add_row("3", "❌",f"[{RENK.randomRENK()}]Öğrenci Sil")
    table.add_row("4", "💾",f"[{RENK.randomRENK()}]Kaydet ve Çık")
    table.add_row("5", ":thumbs_up:",f"[{RENK.randomRENK()}]Ekranı resetle")
    table.add_row("6",":thumbs_down:",f"[{RENK.randomRENK()}]Bir kaydı editleme") 
    table.add_row("7", "📋",f"[{RENK.randomRENK()}]Öğrencileri Listele (10 Dilimli)")
    table.add_row("77", "🍷", f"[{RENK.randomRENK()}]Öğrencileri Listele (50 Dilimli)")
    table.add_row("88", "📊", f"[{RENK.randomRENK()}]Öğrencileri Kaçarlı listelyelim?")
    table.add_row("44", "🍀", f"[{RENK.randomRENK()}]Teknik menüye hicret et")
    table.add_row("8", "📊", f"[yellow]Detaylı[/] arama")
    

    box_stili=random_BoxStili()[1]
    box_stili_adi=random_BoxStili()[0]

    panel = Panel(table, title=f"[{RENK.randomRENK()}] Ana Menü Bölgesi [/]", title_align="right", border_style=renk, expand=True, box=box_stili,
                  subtitle=f"[{RENK.randomRENK()}]Box Stili:[/][{RENK.randomRENK()}]{box_stili_adi}[/]",
                  )
    panel=Align.left(panel)
    console.print(panel)
    
# Menü oluşturuldu





