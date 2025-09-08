from rich import box
import tupleyi_Sozluklestirme
import JSON
import menu
import main
import veri

from rich.table import Table
from rich.console import Console
from rich.panel import Panel
import klavyeDinleme
from rich import pretty
import random
from rich.console import Console
console=Console()


ÖğrenciListesi="👨‍🎓 Öğrenci Listesinden"
ListeBaşlığı="Silinen Öğrenciler"
MenüBaşlığı="Ana Menüsü"

menüTipi="Dalaylama"
listeTipi="Kolordu"



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



box_stili=menu.boxStilim



def TABLO_6lı(liste: list, menüTipi: str = "Ana Menümmmm", listeTipi: str = "Ana Listemmmm"):
    # Tablo yaratılıyor
    
    table = Table(title="TABLO",caption=f"{veri.value} dilimlenmiş tablo",box=box_stili,show_header=True,header_style="bold white",)
    table.add_column("Sıra No", justify="center", style="bold yellow", no_wrap=False)
    table.add_column("Id", justify="center", style="white", no_wrap=True)
    table.add_column("Ad", justify="right",style="white")
    table.add_column("Soyad", justify="left",style="white")
    table.add_column("Numarası", justify="left",style="white")
    table.add_column("dog Tar", justify="center",style="yellow")
    table.add_column("Sınıf", justify="center",style="green")
    table.add_column("Kayıt Tarihi", justify="center", style="white", no_wrap=True,overflow="crop")
    
    for sıra_numarası, ogrenci in enumerate(liste):
                  table.add_row(str(sıra_numarası),
                                  str(ogrenci[0]),
                                      ogrenci[1],
                                      ogrenci[2],
                                      str(ogrenci[3]),
                                      ogrenci[4],
                                      ogrenci[5],
                                      ogrenci[6]
                                     ) 
   
    
# Tablo yaratıldı. 
      
   # panel = Panel(table, title=f"[bold cyan]{menüTipi}",  border_style="blue",style="on black", expand=True)
    console.print(table)
    
    


    
  