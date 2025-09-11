import VERI.veri as Veri
import AnaFonksiyonlar.JSON as Json
from rich.console import Console; console = Console()

sayı: int = 0

def otomatikID():
    global sayı
    if not Veri.TupleliListe_:
        Json.JSONdanYükleme_()

    if Veri.TupleliListe_:
        en_büyük_tuple = max(Veri.TupleliListe_, key=lambda x: x[0])
        sayı = en_büyük_tuple[0]  # Sadece ID'yi al
        console.print("[bold magenta]otomatikID():[/bold magenta]🍀🍺🍺🍀  En büyük ID:",sayı )
    else:
        sayı = 0
        console.print("📂 Liste boş, ID 0'dan başlatıldı.", style="red")

    return sayı


if __name__ == "__main__":
    otomatikID()
