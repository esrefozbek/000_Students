#from veri import TupleliListe_,SözlüklüListe_
import VERI.emptyLists as EMPTY
from rich.console import Console; c = Console()



#NOTE -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükListesineEkle(fark_TupleListesi:list):
    if EMPTY.FARK_SozlukListesi:  
        EMPTY.FARK_SozlukListesi.clear() #FIXME -burada listebaştan yaratılıyor.
        
    for item in fark_TupleListesi :
        EMPTY.FARK_SozlukListesi.append({
            "id": item[0],
            "ad": item[1],
            "soyad": item[2],
            "ogrenciNumarasi":item[3],
            "dogumTarihi": item[4],
            "sinifi": item[5],
            "kayitTarihi":item[6] })
        
    c.print("SözlükYap:: FARK_SozlukListesi >>", EMPTY.FARK_SozlukListesi)
   
   
    if EMPTY.FARK_SozlukListesi:  #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız.
        EMPTY.yedekSozlukluListe_.extend(EMPTY.FARK_SozlukListesi)
        EMPTY.SozlukluListe_Kopya.extend(EMPTY.FARK_SozlukListesi)
      
    return EMPTY.FARK_SozlukListesi 
                
           
                
    

 