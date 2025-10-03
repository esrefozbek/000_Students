from rich.console import Console, Group
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table

console = Console()

# Örnek öğrenci listesi
ogrenciler = [
    {"Id": i, "Ad": f"Ad{i}", "Soyad": f"Soyad{i}", "Sınıf": f"{9+i%4}A"}
    for i in range(1, 31)   # 30 öğrenci örneği
]

# --- Sayfalama ---
def sayfalara_bol(liste, sayfa_boyutu):
    for i in range(0, len(liste), sayfa_boyutu):
        yield liste[i:i+sayfa_boyutu]

# --- Panel oluşturucu ---
def ogrenci_paneli(ogr):
    paneller = [
        Panel(str(ogr["Id"]), title="Id", border_style="yellow", width=12),
        Panel(ogr["Ad"], title="Ad", border_style="green", width=12),
        Panel(ogr["Soyad"], title="Soyad", border_style="blue", width=12),
        Panel(ogr["Sınıf"], title="Sınıf", border_style="magenta", width=12),
    ]
    return Panel(Group(*paneller), title=f"Öğrenci {ogr['Id']}", border_style="cyan")

# --- Tablo oluşturucu ---
def ogrenci_tablosu(liste):
    tablo = Table(title="Öğrenci Listesi", expand=True)
    tablo.add_column("Id", style="yellow", justify="center")
    tablo.add_column("Ad", style="green")
    tablo.add_column("Soyad", style="blue")
    tablo.add_column("Sınıf", style="magenta", justify="center")

    for ogr in liste:
        tablo.add_row(str(ogr["Id"]), ogr["Ad"], ogr["Soyad"], ogr["Sınıf"])
    return tablo

# --- Filtreleme ---
def filtrele(liste, kelime):
    kelime = kelime.lower()
    return [
        ogr for ogr in liste
        if kelime in ogr["Ad"].lower()
        or kelime in ogr["Soyad"].lower()
        or kelime in ogr["Sınıf"].lower()
        or kelime == str(ogr["Id"])
    ]

# --- Sıralama ---
def sirala(liste, alan, ters=False):
    try:
        return sorted(liste, key=lambda x: x[alan], reverse=ters)
    except KeyError:
        return liste

# --- Ana döngü ---
sayfa_boyutu = 4
aktif_sayfa = 0
arama = ""
aktif_liste = ogrenciler[:]
siralama = ("Id", False)   # default: Id ASC
mod = "panel"              # varsayılan görünüm

while True:
    # filtre uygula
    filtreli = filtrele(aktif_liste, arama) if arama else aktif_liste
    # sıralama uygula
    filtreli = sirala(filtreli, siralama[0], siralama[1])
    # sayfalara böl
    sayfalar = list(sayfalara_bol(filtreli, sayfa_boyutu))
    toplam_sayfa = len(sayfalar) if sayfalar else 1
    aktif_sayfa = min(aktif_sayfa, toplam_sayfa-1)

    console.clear()
    console.rule(f"[bold magenta]Öğrenciler (Sayfa {aktif_sayfa+1}/{toplam_sayfa})[/]")

    if sayfalar:
        if mod == "panel":
            icerikler = [ogrenci_paneli(ogr) for ogr in sayfalar[aktif_sayfa]]
            console.print(Columns(icerikler, padding=2, expand=True))
        else:
            tablo = ogrenci_tablosu(sayfalar[aktif_sayfa])
            console.print(tablo)
    else:
        console.print("[red]Eşleşen öğrenci bulunamadı.[/]")

    console.print(
        f"\n[green]Toplam Öğrenci: {len(filtreli)}[/] "
        f"(Arama: '{arama or 'yok'}', Sıralama: {siralama[0]} {'DESC' if siralama[1] else 'ASC'}, "
        f"Mod: {mod.upper()})"
    )

    # kullanıcıdan komut al
    komut = console.input(
        "\n[cyan][n] Sonraki | [p] Önceki | [f] Filtre | [c] Temizle | [s] Sırala | [m] Mod | [q] Çıkış: [/] "
    )

    if komut == "n" and aktif_sayfa < toplam_sayfa-1:
        aktif_sayfa += 1
    elif komut == "p" and aktif_sayfa > 0:
        aktif_sayfa -= 1
    elif komut == "f":
        arama = console.input("[yellow]Arama kelimesi gir: [/]").strip()
        aktif_sayfa = 0
    elif komut == "c":
        arama = ""
        aktif_sayfa = 0
    elif komut == "s":
        alan = console.input("[blue]Sıralama alanı (Id, Ad, Soyad, Sınıf): [/]").strip()
        yon = console.input("[blue]Yön (a=ASC, d=DESC): [/]").strip().lower()
        siralama = (alan if alan in ["Id", "Ad", "Soyad", "Sınıf"] else "Id", yon == "d")
        aktif_sayfa = 0
    elif komut == "m":
        mod = "tablo" if mod == "panel" else "panel"
    elif komut == "q":
        break
