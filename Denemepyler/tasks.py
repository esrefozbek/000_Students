import requests
import time
from rich.console import Console, Group  # ✅ Group eklendi: listeleri render edilebilir hale getirmek için
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.spinner import Spinner
from rich.layout import Layout
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn, TimeElapsedColumn

console = Console()

API_URL = "https://jsonplaceholder.typicode.com/todos"

def fetch_tasks():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        todos = response.json()
        # İlk 5 görevi alıyoruz örnek için
        tasks = []
        for t in todos[:5]:
            tasks.append({
                "name": t["title"],
                "step": 5 if t["completed"] else 2,  # tamamlandıysa 5, değilse 2 adım yapıldı gibi
                "status": "tamamlandı" if t["completed"] else "çalışıyor",
                "max_steps": 5,
                "retry": 0,
                "log": []
            })
        return tasks
    except requests.RequestException as e:
        console.print(f"[red]API isteği başarısız: {e}[/red]")
        return []

def build_layout(tasks_data):
    layout = Layout()
    layout.split(
        Layout(name="ust", size=5),
        Layout(name="orta", ratio=2),
        Layout(name="alt", ratio=1)
    )

    # ✅ Spinner grubu oluşturuluyor
    spinner_group = []
    for task in tasks_data:
        name = task.get("name", "Bilinmiyor")
        status = task.get("status", "bilinmiyor")
        spinner_style = "dots"
        spinner = Spinner(spinner_style, text=f"{name} — {status}")
        panel = Panel(spinner, title=name[:20], border_style="green" if status == "tamamlandı" else "yellow")
        spinner_group.append(panel)

    # ❌ Hatalı: Panel içine liste konulamaz: Panel(spinner_group)
    # ✅ Doğru: Group(*spinner_group) ile listeyi renderable hale getiriyoruz
    layout["ust"].update(Panel(Group(*spinner_group), title="Görevler", border_style="blue"))

    # ✅ Progress bar ayarları
    progress = Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.fields[name]}"),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn()
    )
    task_ids = {}
    for task in tasks_data:
        name = task.get("name", "Bilinmiyor")
        max_steps = task.get("max_steps", 5)
        task_ids[name] = progress.add_task("", total=max_steps, name=name)

    for task in tasks_data:
        name = task.get("name", "Bilinmiyor")
        step = task.get("step", 0)
        progress.update(task_ids[name], completed=step)

    # ✅ Tablo grubu oluşturuluyor
    tablo_group = []
    for task in tasks_data:
        name = task.get("name", "Bilinmiyor")
        step = task.get("step", 0)
        max_steps = task.get("max_steps", 5)
        status = task.get("status", "bilinmiyor")
        retry = task.get("retry", 0)

        table = Table(title=f"{name[:20]} Durum Tablosu", expand=True)
        table.add_column("Adım", justify="center", style="cyan")
        table.add_column("Durum", style="magenta")

        for s in range(1, max_steps + 1):
            if s < step:
                table.add_row(str(s), "✅ Tamamlandı")
            elif s == step:
                table.add_row(str(s), "⏳ İşleniyor..." if status != "tamamlandı" else "✅ Tamamlandı")
            else:
                table.add_row(str(s), "-")

        if retry > 0:
            table.caption = f"[yellow]{retry} kez yeniden denendi[/yellow]"

        panel = Panel(table, border_style="cyan")
        tablo_group.append(panel)

    # ❌ Hatalı: Panel(tablo_group)
    # ✅ Doğru: Group(*tablo_group) + progress ile birlikte
    layout["orta"].update(Panel(Group(progress, *tablo_group), title="Görev Durumları", border_style="magenta"))

    # ✅ Log paneli (şimdilik sabit içerik)
    layout["alt"].update(Panel("[dim]Henüz log yok...[/dim]", title="Log Paneli", border_style="blue"))

    return layout


def main():
    with Live(console=console, refresh_per_second=2, screen=True) as live:
        while True:
            tasks = fetch_tasks()
            if not tasks:
                console.print("[red]Görev verisi alınamadı, tekrar denenecek...[/red]")
            else:
                live.update(build_layout(tasks))
            time.sleep(3)

if __name__ == "__main__":
    main()
