import readchar
from rich.console import Console;c = Console()
from rich.panel import Panel
from rich.layout import Layout;l = Layout()
from rich import print
from rich import print
import sys
import VERI.emptyLists as veriYolu 
aramaSayısı=0


def klavyeDinleme():
    global aramaSayısı
    pressedKeys = ""
    #print("Yazmaya başlayın (ESC ile iptal, ENTER ile tamamla):")

    while True:

        key = readchar.readkey()

        if key == readchar.key.ESC:
            aramaSayısı=0   
            return None
        elif key == readchar.key.ENTER:
            break
        elif key == readchar.key.SPACE:
            pressedKeys += ' '
            sys.stdout.write(' ')
            sys.stdout.flush()
        elif key == readchar.key.BACKSPACE:
            if len(pressedKeys) > 0:
                pressedKeys = pressedKeys[:-1]
                # Ekrandan da sil 
                sys.stdout.write('\b \b')
                sys.stdout.flush()
        elif len(key) == 1 and key.isprintable():
            pressedKeys += key
            sys.stdout.write(key)
            sys.stdout.flush()
        else:
            pass  # shift, ctrl gibi kontrol karakterleri

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



def Mesajlar(sayı:int=0):
    global aramaSayısı
        
    if sayı==0: pass
    if sayı==1:
        if aramaSayısı<1:
            c.print(Panel.fit(f"""📌
[cornsilk1 on navy_blue] Aradığın talebelerin numarasını, adını ya da soyadını gir  [/]
[italic tan on grey23]  {" "*24}Menüye dönmek için [bold orange_red1]Esc[/] tuşuna bas.[/]""", style="deep_sky_blue1"),end="")
            
        else: print("[bold red3] Esc[/][grey30] or[/][bold sea_green2] new[/] [yellow1]>>[/] ", end="", flush=True)
        
    if sayı==2:
        c.print(Panel.fit(f"📌 << [bright_white on red] Silinecek talebelerin numarasını, adını ya da soyadını gir [/] >>,[italic tan] Menüye dönmek için [bold orange_red1]Esc[/] tuşuna bas.[/]", style="red"),end="")
        print("[bold red3] Esc[/][grey30] or[/][bold sea_green2] new[/] [yellow1]>>[/] ", end="", flush=True)
        
    if sayı==3:
       c.print("\n[yellow]Öğrencinin;[/]\n[green]\tADI[/][grey30] || [red1]Esc[/][/grey30]",end=" >> ")
       
    if sayı==4:
        metin1=f"""[yellow]Silinecek öğrencilerin numaralarını girin. Sayıları boşluk veya virgül ile ayırabilirsiniz.[/]        
    [bold magenta]Geçerli aralık:[/] 0 - {len(veriYolu.Bulunanlar) - 1} 
    """  
    if sayı==5:
        metin2=f""" [bold white][italic yellow] Lütfen bu sefer dikkatli ol, Tanrı aşkına![/italic yellow] 🙏  Geçerli aralık:[bold yellow] 0 - {len(veriYolu.Bulunanlar) - 1} [/] [/] """
       
       
       
       
       #print("", end="", flush=True)      
    aramaSayısı+=1
    
    return klavyeDinleme()
