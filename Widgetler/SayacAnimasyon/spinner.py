from rich.console import Console
from rich.spinner import Spinner
import Widgetler.randomRenk as RENK
import time
import random
c = Console()



def spinner(duration, WhichText:int): 
    text="0"    # sayı ve text gönder
    if WhichText==1:
        text=f"[{RENK.randomRENK()}] 🐳 🐳 🐳 Girdiler Veri tabanına Ekleniyor, taaa tabana ...**[/]"
    if WhichText==2:
        text=f"[{RENK.randomRENK()}] 🎯🎯🎯 Siliniyor...[/]"
    if WhichText==3:
        text=f"[{RENK.randomRENK()}] 💻💻💻 Düzeltiliyor, eccük sabırlı ol...[/]"
    if WhichText==4:
        text=f"[{RENK.randomRENK()}]] Bilgilerin kaydı gerçekleşiyor......💬💬💬[/]"
    if WhichText==5:
        text=f"[{RENK.randomRENK()}] Bulunanlar yükleniyor...➕➕➕[/]"
    if WhichText==6:
        text=f"[{RENK.randomRENK()}] Kayıt yapılacak veri girilmedi, ana menüye dönülüyor 🤫🤫🤫😂[/]"   
    if WhichText==7:
        text=f"[{RENK.randomRENK()}] AnaMenüye Hicret ediliyor...[/]" 
    if WhichText==8:
        text=f"[{RENK.randomRENK()}]⚠️ ID çatışması tespit edildi.[/] [bold yellow] Biraz bekle, düzeltip geliyorum.⚠️[/]"
    
       
    with c.status(text, spinner="line"):
        time.sleep(duration)  # burada uzun süren işlemin olur

       

        

from rich._spinners import SPINNERS

spinnersList=[]

def spinnersGecidi():
    for name in SPINNERS.keys():
        spinnersList.append(name)
       # with c.status(f"[bold cyan]Spinner: {name}", spinner=name):
        #    time.sleep(3)
#c.print(spinnersList)


# Rastgele spinner seçen fonksiyon
def random_spinners():
    return random.choice(spinnersList)



def randomSonuc():
    spinnersGecidi()
    name=random_spinners()
    return name



def dene_spinner():
    name=randomSonuc()
    with c.status(f"[bold cyan]Spinner:{name}", spinner=name):
        time.sleep(3)





# from rich.console import Console, Group
# from rich.live import Live
# from rich.spinner import Spinner
# from rich.text import Text
# import time

# console = Console()

# with Live(refresh_per_second=10) as live:
#     for i in range(4):
#         spinner = Spinner("dots", text=f"{i+1}. işlem yapılıyor...")
#         live.update(spinner)
#         time.sleep(0.5)

# console.print("[green]İşlem tamamlandı.")






# from rich.console import Console, Group
# from rich.live import Live
# from rich.spinner import Spinner
# from rich.text import Text
# import time

# console = Console()

# with Live(refresh_per_second=10) as live:
#     for i in range(10):
#         spinner = Spinner("dots", text="Bekleniyor...")
#         status_text = Text(f"[{i+1}/10] İşlem yapılıyor...")
#         group = Group(spinner, status_text)
#         live.update(group)
#         time.sleep(1)

# console.print("[green]İşlem tamamlandı.")


# from rich.console import Console, Group
# from rich.live import Live
# from rich.spinner import Spinner
# from rich.table import Table
# import time

# console = Console()

# def build_table(step: int) -> Table:
#     """Adım adım satır eklenen tablo."""
#     table = Table(title="Veri Yükleme Tablosu")
#     table.add_column("ID", justify="right", style="cyan", no_wrap=True)
#     table.add_column("Durum", style="magenta")

#     for i in range(1, step + 1):
#         table.add_row(str(i), "Yükleniyor...")

#     return table



# with Live(refresh_per_second=10) as live:
#     for step in range(1, 6):
#         spinner = Spinner("dots", text=f"[bold green]{step}. adım işleniyor...")
#         table = build_table(step)
#         group = Group(spinner, table)
#         live.update(group)
#         time.sleep(1)

# console.print("[bold green]✅ İşlem tamamlandı!")




# from rich.console import Console
# from rich.layout import Layout
# from rich.spinner import Spinner
# from rich.table import Table
# from rich.panel import Panel
# from rich.live import Live
# import time

# console = Console()

# def build_table(step: int) -> Table:
#     table = Table(title="Veri Yükleme Durumu")
#     table.add_column("ID", justify="right", style="cyan", no_wrap=True)
#     table.add_column("Durum", style="magenta")

#     for i in range(1, step + 1):
#         table.add_row(str(i), "Yükleniyor..." if i < step else "✅ Tamamlandı")

