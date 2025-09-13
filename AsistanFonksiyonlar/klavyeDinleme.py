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
import keyboard
from rich import print

aramaSayısı=0
def klavyeDinlemesiÖncesiMesaj(sayı:int):
    global aramaSayısı
    if sayı==1:
        aramaSayısı+=1
        if not aramaSayısı>1:
            c.print(Panel(f"📌[white] Aradığın talebenin numarasını, adını ya da soyadını gir,[/][italic tan] Menüye dönmek için [bold orange_red1]Esc[/] tuşuna bas.", style="deep_sky_blue1"),end="")
        print("[bold red3] Esc[/][grey30] or[/][bold sea_green2] new[/] [yellow1]>>[/] ", end="", flush=True)
        
    if sayı==2:
        c.print("\n📌 Öğrenci numarası, adı ya da soyadı gir:", style="bold magenta")
        c.print("Ana menüye dönmek için [ESC] tuşuna bas.", style="bold yellow")
        print(">> ", end="", flush=True)
    if sayı==3:
       c.print("\n[yellow]Öğrencinin;[/]\n[green]\tADI[/][grey30] || [red1]Esc[/][/grey30]",end=" >> ")
       #print("", end="", flush=True)      
    return klavyeGirisi()


def klavyeGirisi():
    pressedKeys = ""

  # print("[bold green]Yazmaya başlayın (ESC ile iptal, ENTER ile tamamla):[/bold green]")

    while True:
        key = keyboard.read_event()

        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'esc':
                print("\n[yellow]ESC'ye basıldı, Ana Menüye dönülüyor...[/yellow]")
                return None
            elif key.name == 'enter':
                break
            elif key.name == 'space':
                pressedKeys += ' '
                print(' ', end="", flush=True)
            elif len(key.name) == 1:
                pressedKeys += key.name
                print(key.name, end="", flush=True)
            else:
                # özel tuşları (örn. shift, ctrl) yoksay
                pass

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
