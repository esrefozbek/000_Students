import AsistanFonksiyonlar.klavyeDinleme as klavyeyiDinle
from rich.console import Console; c = Console()

def AramaParametresiOlustur(mesaj:int=0):
    while True:
        aramaParametresi=klavyeyiDinle.klavyeÖncesiMesaj(mesaj)

        if aramaParametresi is None:   #NOTE -  None cevabı  ancak Esc'ye basıldı ise gelir.
            c.print("\n📤 Kullanıcı ESC'ye bastı. Giriş iptal edildi.",style="")
            break
        else:
          #  arama.arama(aramaParametresi)
          return aramaParametresi
