import readchar
from rich.console import Console
console=Console()


def Evet_Hayır_OnayiAl(ogr):
    console.print(f"\n[?] Bu öğrenciyi silmek istiyor musunuz?\n[bold cyan]{ogr}[/bold cyan]")
    print("Devam etmek için [e/E]vet, iptal için [h/H]ayır tuşuna basın: ", end="", flush=True)

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
