#FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.





import time
import AsistanFonksiyonlar.klavyeDinleme as klavDinle
#import arama
from rich.console import Console; console = Console()
import MenuTablo.tablolarPY as TablolarPY,VERI.veri as Veri_Yolu 
from rich.live import Live
import time
# import aramaParametresi
from rich.console import Console; c=Console()
import Widgetler.randomRenk as RandomRenk
menüTipi="Sorgu Menüsü"
listeTipi="Sorgu Listesi"
AramadaBulunanlarListesi_=[]





def aramaParametresi():
    aramaParametresi:object
    while True:
        aramaParametresi=klavDinle.klavyeDinlemesiÖncesiMesaj(1)

        if aramaParametresi is None:   #NOTE -  None cevabı  ancak Esc'ye basıldı ise gelir.
            console.print("\n📤 Kullanıcı ESC'ye bastı. Giriş iptal edildi.",style="")
            break
        else:
          #  arama.arama(aramaParametresi)
          return aramaParametresi




from rich.spinner import Spinner

#a=aramaParametresi.aramaParametresi()
def arama(aramaArgumani):
   # c.print(veri.TupleliListe_)
    AramadaBulunanlarListesi_.clear()  #TODO - Her sorguda önce temizle 
            
    
    for ogrenci in Veri_Yolu.TupleliListe_:
                if   (aramaArgumani is not None):
                #console.print(" [white on red]Bu numaraya sahip bir öğrenci yok. Düzgün bir sayı gir[/white on red]", style=""  )
                        if aramaArgumani==str(ogrenci[0]) or aramaArgumani in ogrenci[1].lower() or aramaArgumani in ogrenci[2].lower():
                                    AramadaBulunanlarListesi_.append(ogrenci)
                   
                else:
                    continue
    text=f"Aranıyor... "
    with Live(Spinner("dots", text=text),    refresh_per_second=10):
                                        time.sleep(0.8)
                                 



    if not len(AramadaBulunanlarListesi_)==0:
        TablolarPY.TABLO_6lı(AramadaBulunanlarListesi_,menüTipi, listeTipi)
        
    if not AramadaBulunanlarListesi_:
                    RandomRenk.ogrenciYok()
                    
             #     c.print(f"[{randomRenk.randomize(randomRenk.Renkler())}]  Bu kayıtta bir öğrenci bulunamadı.[/]", style="")
               #   print("   öğrenci yok")
           





