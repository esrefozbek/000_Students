
import AsistanFonksiyonlar.klavyeDinleme as klavDinle
import AsistanFonksiyonlar.arama as Arama
from rich.console import Console; console = Console()


def _SırfSorgu_():
    while True:
        arananData=klavDinle.klavyeDinlemesiÖncesiMesaj(1)
        if arananData is None:
            console.print("\n📤 Kullanıcı ESC'ye bastı. Giriş iptal edildi.",style="")
            break
        else:
        #     sorgu.sorgu(arananData)
            Arama.arama(arananData)
