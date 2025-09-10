import readchar
from rich.console import Console;c = Console()
from rich.panel import Panel
from rich import box
from rich.table import Table
from rich.live import Live
import time
from rich.layout import Layout
from rich import print
layout = Layout()

aramaSayısı=0
def klavyeDinlemesiÖncesiMesaj(sayı:int):
    global aramaSayısı
    if sayı==1:
        aramaSayısı+=1
        if not aramaSayısı>1:
            c.print(Panel(f"📌[white] Aradığın talebenin numarasını, adını ya da soyadını gir,[/][italic tan] Menüye dönmek için [bold orange_red1]Esc[/] tuşuna bas.", style="deep_sky_blue1"),end="")
        print("[bold red3] Esc[/][grey50] or[/][bold sea_green2] new[/] [yellow1]>>[/] ", end="", flush=True)
        
    if sayı==2:
        c.print("\n📌 Öğrenci numarası, adı ya da soyadı gir:", style="bold magenta")
        c.print("Ana menüye dönmek için [ESC] tuşuna bas.", style="bold yellow")
        print(">> ", end="", flush=True)
    if sayı==3:
       c.print("\n[color(15)]💰💰 Yeni öğrencinin ADINI giriniz:[color(240)](Bu aşamada [bold magenta]'Esc'[/bold magenta] ile kayıttan çıkabilirsin)[/color(240)]:[/ color(15)]  ",end="")
       #print("", end="", flush=True)      
    return klavyeGirisi()


def klavyeGirisi():
        pressedKeys = ""
        while True:
            pressedKey = readchar.readkey()
            if pressedKey == readchar.key.ESC:
                c.print("\n\nESC'ye basıldı, Ana Menüye dönülüyor  (1.5 second) ...", style="blink")
                time.sleep(1.5)
                return None 
                
            elif pressedKey == '\r':  # ENTER
                break
            else:
                pressedKeys += pressedKey
                print(pressedKey, end="", flush=True)
            
        return pressedKeys.strip()


def enter_OR_esc(metod):
    while True:
        key=readchar.readkey()
        if key=='\r':
            metod()
        elif key == readchar.key.ESC:
                print("\n\nESC'ye basıldı,")
                return None
              

def Enter_ile_devam_et(mesaj="""
➡️  Devam etmek için [bold green]ENTER[/bold green] tuşuna bas..."""):
    c.print(mesaj, style="blink")
    while True:
        key = readchar.readkey()
        if key in ['\r', '\n']:
            break


def ENTER():
    Enter_ile_devam_et()
