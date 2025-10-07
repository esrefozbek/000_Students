from rich.live import Live
import time
import random
import colorsys
import msvcrt
import readchar

from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align
from rich.layout import Layout
from rich.layout import Layout
from rich.text import Text

import MenuTablo.tablolarPY as TABLO
import VERI.emptyLists as EMPTY
import Widgetler.randomRenk as RENK

import math

c = Console()



# ---------- RENK ----------


# ---------- Üst Panel (Tablo + Özet) ----------
from rich.columns import Columns

def top_panel(ogr_list: list[dict]):
    paneller =TABLO.ogrenci_panel(ogr_list)   # senin fonksiyon
    return Columns(paneller, expand=False, equal=False)


# ---------- Alt Onay Paneli ----------


#
# --- Alt paneli oluştur ---
def onay_panel(ogr: dict) -> Align:
    ad_soyad = f"{ogr['ad']} {ogr['soyad']} ({ogr.get('ogrenciNumarasi','')})"
    panel= Panel(
        f"👇👇👇 {ad_soyad} silmek istiyor musunuz ❓\n"
        f"Silmek için 'E', iptal için 'H' tuşuna bas",
        title=" Evet / Hayır Onayı ",
        border_style="yellow",
        width=60,height=5,
        style="on dark_blue"

    )
    return Align.left(panel, vertical="bottom")


# ---------- Öğrenci Silme Onayı ----------
def Evet_Hayir_OnayiAl(ogr: dict,layout) -> bool:
    ad_soyad = f"{ogr['ad']} {ogr['soyad']} ({ogr.get('ogrenciNumarasi','')})"
    layout["bottom"].update(onay_panel(ogr))

    while True:
        tus = readchar.readchar().lower()
        if tus in ['e', '\r']:
            layout["bottom"].update(Panel(f"✅ {ad_soyad} silindi!", border_style="green"))
            return True
        elif tus in ['h', '\x1b']:
            layout["bottom"].update(Panel(f"❌ {ad_soyad} iptal edildi!", border_style="red"))
            return False
        else:
            # Önceki mesajı kaybetmeden uyarı göster
            layout["bottom"].update(
                Panel(
                    f"⚠ Geçersiz tuş! 'E' veya 'H' tuşlarına basın.\n{ad_soyad}",
                    border_style="red"
                )
            )

# ---------- Ana Fonksiyon ----------
def Ogrencileri_Silme_Onayi(sozlukListesi: list) -> list[tuple[dict, bool]]:
    layout = Layout()

    # Ana layout'u dikey (yan yana) böl -> sol ve sağ
    layout.split_row(
        Layout(name="left", ratio=2),   # solda tablo olabilir
        Layout(name="right", ratio=4)   # sağda onay penceresi
    )
    layout["left"].split_column(
        Layout(name="top", ),
        Layout(name="bottom", size=6),
        Layout(name="orta", size=6),
    )
    # Sağ kısmı yatay (alt alta) böl -> top ve bottom
    layout["right"].split_column(
        Layout(name="bottom", size=6),
        Layout(name="top", ),
        
    )

    # Solda tabloyu gösterelim
    layout["left"].update(top_panel(sozlukListesi))

    results = []
    with Live(layout, console=c, screen=True, refresh_per_second=10):
        for ogr in sozlukListesi:
            sonuc = Evet_Hayir_OnayiAl(ogr, layout)
            results.append((ogr, sonuc))

    return results


