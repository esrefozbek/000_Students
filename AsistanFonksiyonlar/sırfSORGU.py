
import AsistanFonksiyonlar.klavyeDinleme as klavyeyiDinle
import AsistanFonksiyonlar.arama as Arama
from rich.console import Console; console = Console()


def _SırfSorgu_():
    while True:
        arananData=klavyeyiDinle.Mesajlar(1)
        if arananData is None:
            console.print("\n📤 Kullanıcı ESC'ye bastı. Giriş iptal edildi.",style="")
            break
        else:
        #     sorgu.sorgu(arananData)
            Arama.tumKriterleriBul(arananData)
