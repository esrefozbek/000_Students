from AsistanFonksiyonlar.eskiler import otomatikID as otmID
from rich.console import Console; c=Console()
from datetime import datetime
import AsistanFonksiyonlar.txt_Jobs as TxtYolu
import os


class Ogrenciler():
    # ogrenciId:int
    # ad:str
    # soyad:str
    # doğumTarihi:str
    # sinifi:str
    # kayıtTarihi:datetime 
    

    #NOTE -  BURADA TUPLELER İÇEREN LİSTE YAPISINA EKLEME YAPILIYOR
    
    def __init__(self,  ad, soyad,öğrenciNumarası, dogTarihi,sinifi):
        if not os.path.exists("VERI/Text.txt"):
            print("sınıfta if not exists  |||>> ",)
            TxtYolu.txtYoksaOlustur("VERI/Text.txt")
        c.print("sınıfta Text'ten okunan değer >>",(TxtYolu.txtID_Oku("VERI/Text.txt")))
        self.ogrenciId=int(TxtYolu.txtID_Oku("VERI/Text.txt")) + 1
        c.print("sınıfta +1 yapıldı ve basıldı  >> ",self.ogrenciId,style="")
        TxtYolu.txteYeniID_Gir(str(self.ogrenciId))
        input("sınıf yatışı 1")
        self.ad=ad
        self.soyad=soyad
        self.öğrenciNumarası=öğrenciNumarası
        self.doğumTarihi=dogTarihi
        self.sinifi=sinifi
        self.kayıtTarihi = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

      #  console.print ("\n Ogrenciler klasının bir nesnesi oluşturuldu.\n", style="")
        
    
    def toTuple(self):  #inputla alınan veriler  tuple olarak return edildi. 
        return (self.ogrenciId, self.ad, self.soyad, self.öğrenciNumarası, self.doğumTarihi,self.sinifi, self.kayıtTarihi)

        


# --- Araba sınıfı burada bitti ---
# Ogrenciler'den bir nesne oluşturmak için class dışında olmalısın.
