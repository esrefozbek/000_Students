#from veri import TupleliListe_,SözlüklüListe_
import VERI.emptyLists as veriYolu
from rich.console import Console; c = Console()



#NOTE -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükListesineEkle(fark_TupleListesi:list):
    if veriYolu.FARK_SozlukListesi:  
        veriYolu.FARK_SozlukListesi.clear() #FIXME -burada listebaştan yaratılıyor.
        
    for item in fark_TupleListesi :
        veriYolu.FARK_SozlukListesi.append({
            "id": item[0],
            "ad": item[1],
            "soyad": item[2],
            "ogrenciNumarasi":item[3],
            "dogumTarihi": item[4],
            "sinifi": item[5],
            "kayitTarihi":item[6] })
        
    c.print("SözlükYap:: FARK_SozlukListesi >>", veriYolu.FARK_SozlukListesi)
   
   
    if veriYolu.FARK_SozlukListesi:  #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız.
        veriYolu.yedekSozlukluListe_.extend(veriYolu.FARK_SozlukListesi)
        veriYolu.SozlukluListe_Kopya.extend(veriYolu.FARK_SozlukListesi)
      
    return veriYolu.FARK_SozlukListesi 
                
           
                
    

 