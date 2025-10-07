from rich import box
import MenuTablo.menu as Menu
import VERI.emptyLists as EMPTY
from rich.table import Table
from rich.text import Text
from rich.console import Console; c=Console()
import Widgetler.randomRenk  as RENK
from rich.panel import Panel
from rich.columns import Columns
import AsistanFonksiyonlar.arama as ARAMA
from rich.align import Align

#FIXME - Erkek dişi sütunu ekle. Uyruk sütünu kle. Ya da bunları alt listede ver.

ÖğrenciListesi="👨‍🎓 Öğrenci Listesinden"
ListeBaşlığı="Silinen Öğrenciler"
MenüBaşlığı="Ana Menüsü"
menüTipi="Dalaylama"
listeTipi="Kolordu"
Table_Box_style=Menu.random_BoxStili()

def tabloyaGonder(liste):
        if len(liste[0])==9:
                TABLO_kriterli(liste)
        if len(liste[0])==8:
                genel_TABLO(liste)


def genel_TABLO(liste: list):
    c.rule("TABLO SONUÇLARI",style="orange_red1",align="right")
    # Tablo yaratılıyor
    Eight_Colors=[]
    Eight_Colors.clear()
    Eight_Colors = list(set([RENK.randomRENK() for _ in range(1,9)]))
    while len(Eight_Colors) < 8:
        Eight_Colors.append(RENK.randomRENK())

    c.print("SevenColors >> ",Eight_Colors ,end="")
    c.print(ARAMA.renk_teksti(Eight_Colors))
    c.print(Columns([ARAMA.renk_kutusu(renk) for renk in Eight_Colors]),end="\n")
    c.print("  \n") 
    
        
    titleAbove=f"[{RENK.randomRENK()}]ÖĞRENCİLER TABLOSU[/]  "
   
    table = Table(title=titleAbove,
                 caption=f"[{RENK.randomRENK()}]{EMPTY.value}[/] [{RENK.randomRENK()}]tane var[/] ",
                 box=Table_Box_style[1],
                 show_header=True,
                 #header_style="bold bright_white",
                 row_styles = ["none", "dim"],
                 border_style=f"{RENK.randomRENK()}",
                 title_justify="right",
                 highlight=True,
                 safe_box=False  )

    table.add_column(f"[{Eight_Colors[0]}]SıraTNo", justify="center", no_wrap=False)
    table.add_column(f"[{Eight_Colors[1]}]Id", justify="center", no_wrap=True)
    table.add_column(f"[{Eight_Colors[3]}]Ad", justify="right")
    table.add_column(f"[{Eight_Colors[3]}]Soyad", justify="left")
    table.add_column(f"[{Eight_Colors[4]}]Numarası", justify="left")
    table.add_column(f"[{Eight_Colors[5]}]Doğ.Tar.", justify="center")
    table.add_column(f"[{Eight_Colors[6]}]Sınıf", justify="center")
    table.add_column(f"[{Eight_Colors[7]}]Kayıt Tarihi", justify="center", no_wrap=True,overflow="crop")

    for sıra_numarası, item in enumerate(liste, start=1):
      table.add_row(
        f"[{Eight_Colors[0]}]{sıra_numarası}[/]",
        f"[{Eight_Colors[1]}]{item['Id']}[/]",
        f"[{Eight_Colors[3]}]{item['ad']}[/]",
        f"[{Eight_Colors[3]}]{item['soyad']}[/]",
        f"[{Eight_Colors[4]}]{item['ogrenciNumarasi']}[/]",
        f"[{Eight_Colors[5]}]{item['dogumTarihi']}[/]",
        f"[{Eight_Colors[6]}]{item['sinifi']}[/]",
        f"[{Eight_Colors[7]}]{item['kayitTarihi']}[/]",
    )


    
    return  table
    

 
