import time, sys
import keyboard  # pip install keyboard
from rich.live import Live
from rich.text import Text
from rich.progress import Progress, BarColumn, TimeRemainingColumn, TextColumn
from rich.console import Console
console = Console()

def kronometre(saniye_sayisi: int =14 ):
    console.print("Kronometre başlıyor... (Enter'a basarsan durur)\n", style="bold cyan")
    
    for i in range(saniye_sayisi, 0, -1):
        sys.stdout.write('\033[2K\r')       # Satırı temizle ve başa dön
        sys.stdout.write(f"Geri sayım: {i}")
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write('\033[2K\r')  # Son satırı da temizle
    print("Bitti!")
    # if keyboard.is_pressed('enter'):
    #     console.print("\n[red]Enter'a basıldı, kronometre durduruldu.[/red]")
    #     break

def enter_kronometre(saniye_sayisi: int =14 ):
    console.print("Kronometre başlıyor... (Enter'a basarsan durur)\n", style="bold cyan")
    
    for i in range(saniye_sayisi, 0, -1):
        sys.stdout.write('\033[2K\r')       # Satırı temizle ve başa dön
        sys.stdout.write(f"Geri sayım: {i}")
        sys.stdout.flush()
        if keyboard.is_pressed('enter'):
            console.print("\n[red]Enter'a basıldı, kronometre durduruldu.[/red]")
            break       
        time.sleep(1)

    sys.stdout.write('\033[2K\r')  # Son satırı da temizle
    print("Bitti!")
        
        

def dongu():
    print("Başladı. Enter'a bastığında çıkılacak.\n")
    while True:
        print("Çalışıyor...")
        time.sleep(0.5)  # CPU'yu yormamak için biraz beklet

        if keyboard.is_pressed('enter'):
            print("Enter'a basıldı, çıkılıyor...")
            break

def enter_richile():
    with Live(refresh_per_second=10) as live:
        for i in range(15):
            live.update(Text(f"Sayaç: {i}", style="cyan"))
            time.sleep(1)
            if keyboard.is_pressed('enter'):
                live.update(Text("Enter'a basıldı, çıkılıyor...", style="bold red"))
                break
    print("Bitti!")


def richSayaç():
    with Live(refresh_per_second=10) as live:
        for i in range(11):
            live.update(f"[cyan]Sayaç: {i}[/cyan]")
            time.sleep(1)
    print("Bitti!")


def geri_say(saniye: int = 10, iptal_tusu: str = 'esc'):
    with Live(refresh_per_second=10) as live:
        for i in range(saniye, 0, -1):
            if keyboard.is_pressed(iptal_tusu):
                live.update(Text(f"[{iptal_tusu.upper()}] tuşuna basıldı, iptal edildi.", style="bold yellow"))
                break
            metin = Text(f"Kalan süre: {i} saniye", style="bold green")
            live.update(metin)
            time.sleep(1)
        else:
            live.update(Text("Geri sayım tamamlandı!", style="bold white"))
            
def progress_sayac(saniye: int = 3):
    with Progress() as progress:
        task = progress.add_task("[cyan]Geri sayım...", total=saniye)

        for _ in range(saniye):
            time.sleep(1)
            progress.update(task, advance=1)

    print("⏰ Süre doldu!")  
  



          

if __name__ == "__main__":
    geri_say(8)



