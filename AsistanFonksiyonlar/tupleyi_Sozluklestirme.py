#from veri import TupleliListe_,SözlüklüListe_
import VERI.emptyLists as E_LISTS
from rich.console import Console; c = Console()



#NOTE -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükListesineEkle(fark_TupleListesi:list):
    if E_LISTS.FARK_SozlukListesi:  
        E_LISTS.FARK_SozlukListesi.clear() #FIXME -burada listebaştan yaratılıyor.
        
    for item in fark_TupleListesi :
        E_LISTS.FARK_SozlukListesi.append({
            "id": item[0],
            "ad": item[1],
            "soyad": item[2],
            "ogrenciNumarasi":item[3],
            "dogumTarihi": item[4],
            "sinifi": item[5],
            "kayitTarihi":item[6] })
        
    c.print("SözlükYap:: FARK_SozlukListesi >>", E_LISTS.FARK_SozlukListesi)
   
   
    if E_LISTS.FARK_SozlukListesi:  #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız.
        E_LISTS.yedekSozlukluListe_.extend(E_LISTS.FARK_SozlukListesi)
        E_LISTS.SozlukluListe_Kopya.extend(E_LISTS.FARK_SozlukListesi)
      
    return E_LISTS.FARK_SozlukListesi 
                
           
                
    

 