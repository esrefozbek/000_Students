import klavyeDinleme
#import arama
from rich.console import Console; console = Console()
import tablolarPY,veri 
# import aramaParametresi
from rich.console import Console; c=Console()
import random,randomRenk
menüTipi="Sorgu Menüsü"
listeTipi="Sorgu Listesi"
AramadaBulunanlarListesi_=[]





def aramaParametresi():
    aramaParametresi:object
    while True:
        aramaParametresi=klavyeDinleme.klavyeÖncesiMesaj(1)

        if aramaParametresi is None:   #NOTE -  None cevabı  ancak Esc'ye basıldı ise gelir.
            console.print("\n📤 Kullanıcı ESC'ye bastı. Giriş iptal edildi.",style="")
            break
        else:
          #  arama.arama(aramaParametresi)
          return aramaParametresi





#a=aramaParametresi.aramaParametresi()
def arama(aramaArgumani):
   # c.print(veri.TupleliListe_)
    AramadaBulunanlarListesi_.clear()  #TODO - Her sorguda önce temizle 
            
    
    for ogrenci in veri.TupleliListe_:
                if   (aramaArgumani.isdigit() or aramaArgumani.isalpha() ):
                #console.print(" [white on red]Bu numaraya sahip bir öğrenci yok. Düzgün bir sayı gir[/white on red]", style=""  )
                        if aramaArgumani==str(ogrenci[0]) or aramaArgumani in ogrenci[1].lower() or aramaArgumani in ogrenci[2].lower():
                                    AramadaBulunanlarListesi_.append(ogrenci)
                else:
                    continue
                
                                 




    if not len(AramadaBulunanlarListesi_)==0:
        tablolarPY.TABLO_6lı(AramadaBulunanlarListesi_,menüTipi, listeTipi)
        
    if not AramadaBulunanlarListesi_:
                    #randomRenk.ogrenciYok()
             #     c.print(f"[{randomRenk.randomize(randomRenk.Renkler())}]  Bu kayıtta bir öğrenci bulunamadı.[/]", style="")
                  print("   öğrenci yok")
           