#     return table

# def build_layout(step: int) -> Layout:
#     layout = Layout()

#     # Ekranı ikiye böl (yatay)
#     layout.split_row(
#         Layout(name="left", ratio=1),
#         Layout(name="right", ratio=2),
#     )

#     # Sol: Spinner (panel içinde)
#     spinner = Spinner("dots", text=f"[bold green]{step}. adım işleniyor...")
#     layout["left"].update(Panel(spinner, title="İşlem Durumu", border_style="green"))

#     # Sağ: Tablo
#     table = build_table(step)
#     layout["right"].update(Panel(table, title="Yükleme Tablosu", border_style="cyan"))

#     return layout

# # Ana döngü
# with Live(build_layout(0), refresh_per_second=10, screen=True) as live:
#     for step in range(1, 16):
#         live.update(build_layout(step))
#         time.sleep(1)

# console.print("\n[bold green]✅ Tüm işlemler tamamlandı!")





# from rich.console import Console
# from rich.layout import Layout
# from rich.spinner import Spinner
# from rich.panel import Panel
# from rich.table import Table
# from rich.live import Live
# import time

# console = Console()

# def build_table(name: str, step: int) -> Table:
#     table = Table(title=f"{name} Görevi", expand=True)
#     table.add_column("ID", justify="right", style="cyan", no_wrap=True)
#     table.add_column("Durum", style="magenta")

#     for i in range(1, step + 1):
#         durum = "✅ Tamamlandı" if i < step else "⏳ Yükleniyor..."
#         table.add_row(str(i), durum)

#     return table

# def build_layout(step: int) -> Layout:
#     layout = Layout()

#     # Ana bölme: üst (spinnerlar) + alt (tablolar)
#     layout.split(
#         Layout(name="ust", size=5),
#         Layout(name="alt")
#     )

#     # Üst: 2 spinner yan yana
#     layout["ust"].split_row(
#         Layout(name="spinner1"),
#         Layout(name="spinner2")
#     )

#     spinner1 = Spinner("dots", text="[green]1. görev işleniyor...")
#     spinner2 = Spinner("line", text="[cyan]2. görev işleniyor...")

#     layout["spinner1"].update(Panel(spinner1, title="Görev 1", border_style="green"))
#     layout["spinner2"].update(Panel(spinner2, title="Görev 2", border_style="cyan"))

#     # Alt: 2 tablo yan yana
#     layout["alt"].split_row(
#         Layout(name="tablo1"),
#         Layout(name="tablo2")
#     )

#     table1 = build_table("Görev 1", step)
#     table2 = build_table("Görev 2", step)

#     layout["tablo1"].update(Panel(table1, title="Görev 1 Tablosu", border_style="green"))
#     layout["tablo2"].update(Panel(table2, title="Görev 2 Tablosu", border_style="cyan"))

#     return layout

# # Terminal arayüzünü başlat
# with Live(build_layout(0), refresh_per_second=10, screen=True) as live:
#     for step in range(1, 16):
#         live.update(build_layout(step))
#         time.sleep(1)

# console.print("\n[bold green]✅ Tüm görevler başarıyla tamamlandı!")



# from rich.console import Console
# from rich.layout import Layout
# from rich.spinner import Spinner
# from rich.panel import Panel
# from rich.table import Table
# from rich.live import Live
# import time

# console = Console()

# # Görev isimleri (dinamik şekilde arttırılabilir)
# gorev_sayisi = 3  # 🟢 Buradan artır: 2, 4, 6 vs.
# gorevler = [f"Görev {i+1}" for i in range(gorev_sayisi)]
# spinner_turleri = ["dots", "line", "bouncingBar", "arc", "clock", "earth", "moon", "weather"]


# def build_table(gorev_adi: str, step: int) -> Table:
#     table = Table(title=f"{gorev_adi} Tablosu", expand=True)
#     table.add_column("ID", justify="right", style="cyan", no_wrap=True)
#     table.add_column("Durum", style="magenta")

#     for i in range(1, step + 1):
#         durum = "✅ Tamamlandı" if i < step else "⏳ Yükleniyor..."
#         table.add_row(str(i), durum)

#     return table


# def build_layout(step: int) -> Layout:
#     layout = Layout()

#     # Üst: spinnerlar
#     layout.split(
#         Layout(name="ust", size=5),
#         Layout(name="alt")
#     )

#     # Üst kısmı görev sayısına göre yatay böl
#     spinner_bolmeler = [Layout(name=f"spinner_{i}") for i in range(len(gorevler))]
#     layout["ust"].split_row(*spinner_bolmeler)

