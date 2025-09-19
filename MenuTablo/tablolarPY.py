from rich import box
import MenuTablo.menu as Menu
import VERI.emptyLists as EmptyLists
from rich.table import Table
from rich.console import Console
from rich.console import Console; z=Console()


ÖğrenciListesi="👨‍🎓 Öğrenci Listesinden"
ListeBaşlığı="Silinen Öğrenciler"
MenüBaşlığı="Ana Menüsü"
menüTipi="Dalaylama"
listeTipi="Kolordu"


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

altBox_stili=Menu.rastgele_box_stili()

def TABLO_6lı(liste: list, menüTipi: str = "Ana Menüm", listeTipi: str = "Ana Listem", Aranan:str="kelime"):
    # Tablo yaratılıyor
    
    
    
    table = Table(title=f"[bold yellow1]BULUNAN ÖĞRENCİLER TABLOSU[/] [thistle1]box_stili:[/]{altBox_stili[0]}",caption=f"{EmptyLists.value} dilimlenmiş tablo",box=altBox_stili[1],show_header=True,header_style="bold cyan",)
    
    
    table.add_column("{Aranan Kelam}", justify="center", style="bold yellow", no_wrap=False)
    table.add_column("Sıra No", justify="center", style="bold yellow", no_wrap=False)
    table.add_column("Id", justify="center", style="white", no_wrap=True)
    table.add_column("Ad", justify="right",style="white")
    table.add_column("Soyad", justify="left",style="white")
    table.add_column("Numarası", justify="left",style="white")
    table.add_column("Doğ.Tar.", justify="center",style="yellow")
    table.add_column("Sınıf", justify="center",style="green")
    table.add_column("Kayıt Tarihi", justify="center", style="white", no_wrap=True,overflow="crop")
    
    for sıra_numarası, ogrenci in enumerate(liste):
            [ f"Aranan"],
            table.add_row(str(sıra_numarası),
                                   str(ogrenci["Id"]),
            ogrenci["ad"],
            ogrenci["soyad"],
            ogrenci["ogrenciNumarasi"],
            ogrenci["dogumTarihi"],
            ogrenci["sinifi"],
            ogrenci["kayitTarihi"],
                                     ) 
   
    
            # Tablo yaratıldı. 
    
    
    z.print("\n", table)
    
    


    
  