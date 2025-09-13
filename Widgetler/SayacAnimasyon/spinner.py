from rich.console import Console
from rich.spinner import Spinner
import time

console = Console()


def spinner1(sayi):

    with console.status("[bold green]Yükleniyor...", spinner="dots"):
        time.sleep(sayi)  # burada uzun süren işlemin olur


def spinner2(sayi):

    with console.status("[bold green]Düzeltiliyor...", spinner="dots"):
        time.sleep(sayi)  # burada uzun süren işlemin olur
        
        
def spinner3(sayi):

    with console.status("[bold green]KAyıt yapılıyor...", spinner="dots"):
        time.sleep(sayi)  # burada uzun süren işlemin olur