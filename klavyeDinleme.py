import readchar
from rich.console import Console
console = Console()
import time


def klavyeGirisi():
        girilenKlavyeTusu = ""
        while True:
            key = readchar.readkey()
            if key == readchar.key.ESC:
                console.print("\n\nESC'ye basıldı, Ana Menüye dönülüyor...", style="blink")
                time.sleep(2)
                return None
                
            elif key == '\r':  # ENTER
                break
            else:
                girilenKlavyeTusu += key
                print(key, end="", flush=True)
            
        return girilenKlavyeTusu.strip()


def enter_OR_esc(metod):
    while True:
        key=readchar.readkey()
        if key=='\r':
            metod()
        elif key == readchar.key.ESC:
                print("\n\nESC'ye basıldı,")
                return None






def klavyeÖncesiMesaj(sayı:int):
    if sayı==1:
        console.print("\n📌 Öğrenci numarası, adı ya da soyadı gir:", style="bold yellow")
        print("Ana menüye dönmek için [ESC] tuşuna bas.")
        print(">> ", end="", flush=True)
        
    elif sayı==2:
        console.print("\n📌 Öğrenci numarası, adı ya da soyadı gir:", style="bold magenta")
        console.print("Ana menüye dönmek için [ESC] tuşuna bas.", style="bold yellow")
        print(">> ", end="", flush=True)
    
    elif sayı==3:
    
       console.print("\n[color(15)]💰💰 Yeni öğrencinin ADINI giriniz:[color(240)](Bu aşamada [bold magenta]'Esc'[/bold magenta] ile kayıttan çıkabilirsin)[/color(240)]:[/ color(15)]  ",end="")
       #print("", end="", flush=True)      
    
    return klavyeGirisi()


 
                

def Enter_ile_devam_et(mesaj="""
➡️  Devam etmek için [bold green]ENTER[/bold green] tuşuna bas..."""):
    console.print(mesaj, style="blink")
    while True:
        key = readchar.readkey()
        if key in ['\r', '\n']:
            break


def ENTER():
    Enter_ile_devam_et()
