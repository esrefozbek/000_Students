import time
import keyboard
from rich.progress import Progress, BarColumn, TimeRemainingColumn, TextColumn
from rich.console import Console

console = Console()

def geri_say_bar(sure_saniye: int, aciklama: str) -> bool:
    with Progress(
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=None),
        TimeRemainingColumn(),
    ) as progress:
        task = progress.add_task(aciklama, total=sure_saniye)

        for _ in range(sure_saniye):
            if keyboard.is_pressed('esc'):
                progress.stop()
                console.print("[red]🛑 ESC'ye basıldı, işlem iptal edildi.[/red]")
                return False
            time.sleep(1)
            progress.update(task, advance=1)

    return True

def pomodoro_dongusu(pomodoro_sayisi: int = 4, calisma_suresi: int = 25*60, kisa_mola: int = 5*60, uzun_mola: int = 15*60):
    for dongu in range(1, pomodoro_sayisi + 1):
        console.rule(f"[green]🍅 Pomodoro {dongu}")
        
        devam = geri_say_bar(calisma_suresi, f"💼 Odaklan! ({calisma_suresi // 60} dk)")
        if not devam:
            return

        if dongu < pomodoro_sayisi:
            console.print(f"[cyan]⏳ Kısa mola başlıyor... ({kisa_mola // 60} dk)[/cyan]")
            devam = geri_say_bar(kisa_mola, "☕ Kısa Mola")
            if not devam:
                return
        else:
            console.print(f"[magenta]🎉 Tüm pomodorolar tamam! Şimdi uzun mola. ({uzun_mola // 60} dk)[/magenta]")
            geri_say_bar(uzun_mola, "🛌 Uzun Mola")

    console.print("[bold green]✅ Pomodoro seansı tamamlandı![/bold green]")

if __name__ == "__main__":
    # Daha hızlı test etmek için süreleri düşürebilirsin:
    pomodoro_dongusu(
        pomodoro_sayisi=4,
        calisma_suresi=25,  # gerçek kullanırken 25*60 yap
        kisa_mola=5,
        uzun_mola=10
    )
