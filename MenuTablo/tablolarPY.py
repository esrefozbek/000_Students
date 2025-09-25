from rich import box
import MenuTablo.menu as Menu
import VERI.emptyLists as EMPTY_LISTS
from rich.table import Table
from rich.console import Console
from rich.table import Table
from rich.console import Console; c=Console()

#FIXME - Erkek dişi sütunu ekle. 

ÖğrenciListesi="👨‍🎓 Öğrenci Listesinden"
ListeBaşlığı="Silinen Öğrenciler"
MenüBaşlığı="Ana Menüsü"
menüTipi="Dalaylama"
listeTipi="Kolordu"

def tabloyaGonder(liste,  ):
        genel_TABLO(liste, )

altBox_stili=Menu.rastgele_box_stili()

def genel_TABLO(liste: list, ):
    # Tablo yaratılıyor
    titleBelow=f"[bold spring_green2]BULUNAN ÖĞRENCİLER TABLOSU[/]   [thistle1]box_stilim:[/]{altBox_stili[0]}"
    table = Table(title=titleBelow,
                 caption=f"{EMPTY_LISTS.value} tane",
                 box=altBox_stili[1],
                 show_header=True,header_style="bold bright_black",
                 row_styles=["none", "dim"],
                 safe_box=False  )
    
    table.add_column("Sıra No", justify="center", style="bold yellow", no_wrap=False)
    table.add_column("Aranan", justify="center", style="bold yellow", no_wrap=False)
    table.add_column("Id", justify="center", style="white", no_wrap=True)
    table.add_column("Ad", justify="right",style="medium_turquoise")
    table.add_column("Soyad", justify="left",style="medium_turquoise")
    table.add_column("Numarası", justify="left",style="white")
    table.add_column("Doğ.Tar.", justify="center",style="yellow")
    table.add_column("Sınıf", justify="center",style="green")
    table.add_column("Kayıt Tarihi", justify="center", style="white", no_wrap=True,overflow="crop")
    
    for sıra_numarası, item in enumerate(liste,start=1):
            table.add_row(
            str(sıra_numarası),
            item["kriter"],
            str(item["Id"]),
            item["ad"],
            item["soyad"],
            item["ogrenciNumarasi"],
            item["dogumTarihi"],
            item["sinifi"],
            item["kayitTarihi"], ) 
    
    c.print("", table,end="\n")
    c.rule("sonuçlar yukarıda sunuldu",style="red")
    c.print("",end="\n")
    
 #_   if EMPTY_LISTS.Bulunanlar:
 #       c.print("\n➡️  Yeni arama için [bold green]ENTER[/bold green] tuşuna bas...\n➡️  Ana menüye dönmek için [bold red]ESC[/bold red] tuşuna bas...\n")
    


    
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
  