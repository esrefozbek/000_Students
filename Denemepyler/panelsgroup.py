from rich.console import Console, Group
from rich.panel import Panel
from rich.columns import Columns

console = Console()

ust_panel = Panel("Ben üst panelim", title="Üst", border_style="green")
alt_panel = Panel("Ben alt panelim", title="Alt", border_style="blue")

# İki paneli grupla
birlesik = Panel(
    Group(ust_panel, alt_panel),  # içeriğe panelleri alt alta koyduk
    title="Dış Panel", 
    border_style="magenta"
)

console.print(birlesik)


#~                                                                              




p1 = Panel("Birinci", border_style="red")
p2 = Panel("İkinci", border_style="green")
p3 = Panel("Üçüncü", border_style="blue")

# Yan yana
console.print(Columns([p1, p2, p3], padding=2))

# Alt alta
console.print(Group(p1, p2, p3))

# Alt alta panelleri TEK PANEL içine almak
console.print(Panel(Group(p1, p2, p3), title="Dış Panel"))






#~                                                                          



from rich.console import Console, Group
from rich.panel import Panel
from rich.columns import Columns

console = Console()

# Örnek öğrenci kayıtları
ogrenciler = [
    {"Id": 1, "Ad": "Ayşe", "Soyad": "Yılmaz", "Sınıf": "10A"},
    {"Id": 2, "Ad": "Mehmet", "Soyad": "Demir", "Sınıf": "11B"},
    {"Id": 3, "Ad": "Fatma", "Soyad": "Kara", "Sınıf": "9C"},
]

# Her öğrenci için alt alta paneller oluştur
icerikler = []
for ogr in ogrenciler:
    paneller = [
        Panel(str(ogr["Id"]), title="Id", border_style="yellow", width=12),
        Panel(ogr["Ad"], title="Ad", border_style="green", width=12),
        Panel(ogr["Soyad"], title="Soyad", border_style="blue", width=12),
        Panel(ogr["Sınıf"], title="Sınıf", border_style="magenta", width=12),
    ]
    # Öğrencinin tüm bilgilerini alt alta grupla
    ogr_group = Group(*paneller)
    # Tek panel içinde öğrenci bilgileri
    ogr_panel = Panel(ogr_group, title=f"Öğrenci {ogr['Id']}", border_style="cyan")
    icerikler.append(ogr_panel)

# Tüm öğrencileri yan yana kolonlara koy
console.print(Columns(icerikler, padding=3, expand=True))


#~                                                                            

from rich.console import Console, Group
from rich.panel import Panel
from rich.columns import Columns

console = Console()

# Örnek büyük öğrenci listesi
ogrenciler = [
    {"Id": i, "Ad": f"Ad{i}", "Soyad": f"Soyad{i}", "Sınıf": f"{9+i%4}A"}
    for i in range(1, 21)   # 20 öğrenci örneği
]

# --- Sayfalama fonksiyonu ---
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

# --- Ana döngü ---
sayfa_boyutu = 4  # her sayfada 4 öğrenci
sayfalar = list(sayfalara_bol(ogrenciler, sayfa_boyutu))
toplam_sayfa = len(sayfalar)
aktif_sayfa = 0

while True:
    console.clear()
    console.rule(f"[bold magenta]Öğrenciler (Sayfa {aktif_sayfa+1}/{toplam_sayfa})[/]")
    
    # aktif sayfadaki öğrenciler
    icerikler = [ogrenci_paneli(ogr) for ogr in sayfalar[aktif_sayfa]]
    console.print(Columns(icerikler, padding=2, expand=True))
    
    # kullanıcıdan komut al
    komut = console.input("\n[cyan][n] Sonraki | [p] Önceki | [q] Çıkış: [/]")
    if komut == "n" and aktif_sayfa < toplam_sayfa-1:
        aktif_sayfa += 1
    elif komut == "p" and aktif_sayfa > 0:
        aktif_sayfa -= 1
    elif komut == "q":
        break


#~                                                                                            

from rich.console import Console, Group
from rich.panel import Panel
from rich.columns import Columns

console = Console()

# Örnek öğrenci listesi
ogrenciler = [
    {"Id": i, "Ad": f"Ad{i}", "Soyad": f"Soyad{i}", "Sınıf": f"{9+i%4}A"}
    for i in range(1, 31)   # 30 öğrenci örneği
]

# --- Sayfalama fonksiyonu ---
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

# --- Filtreleme fonksiyonu ---
def filtrele(liste, kelime):
    kelime = kelime.lower()
    return [
        ogr for ogr in liste
        if kelime in ogr["Ad"].lower()
        or kelime in ogr["Soyad"].lower()
        or kelime in ogr["Sınıf"].lower()
        or kelime == str(ogr["Id"])
    ]

# --- Ana döngü ---
sayfa_boyutu = 4
aktif_sayfa = 0
aktif_liste = ogrenciler[:]   # başlangıçta tüm liste
arama = ""

while True:
    # listeyi filtrele
    filtreli = filtrele(aktif_liste, arama) if arama else aktif_liste
    sayfalar = list(sayfalara_bol(filtreli, sayfa_boyutu))
    toplam_sayfa = len(sayfalar) if sayfalar else 1
    aktif_sayfa = min(aktif_sayfa, toplam_sayfa-1)

    console.clear()
    console.rule(f"[bold magenta]Öğrenciler (Sayfa {aktif_sayfa+1}/{toplam_sayfa})[/]")
    
    if sayfalar:
        icerikler = [ogrenci_paneli(ogr) for ogr in sayfalar[aktif_sayfa]]
        console.print(Columns(icerikler, padding=2, expand=True))
    else:
        console.print("[red]Eşleşen öğrenci bulunamadı.[/]")
    
    console.print(f"\n[green]Toplam Öğrenci: {len(filtreli)}[/] (Arama: '{arama or 'yok'}')")

    # kullanıcıdan komut al
    komut = console.input("\n[cyan][n] Sonraki | [p] Önceki | [f] Filtre | [c] Temizle | [q] Çıkış: [/] ")

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
    elif komut == "q":
        break