#     # Spinnerları her bölmeye ekle
#     for i, gorev in enumerate(gorevler):
#         spinner_tipi = spinner_turleri[i % len(spinner_turleri)]
#         spinner = Spinner(spinner_tipi, text=f"[bold green]{gorev} çalışıyor...")
#         layout["ust"][f"spinner_{i}"].update(Panel(spinner, title=gorev, border_style="green"))

#     # Alt kısmı da aynı şekilde böl
#     tablo_bolmeler = [Layout(name=f"tablo_{i}") for i in range(len(gorevler))]
#     layout["alt"].split_row(*tablo_bolmeler)

#     for i, gorev in enumerate(gorevler):
#         tablo = build_table(gorev, step)
#         layout["alt"][f"tablo_{i}"].update(Panel(tablo, title=gorev + " Tablosu", border_style="cyan"))

#     return layout


# # 🧠 Simülasyon: Tüm görevlerde 5 adım var
# toplam_adim = 15

# with Live(build_layout(0), refresh_per_second=10, screen=True) as live:
#     for step in range(1, toplam_adim + 1):
#         live.update(build_layout(step))
#         time.sleep(1)

# console.print(f"\n[bold green]✅ {gorev_sayisi} görev başarıyla tamamlandı!")





# import threading
# import time
# from rich.console import Console
# from rich.live import Live
# from rich.panel import Panel
# from rich.spinner import Spinner
# from rich.table import Table
# from rich.layout import Layout

# console = Console()

# # Konfigürasyon
# gorev_sayisi = 4
# adim_sayisi = 25
# gorevler = [f"Görev {i+1}" for i in range(gorev_sayisi)]
# spinner_turleri = ["dots", "line", "bouncingBar", "arc", "clock", "earth", "moon", "weather"]

# # Görev durumları burada tutulur
# # Her görev için: {"adim": 0, "durum": "çalışıyor" | "tamamlandı"}
# gorev_durumlari = {gorev: {"adim": 0, "durum": "çalışıyor"} for gorev in gorevler}

# def gorev_isle(gorev_adi: str):
#     for i in range(1, adim_sayisi + 1):
#         time.sleep(1 + 0.2 * i)  # Farklı görevler farklı sürede ilerlesin
#         gorev_durumlari[gorev_adi]["adim"] = i
#     gorev_durumlari[gorev_adi]["durum"] = "tamamlandı"

# # Layout oluşturan fonksiyon
# def build_layout() -> Layout:
#     layout = Layout()
#     layout.split(
#         Layout(name="ust", size=5),
#         Layout(name="alt")
#     )

#     # Üst: Spinnerlar
#     spinner_bolmeler = [Layout(name=f"spinner_{i}") for i in range(gorev_sayisi)]
#     layout["ust"].split_row(*spinner_bolmeler)

#     # Alt: Tablolar
#     tablo_bolmeler = [Layout(name=f"tablo_{i}") for i in range(gorev_sayisi)]
#     layout["alt"].split_row(*tablo_bolmeler)

#     for i, gorev in enumerate(gorevler):
#         step = gorev_durumlari[gorev]["adim"]
#         durum = gorev_durumlari[gorev]["durum"]
#         spinner_tipi = spinner_turleri[i % len(spinner_turleri)]

#         spinner = Spinner(spinner_tipi, text=f"[green]{gorev} {'Tamamlandı' if durum == 'tamamlandı' else 'Çalışıyor...'}")
#         table = Table(title=f"{gorev} Durumu", expand=True)
#         table.add_column("Adım", justify="center", style="cyan")
#         table.add_column("Durum", style="magenta")

#         for s in range(1, adim_sayisi + 1):
#             if s < step:
#                 table.add_row(str(s), "✅ Tamamlandı")
#             elif s == step:
#                 if durum == "tamamlandı":
#                     table.add_row(str(s), "✅ Tamamlandı")
#                 else:
#                     table.add_row(str(s), "⏳ İşleniyor...")
#             else:
#                 table.add_row(str(s), "-")

#         layout[f"spinner_{i}"].update(Panel(spinner, title=gorev, border_style="green"))
#         layout[f"tablo_{i}"].update(Panel(table, title=f"{gorev} Tablosu", border_style="cyan"))

#     return layout






# # Görevleri başlat
# threads = []
# for gorev in gorevler:
#     thread = threading.Thread(target=gorev_isle, args=(gorev,), daemon=True)
#     thread.start()
#     threads.append(thread)

# # Live dashboard
# with Live(build_layout(), refresh_per_second=5, screen=True) as live:
#     while any(g["durum"] != "tamamlandı" for g in gorev_durumlari.values()):
#         live.update(build_layout())
#         time.sleep(0.5)

#     # Son halini bir kez daha göster
#     live.update(build_layout())

# console.print("\n[bold green]✅ Tüm görevler başarıyla tamamlandı!")
