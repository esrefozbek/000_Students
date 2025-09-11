import time
import keyboard
from rich.progress import Progress, BarColumn, TimeRemainingColumn, TextColumn
from rich.console import Console;c = Console()




def GeriSayar(sure_saniye: int, aciklama: str) -> bool:
    with Progress(
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=None),
        TimeRemainingColumn(),
    ) as progress:
        task = progress.add_task(aciklama, total=sure_saniye)

        for _ in range(sure_saniye):
            if keyboard.is_pressed('esc'):
                progress.stop()
                c.print("[red]🛑 ESC'ye basıldı, işlem iptal edildi.[/red]")
                return False
            time.sleep(1)
            progress.update(task, advance=1)

    return True


