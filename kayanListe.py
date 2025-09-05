from rich.live import Live
from rich.console import Console
from time import sleep
import keyboard

console = Console()

def kayma():
    liste = ["Eşref", "Ömer", "Ahmet", "Mehmet", "Ali", "Veli", "Ayşe", "Fatma", "Can"] # Örnek liste: [1, 2, 3, 4, 5]

    with Live(f"{liste}", refresh_per_second=10, console=console) as live:
        while True:
            if keyboard.is_pressed('left'):
                liste = liste[1:] + [liste[0]]  # sola kaydır
                live.update(f"{liste}")
                keyboard.wait('left', suppress=True)

            elif keyboard.is_pressed('right'):
                liste = [liste[-1]] + liste[0:-1]  # sağa kaydır
                live.update(f"{liste}")
                keyboard.wait('right', suppress=True)

            elif keyboard.is_pressed('esc'):
                console.print("\n[red]Çıkılıyor...[/red]")
                break

            sleep(0.05)  # CPU'yu dinlendir

if __name__ == "__main__":
    kayma()
