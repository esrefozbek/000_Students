import readchar
from rich.console import Console;c = Console()
from rich.layout import Layout;l = Layout()
from rich import print
import sys



def KlavyeDinle():
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
            ➡️  Devam etmek için [bold green]ENTER[/] tuşuna bas..."""):
    c.print(mesaj, style="light_sky_blue3")
    while True:
        key = readchar.readkey()
        if key in ['\r', '\n']:
            break


def ENTER():
    Enter_ile_devam_et()



    
    return KlavyeDinle()
