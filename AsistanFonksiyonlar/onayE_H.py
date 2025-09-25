import readchar
from rich.console import Console; c=Console()
from rich import print as p
from rich.panel import Panel


def Evet_Hayır_OnayiAl(ogr):
    p(Panel.fit(f"\n[?] Bu öğrenciyi silmek istiyor musunuz?  [cyan]{ogr}[/] \nDevam etmek için 'e/E'(evet), iptal için 'h/H'(hayır/Esc) tuşuna bas" , title=" Evet Hayır ONAYI ",     style="red1"))
            
            
    while True:
        tus = readchar.readchar().lower()
        if tus == 'e' or tus=='E':
            print(" → Onaylandı.")
            return True
        elif tus == 'h' or 'H':
            print(" → İptal edildi.")
            return False
                
        else:
            print("\nGeçersiz tuş! Lütfen 'e/E' veya 'h/H' tuşlarına basın: ", end="", flush=True)
