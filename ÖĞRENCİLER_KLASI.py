
import otomatikID
from rich.console import Console
console=Console()
from datetime import datetime


class Ogrenciler():
    # ogrenciId:int
    # ad:str
    # soyad:str
    # doğumTarihi:str
    # sinifi:str
    # kayıtTarihi:datetime 
    

    #? BURADA TUPLELER İÇEREN LİSTE YAPISINA EKLEME YAPILIYOR
    
    def __init__(self,  ad, soyad,öğrenciNumarası, dogTarihi,sinifi):
        self.ogrenciId= otomatikID.otomatikID()+1
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
