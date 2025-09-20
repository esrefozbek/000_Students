#breakpoint()
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
    
    def __init__(self,  ad, soyad, ogrenciNumarasi, dogumTarihi, sinifi):
        
        self.Id=TxtYolu.ID_olustur_ve_oku()
        self.ad=ad
        self.soyad=soyad
        self.ogrenciNumarasi=ogrenciNumarasi
        self.dogumTarihi=dogumTarihi
        self.sinifi=sinifi
        self.kayitTarihi = datetime.now().strftime("%d/%m/%Y")

      #  console.print ("\n Ogrenciler klasının bir nesnesi oluşturuldu.\n", style="")
        
    
    # def toTuple(self):  #inputla alınan veriler  tuple olarak return edildi. 
    #     return (self.ogrenciId, self.ad, self.soyad, self.ogrenciNumarasi, self.dogumTarihi,self.sinifi, self.kayitTarihi)

    
    def toDict(self):
        return {"Id":self.Id, "ad":self.ad, "soyad":self.soyad, "ogrenciNumarasi":self.ogrenciNumarasi, "dogumTarihi":self.dogumTarihi, "sinifi":self.sinifi, "kayitTarihi":self.kayitTarihi  }
    
        


# --- Araba sınıfı burada bitti ---
# Ogrenciler'den bir nesne oluşturmak için class dışında olmalısın.
