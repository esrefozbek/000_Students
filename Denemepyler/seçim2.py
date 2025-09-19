from rich.console import Console
from rich.panel import Panel
from rich import box
import readchar

# Örnek veri
bulunanlarListesi = [
    {"ad": "Ahmet", "soyad": "Yılmaz"},
    {"ad": "Ayşe", "soyad": "Kara"},
    {"ad": "Mehmet", "soyad": "Demir"},
    {"ad": "Elif", "soyad": "Çelik"},
    {"ad": "Can", "soyad": "Yıldız"},
]

console = Console()
secilen_index = 0
secili_satirlar = set()  # Çoklu seçimleri tutacak

def ekran_yenile():
    console.clear()
    console.print(Panel("⬇️ [bold]Öğrenci Seçimi[/bold] ⬇️", style="cyan", box=box.ROUNDED))

    for i, ogr in enumerate(bulunanlarListesi):
        adSoyad = f"{ogr['ad']} {ogr['soyad']}"

        işaret = "✅" if i in secili_satirlar else "  "
        gösterim = f"{işaret} {adSoyad}"

        if i == secilen_index:
            console.print(f"[reverse]{gösterim}[/reverse]")
        else:
            console.print(gösterim)

    console.print("\n[dim]↑ ↓: Gezin | Space: Seç/Çıkar | Enter: Onayla | Esc: Çıkış[/dim]")

while True:
    ekran_yenile()
    key = readchar.readkey()

    if key == readchar.key.UP:
        secilen_index = (secilen_index - 1) % len(bulunanlarListesi)

    elif key == readchar.key.DOWN:
        secilen_index = (secilen_index + 1) % len(bulunanlarListesi)

    elif key == readchar.key.SPACE:
        if secilen_index in secili_satirlar:
            secili_satirlar.remove(secilen_index)
        else:
            secili_satirlar.add(secilen_index)

    elif key == readchar.key.ENTER:
        console.clear()
        console.print("[bold green]✅ Seçilen Öğrenciler:[/bold green]")
        for i in secili_satirlar:
            ogr = bulunanlarListesi[i]
            console.print(f"- {ogr['ad']} {ogr['soyad']}")
        break

    elif key == readchar.key.ESC:
        console.print("[bold red]❌ Seçim iptal edildi.[/bold red]")
        break