def sagSolTablo(tablo:Table,liste: list):
    # Sol panel: tablo
        panel_sol = Panel(tablo, title=f"[{RENK.randomRENK()}]Öğrenci Tablosu[/]",subtitle=f"[{RENK.randomRENK()}]box_sitilim:[/][{RENK.randomRENK()}]{Table_Box_style[0]}[/]", subtitle_align="right", border_style=f"{RENK.randomRENK()}",title_align="left", width=90,)

        # Sağ panel: özet bilgiler
        toplam_ogrenci = len(liste)
        aranan_kriterler = sum(1 for item in liste if item.get("kriter")) 
        ilk_kayit = liste[0]["kayitTarihi"] if liste else "—"
        son_kayit = liste[-1]["kayitTarihi"] if liste else "—"  
        kriterler = ", ".join(set(item.get("kriter", "") for item in liste if item.get("kriter"))) or "Yok"
        ozet_text = Text(overflow="ellipsis")
        ozet_text.append(f"👥 Toplam Öğrenci: {toplam_ogrenci}\n", style=f"{RENK.randomRENK()}")
        ozet_text.append(f"🔎 Aranan Kriterler: {kriterler}", style=f"{RENK.randomRENK()}")
        ozet_text.append(f"\n🔎 Aranan Kriter Sayısı: {aranan_kriterler}", style=f"{RENK.randomRENK()}")
    #     ozet_text.append(f"📅 İlk Kayıt: {ilk_kayit}\n", style="bold green")
    #     ozet_text.append(f"📅 Son Kayıt: {son_kayit}\n", style="bold magenta")

        panel_sag = Panel(ozet_text,
                          title=f"[{RENK.randomRENK()}]Özet Bilgiler[/]",
                          border_style=f"{RENK.randomRENK()}",
                            title_align="left",
                            style=f"on {RENK.randomRENK()}",
                          width=35)

        kolonlar = Columns([panel_sol,panel_sag], align="left", expand=False)
        c.print(kolonlar)
        
        return tabloKapanis()
        
        
    
def tabloKapanis():
        c.rule("Tablo sonuçlar yukarıda sunuldu",style="orange_red1",align="right")
        c.print("",end="\n")
        EMPTY.TKB_Miktarlar=[]
  

def ogrenci_panel(sozlukListesi: list[dict]):
    panellerListesi = []
    for ogr_data in sozlukListesi:
        # Her alanı güvenli şekilde al (None ise boş string)
        ogr_id   = str(ogr_data.get("Id", ""))
        ad       = ogr_data.get("ad", "") or ""
        soyad    = ogr_data.get("soyad", "") or ""
        numara   = ogr_data.get("ogrenciNumarasi", "") or ""
        sinif    = ogr_data.get("sinifi", "") or ""
        dogum    = ogr_data.get("dogumTarihi", "") or ""
        # Text ile biçimlendirilmiş içerik
        info = Text() 
        info.append(f"\n🆔 ID       > {ogr_id}\n", style=f"{RENK.randomRENK()}")
        info.append(f"👤 Ad       > {ad}\n", style=f"{RENK.randomRENK()}")
        info.append(f"👥 Soyad    > {soyad}\n", style=f"{RENK.randomRENK()}")
        info.append(f"🔢 Numara   > {numara}\n", style=f"{RENK.randomRENK()}")
        info.append(f"🏫 Şube     > {sinif}\n", style=f"{RENK.randomRENK()}")
        info.append(f"🎂 Doğ. Tar.> {dogum}", style=f"{RENK.randomRENK()}")
        # Panel hazırla
        panel = Panel(
            info,
            title="[bold spring_green2]Öğrenci Bilgisi  [/]",
            border_style=f"{RENK.randomRENK()}",
            expand=False,
            width=30,
            
        )
        panel=Align.left(panel)
        panellerListesi.append(panel)
        
        # Tüm panelleri yan yana göster
    return panellerListesi    # bu  return  ulaştığı yerde print edilir.




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
    titleBelow=f"[bold spring_green2]BULUNAN ÖĞRENCİLER TABLOSU[/]   [thistle1]box_stilim:[/]{Table_Box_style[0]}"
    table = Table(title=titleBelow,
                 caption=f"{EMPTY.value} tane olsun Benim olsun",
                 box=box.HORIZONTALS,        
                 show_header=True,header_style="bold bright_black",
                 row_styles=["none", "dim"],
                 safe_box=False  )      #box=altBox_stili[1],

    table.add_column("Sıra No", justify="center", style=f"{RENK.randomRENK()}", no_wrap=False)
    table.add_column("Id", justify="center", style=f"{RENK.randomRENK()}", no_wrap=True)
    table.add_column("Ad", justify="right",style=f"{RENK.randomRENK()}")
    table.add_column("Soyad", justify="left",style=f"{RENK.randomRENK()}")
    table.add_column("Numarası", justify="center",style=f"{RENK.randomRENK()}")
    table.add_column("Doğ.Tar.", justify="center",style=f"{RENK.randomRENK()}")
    table.add_column("Sınıf", justify="center",style=f"{RENK.randomRENK()}")
    table.add_column("Kayıt Tarihi", justify="center", style=f"{RENK.randomRENK()}", no_wrap=True,overflow="crop")
    table.add_column("Aranan", justify="left", style=f"{RENK.randomRENK()}", no_wrap=False)

    for sıra_numarası, item in enumerate(liste, start=1):
        try:
                miktar = EMPTY.TKB_Miktarlar[sıra_numarası-1]
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