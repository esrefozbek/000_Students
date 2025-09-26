import readchar
from rich.console import Console; c=Console()
from rich import print as p
from rich.panel import Panel


def Evet_Hayır_OnayiAl(ogr):
    p(Panel.fit(f"\n 🔍[bold green]{ogr}[/] << [bold red1]Bu öğrenciyi silmek istiyor musunuz ❓ [/]  \nDevam etmek için 'e/E'(evet), iptal için 'h/H'(hayır/Esc) tuşuna bas" , title=" Evet Hayır ONAYI ",     style="grey70",border_style="grey23"))
            
            
    while True:
        tus = readchar.readchar().lower()
        if tus == 'e' or tus=='E':
            print(" → Silme Onaylandı. ✅ ")
            return True
        elif tus == 'h' or 'H':
            print(" → Silme İptal edildi. ❌ ")
            return False
                
        else:
            print("\nGeçersiz tuş! Lütfen 'e/E' veya 'h/H' tuşlarına basın: ", end="", flush=True)
