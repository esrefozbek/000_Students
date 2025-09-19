from rich.console import Console
from rich.panel import Panel
from rich import box
import readchar

bulunanlarListesi = [
    {"ad": "Ahmet", "soyad": "Yılmaz"},
    {"ad": "Ayşe", "soyad": "Kara"},
    {"ad": "Mehmet", "soyad": "Demir"},
    {"ad": "Elif", "soyad": "Çelik"},
]

console = Console()
secilen_index = 0

def ekrani_guncelle():
    console.clear()
    console.print(Panel("⬇️ [bold]Öğrenci Seçimi[/bold] ⬇️", style="cyan", box=box.ROUNDED))

    for i, ogr in enumerate(bulunanlarListesi):
        adSoyad = f"{ogr['ad']} {ogr['soyad']}"
        if i == secilen_index:
            console.print(f"[bold green]> {adSoyad} <[/bold green]")
        else:
            console.print(f"  {adSoyad}")

    console.print("\n[dim]Yukarı/Aşağı: Seç | Enter: Onayla | Esc: Çıkış[/dim]")

while True:
    ekrani_guncelle()
    key = readchar.readkey()

    if key == readchar.key.UP:
        secilen_index = (secilen_index - 1) % len(bulunanlarListesi)
    elif key == readchar.key.DOWN:
        secilen_index = (secilen_index + 1) % len(bulunanlarListesi)
    elif key == readchar.key.ENTER:
        console.print(f"\n✅ Seçilen öğrenci: [bold]{bulunanlarListesi[secilen_index]['ad']}[/bold]")
        break
    elif key == readchar.key.ESC:
        console.print("\n❌ Seçim iptal edildi.")
        break
