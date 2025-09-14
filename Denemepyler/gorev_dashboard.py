import threading
import time
import random
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.spinner import Spinner
from rich.table import Table
from rich.layout import Layout
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn, TimeElapsedColumn

console = Console()

# Görev konfigürasyonu
gorev_sayisi = 4
adim_sayisi = 15
gorevler = [f"Görev {i+1}" for i in range(gorev_sayisi)]
spinner_turleri = ["dots", "line", "bouncingBar", "arc", "clock", "earth", "moon", "weather"]

# Ortak veri yapıları
gorev_durumlari = {gorev: {"adim": 0, "durum": "çalışıyor", "hata": False, "retry": 0} for gorev in gorevler}
log_kayitlari = []  # Log paneli için

# Progress bar'ları hazırlıyoruz
progress = Progress(
    SpinnerColumn(),
    TextColumn("[bold blue]{task.fields[gorev]}"),
    BarColumn(bar_width=None),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeElapsedColumn()
)
task_ids = {gorev: progress.add_task("", total=adim_sayisi, gorev=gorev) for gorev in gorevler}

def log_yaz(gorev, mesaj):
    timestamp = time.strftime("%H:%M:%S")
    log_kayitlari.append(f"[{timestamp}] [cyan]{gorev}:[/cyan] {mesaj}")

def gorev_isle(gorev_adi: str):
    for i in range(1, adim_sayisi + 1):
        # Rastgele hata simülasyonu (%20 ihtimalle)
        if random.random() < 0.2:
            log_yaz(gorev_adi, f"[red]HATA![/red] {i}. adımda sorun oluştu. Tekrar deneniyor...")
            gorev_durumlari[gorev_adi]["retry"] += 1
            time.sleep(1)
            continue

        time.sleep(0.5 + 0.2 * i)
        gorev_durumlari[gorev_adi]["adim"] = i
        progress.update(task_ids[gorev_adi], advance=1)
        log_yaz(gorev_adi, f"{i}. adım başarıyla tamamlandı.")

    gorev_durumlari[gorev_adi]["durum"] = "tamamlandı"
    log_yaz(gorev_adi, f"[green]TAMAMLANDI[/green]")

def build_layout() -> Layout:
    layout = Layout()
    layout.split(
        Layout(name="ust", size=6),
        Layout(name="orta", size=12),
        Layout(name="alt", ratio=1)
    )

    # Spinnerlar
    spinner_group = []
    for i, gorev in enumerate(gorevler):
        durum = gorev_durumlari[gorev]["durum"]
        spinner_tipi = spinner_turleri[i % len(spinner_turleri)]
        spinner = Spinner(spinner_tipi, text=f"[green]{gorev} {'TAMAMLANDI' if durum == 'tamamlandı' else 'ÇALIŞIYOR...'}")
        panel = Panel(spinner, title=gorev, border_style="green" if durum == "tamamlandı" else "yellow")
        spinner_group.append(panel)
    layout["ust"].update(Group(*spinner_group))

    # Tablo + Progress bar
    tablo_group = []
    for gorev in gorevler:
        step = gorev_durumlari[gorev]["adim"]
        durum = gorev_durumlari[gorev]["durum"]
        retry = gorev_durumlari[gorev]["retry"]

        table = Table(title=f"{gorev} Durumu", expand=True)
        table.add_column("Adım", justify="center", style="cyan")
        table.add_column("Durum", style="magenta")

        for s in range(1, adim_sayisi + 1):
            if s < step:
                table.add_row(str(s), "✅ Tamamlandı")
            elif s == step:
                table.add_row(str(s), "⏳ İşleniyor..." if durum != "tamamlandı" else "✅ Tamamlandı")
            else:
                table.add_row(str(s), "-")

        if retry > 0:
            table.caption = f"[yellow]{retry} kez tekrarlandı."

        panel = Panel(table, border_style="cyan")
        tablo_group.append(panel)

    layout["orta"].update(Group(progress, *tablo_group))

    # Log panel
    log_text = "\n".join(log_kayitlari[-10:]) or "[dim]Henüz log yok...[/dim]"
    layout["alt"].update(Panel(log_text, title="Log Paneli", border_style="blue"))

    return layout

# Görevleri başlat
threads = []
for gorev in gorevler:
    thread = threading.Thread(target=gorev_isle, args=(gorev,), daemon=True)
    thread.start()
    threads.append(thread)

with Live(build_layout(), refresh_per_second=10, screen=True) as live:
    while any(g["durum"] != "tamamlandı" for g in gorev_durumlari.values()):
        live.update(build_layout())
        time.sleep(0.5)

    live.update(build_layout())

console.print(f"\n[bold green]✅ Tüm görevler başarıyla tamamlandı![/bold green]")
