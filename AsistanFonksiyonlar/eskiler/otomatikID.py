import VERI.emptyLists as VERIModul
import AnaFonksiyonlar.JSON_jobs as AnaModul
from rich.console import Console; c = Console()

sayı: int = 0

def otomatikID():
    global sayı
    if not VERIModul.SilinenlerinTupleliListesi_:
        AnaModul.JSONdanYükleme_()

    if VERIModul.SilinenlerinTupleliListesi_:
        en_büyük_tuple = max(VERIModul.SilinenlerinTupleliListesi_, key=lambda x: x[0])
        sayı = en_büyük_tuple[0]  # Sadece ID'yi al
        c.print("\t[green3]ID[/green3] >>",sayı,end=", " )
    else:
        sayı = 0
        c.print("📂 Liste boş, ID 0'dan başlatıldı.", style="red")

    return sayı


if __name__ == "__main__":
    otomatikID()
