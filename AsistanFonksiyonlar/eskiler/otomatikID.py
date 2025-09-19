import VERI.emptyLists as EmptyLists
import AnaFonksiyonlar.JSON_jobs as AnaModul
from rich.console import Console; c = Console()

sayı: int = 0

def otomatikID():
    global sayı
    if not EmptyLists.Jsonda_Mevcut_Veriler:
        AnaModul.JSONdanImport()

    if EmptyLists.Jsonda_Mevcut_Veriler:
        en_büyük_tuple = max(EmptyLists.Jsonda_Mevcut_Veriler, key=lambda x: x[0])
        sayı = en_büyük_tuple[0]  # Sadece ID'yi al
        c.print("\t[green3]ID[/green3] >>",sayı,end=", " )
    else:
        sayı = 0
        c.print("📂 Liste boş, ID 0'dan başlatıldı.", style="red")

    return sayı


if __name__ == "__main__":
    otomatikID()
