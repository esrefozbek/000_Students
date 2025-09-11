#breakpoint()
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import print, box

console = Console()
bulunanlar = []


from rich.console import Console
from rich.table import Table
from rich.live import Live
import time

console = Console()

# Öğrenci kayıtları (örnek)
veri = {
    1: {"id": 1, "ad": "Fahrettin", "soyad": "Cürekli", "numara": 1653, "dogum_tarihi": "1970", "sinif": "5g", "kayit_tarihi": "02/09/2025 23:12:20"},
    2: {"id": 2, "ad": "Zeynep", "soyad": "Karakurt", "numara": 1654, "dogum_tarihi": "2008", "sinif": "6a", "kayit_tarihi": "02/09/2025 23:13:01"},
    12: {"id": 12, "ad": "Ece", "soyad": "Bozkurt", "numara": 1664, "dogum_tarihi": "2009", "sinif": "5e", "kayit_tarihi": "02/09/2025 23:18:50"}
}

# Bulunan öğrencileri tutar
bulunanlar = []

def tabloyu_olustur():
    table = Table(title="🔎 BULUNAN ÖĞRENCİLER TABLOSU", box=box.HORIZONTALS)
    table.add_column("Sıra No")
    table.add_column("Id")
    table.add_column("Ad")
    table.add_column("Soyad")
    table.add_column("Numarası")
    table.add_column("Doğ.Tar.")
    table.add_column("Sınıf")
    table.add_column("Kayıt Tarihi")

    for i, ogr in enumerate(bulunanlar):
        table.add_row(
            str(i),
            str(ogr["id"]),
            ogr["ad"],
            ogr["soyad"],
            str(ogr["numara"]),
            ogr["dogum_tarihi"],
            ogr["sinif"],
            ogr["kayit_tarihi"]
        )
    return table

def arama_yap(ids):
    with Live(tabloyu_olustur(), refresh_per_second=4, console=console) as live:
        for id in ids:
            if id in veri:
                bulunanlar.append(veri[id])
                live.update(tabloyu_olustur())
            else:
                console.print(f"[red]❌ {id} id'li öğrenci bulunamadı[/]")
            time.sleep(2.5)

# Örnek arama
arama_yap([1, 2, 12])
