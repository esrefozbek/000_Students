
import keyboard


        
        
import keyboard
from rich import print

def klavyeGirisi_keyboard():
    pressedKeys = ""

    print("[bold green]Yazmaya başlayın (ESC ile iptal, ENTER ile tamamla):[/bold green]")

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

if __name__ == "__main__":
    girilen = klavyeGirisi_keyboard()
    print(f"\n[cyan]Girdi:[/] {girilen}")
