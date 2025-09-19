#from veri import TupleliListe_,SözlüklüListe_
import VERI.emptyLists as EmptyLists
from rich.console import Console; c = Console()



#NOTE -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükListesineEkle(fark_TupleListesi:list):
    if EmptyLists.FARK_SozlukListesi:  
        EmptyLists.FARK_SozlukListesi.clear() #FIXME -burada listebaştan yaratılıyor.
        
    for item in fark_TupleListesi :
        EmptyLists.FARK_SozlukListesi.append({
            "id": item[0],
            "ad": item[1],
            "soyad": item[2],
            "ogrenciNumarasi":item[3],
            "dogumTarihi": item[4],
            "sinifi": item[5],
            "kayitTarihi":item[6] })
        
    c.print("SözlükYap:: FARK_SozlukListesi >>", EmptyLists.FARK_SozlukListesi)
   
   
    if EmptyLists.FARK_SozlukListesi:  #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız.
        EmptyLists.yedekSozlukluListe_.extend(EmptyLists.FARK_SozlukListesi)
        EmptyLists.SozlukluListe_Kopya.extend(EmptyLists.FARK_SozlukListesi)
      
    return EmptyLists.FARK_SozlukListesi 
                
           
                
    

 