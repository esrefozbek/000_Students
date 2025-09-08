from menu import menu_goster, ekranTemizle
import klavyeDinleme
import SORGU
from rich.console import Console; console = Console()

def _SırfSorgu_():
    while True:
        arananData=klavyeDinleme.klavyeÖncesiMesaj(1)
        if arananData is None:
            console.print("\n📤 Kullanıcı ESC'ye bastı. Giriş iptal edildi.",style="")
            break
        else:
        #     sorgu.sorgu(arananData)
            SORGU._Sorgu_(arananData)
