#from veri import TupleliListe_,SözlüklüListe_
import VERI.emptyLists as EMPTY_LISTS
from rich.console import Console; c = Console()



#NOTE -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükListesineEkle(fark_TupleListesi:list):
    if EMPTY_LISTS.FARK_SozlukListesi:  
        EMPTY_LISTS.FARK_SozlukListesi.clear() #FIXME -burada listebaştan yaratılıyor.
        
    for item in fark_TupleListesi :
        EMPTY_LISTS.FARK_SozlukListesi.append({
            "id": item[0],
            "ad": item[1],
            "soyad": item[2],
            "ogrenciNumarasi":item[3],
            "dogumTarihi": item[4],
            "sinifi": item[5],
            "kayitTarihi":item[6] })
        
    c.print("SözlükYap:: FARK_SozlukListesi >>", EMPTY_LISTS.FARK_SozlukListesi)
   
   
    if EMPTY_LISTS.FARK_SozlukListesi:  #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız.
        EMPTY_LISTS.yedekSozlukluListe_.extend(EMPTY_LISTS.FARK_SozlukListesi)
        EMPTY_LISTS.SozlukluListe_Kopya.extend(EMPTY_LISTS.FARK_SozlukListesi)
      
    return EMPTY_LISTS.FARK_SozlukListesi 
                
           
                
    

 