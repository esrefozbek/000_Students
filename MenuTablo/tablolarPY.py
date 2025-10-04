from rich import box
import MenuTablo.menu as Menu
import VERI.emptyLists as E_LISTS
from rich.table import Table
from rich.text import Text
from rich.console import Console; c=Console()
import Widgetler.randomRenk  as RR
from rich.panel import Panel
from rich.columns import Columns

#FIXME - Erkek dişi sütunu ekle. Uyruk sütünu kle. Ya da bunları alt listede ver.

ÖğrenciListesi="👨‍🎓 Öğrenci Listesinden"
ListeBaşlığı="Silinen Öğrenciler"
MenüBaşlığı="Ana Menüsü"
menüTipi="Dalaylama"
listeTipi="Kolordu"
Box_stili=Menu.rastgele_box_stili()

def tabloyaGonder(liste):
        if len(liste[0])==9:
                TABLO_kriterli(liste)
        if len(liste[0])==8:
                TABLO_kritersiz(liste)


def TABLO_kritersiz(liste: list):
    # Tablo yaratılıyor
    titleBelow=f"[bold spring_green2]BULUNAN ÖĞRENCİLER TABLOSU[/]   [thistle1]box_stilim:[/]{Box_stili[0]}"
    table = Table(title=titleBelow,
                 caption=f"{E_LISTS.value} tane var ",
                 box=Box_stili[1],
                 show_header=True,header_style="bold bright_black",
                 row_styles=["none", "dim"],
                 safe_box=False  )
    
    table.add_column("Sıra No", justify="center", style="bold yellow", no_wrap=False)
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
            str(item["Id"]),
            item["ad"],
            item["soyad"],
            item["ogrenciNumarasi"],
            item["dogumTarihi"],
            item["sinifi"],
            item["kayitTarihi"], ) 
    
    return  table
    

 
def sagSolTablo(tablo:Table,liste: list):
    # Sol panel: tablo
         
        panel_sol = Panel(tablo, title="[bold cyan]Öğrenci Tablosu[/]", border_style="green", width=105)    

        # Sağ panel: özet bilgiler
        toplam_ogrenci = len(liste)
        aranan_kriterler = sum(1 for item in liste if item.get("kriter"))
        ilk_kayit = liste[0]["kayitTarihi"] if liste else "—"
        son_kayit = liste[-1]["kayitTarihi"] if liste else "—"  
        kriterler = ", ".join(set(item.get("kriter", "") for item in liste if item.get("kriter"))) or "Yok"
        ozet_text = Text()
        ozet_text.append(f"👥 Toplam Öğrenci: {toplam_ogrenci}\n", style="bold cyan")
        ozet_text.append(f"🔎 Aranan Kriterler: {kriterler}\n", style="bold yellow")
        ozet_text.append(f"🔎 Aranan Kriter Sayısı: {aranan_kriterler}\n", style="bold yellow")
    #     ozet_text.append(f"📅 İlk Kayıt: {ilk_kayit}\n", style="bold green")
    #     ozet_text.append(f"📅 Son Kayıt: {son_kayit}\n", style="bold magenta")

        panel_sag = Panel(ozet_text,
                          title="[bold magenta]Özet Bilgiler[/]",
                          border_style="blue",
                          width=40)

        kolonlar = Columns([panel_sol,panel_sag], align="left", expand=False)
        c.print(kolonlar)
        
        return tabloKapanis()
        
        
    
def tabloKapanis():
        c.rule("Tablo sonuçlar yukarıda sunuldu",style="orange_red1",align="right")
        c.print("",end="\n")
        E_LISTS.TKB_Miktarlar=[]
  

def ogrenci_panel():
    paneller = []
    for ogr_data in E_LISTS.FARK_SozlukListesi:
        # Her alanı güvenli şekilde al (None ise boş string)
        ogr_id   = str(ogr_data.get("Id", ""))
        ad       = ogr_data.get("ad", "") or ""
        soyad    = ogr_data.get("soyad", "") or ""
        numara   = ogr_data.get("ogrenciNumarasi", "") or ""
        sinif    = ogr_data.get("sinifi", "") or ""
        dogum    = ogr_data.get("dogumTarihi", "") or ""
        # Text ile biçimlendirilmiş içerik
        info = Text() 
        info.append(f"\n🆔 ID       > {ogr_id}\n", style="bold cyan")
        info.append(f"👤 Ad       > {ad}\n", style="bold green")
        info.append(f"👥 Soyad    > {soyad}\n", style="bold green")
        info.append(f"🔢 Numara   > {numara}\n", style="bold yellow")
        info.append(f"🏫 Şube     > {sinif}\n", style="bold white")
        info.append(f"🎂 Doğ. Tar.> {dogum}", style="bold blue")
        # Panel hazırla
        panel = Panel(
            info,
            title="[bold spring_green2]Öğrenci Bilgisi[/]",
            border_style="yellow",
            expand=False
        )
        paneller.append(panel)
        # Tüm panelleri yan yana göster
    return Columns(paneller, expand=False)    # bu  return  ulaştığı yerde print edilir.  
 

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
  
   

def TABLO_kriterli(liste: list):
    # Tablo yaratılıyor
    titleBelow=f"[bold spring_green2]BULUNAN ÖĞRENCİLER TABLOSU[/]   [thistle1]box_stilim:[/]{Box_stili[0]}"
    table = Table(title=titleBelow,
                 caption=f"{E_LISTS.value} tane olsun Benim olsun",
                 box=box.HORIZONTALS,        
                 show_header=True,header_style="bold bright_black",
                 row_styles=["none", "dim"],
                 safe_box=False  )      #box=altBox_stili[1],
    
    table.add_column("Sıra No", justify="center", style=RR.randomRENK(), no_wrap=False)
    table.add_column("Id", justify="center", style=RR.randomRENK(), no_wrap=True)
    table.add_column("Ad", justify="right",style=RR.randomRENK())
    table.add_column("Soyad", justify="left",style=RR.randomRENK())
    table.add_column("Numarası", justify="center",style=RR.randomRENK())
    table.add_column("Doğ.Tar.", justify="center",style=RR.randomRENK())
    table.add_column("Sınıf", justify="center",style=RR.randomRENK())
    table.add_column("Kayıt Tarihi", justify="center", style=RR.randomRENK(), no_wrap=True,overflow="crop")
    table.add_column("Aranan", justify="left", style=RR.randomRENK(), no_wrap=False)
    
    for sıra_numarası, item in enumerate(liste, start=1):
        try:
                miktar = E_LISTS.TKB_Miktarlar[sıra_numarası-1]
        except (IndexError, TypeError):
                miktar = 0   # liste kısa veya int hatası durumunda 0 göster
        cell_text = Text()
        cell_text.append(f"{item.get('kriter','')}\n", style="bold green")   # üst satır
        cell_text.append(f"{miktar} adet", style="bold yellow")
        
        table.add_row(
            str(sıra_numarası),
            str(item["Id"]),
            item["ad"],
            item["soyad"],
            item["ogrenciNumarasi"],
            item["dogumTarihi"],
            item["sinifi"],
            item["kayitTarihi"],
            cell_text,
        )

   
   # c.print("", table,end="\n")
   
    return  table