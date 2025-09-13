#from veri import TupleliListe_,SözlüklüListe_
import VERI.emptyLists as Veri_Yolu
from rich.console import Console; c = Console()


#NOTE -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükYap(YeniEklenenlerinTupleListesi_):
        
    if Veri_Yolu.SozluklerListesi_:  
        Veri_Yolu.SozluklerListesi_.clear() #FIXME -burada listebaştan yaratılıyor.
        c.print("TupleyiSözlükYap>>yeniEklenenlerListesi_>>", YeniEklenenlerinTupleListesi_)
    for TupleClassNesnesi in YeniEklenenlerinTupleListesi_ :
        Veri_Yolu.SozluklerListesi_.append({
            "id": TupleClassNesnesi[0],
            "ad": TupleClassNesnesi[1],
            "soyad": TupleClassNesnesi[2],
            "öğrenciNumarası":TupleClassNesnesi[3],
            "dogum_yili": TupleClassNesnesi[4],
            "sinif": TupleClassNesnesi[5],
            "kayıtTarihi":TupleClassNesnesi[6] })
        
  #  c.print("[bold yellow]TupleyiSözlükYap_():[/] Dolum sonrası SözlüklüListe_:",end="")
#    if Veri_Yolu.SozluklerListesi_:
      #  c.print("[...]" )
    
   
    if Veri_Yolu.SozluklerListesi_:  #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız.
        Veri_Yolu.yedekSozlukluListe_.extend(Veri_Yolu.SozluklerListesi_)
        Veri_Yolu.SozlukluListe_Kopya.extend(Veri_Yolu.SozluklerListesi_)
        
        
        
       # c.print ("\n[bold magenta]Tupleyi Sözlükleştirme:[/] Tuplenin sözlüğe dönüştürülüp SözlüklüListe_ ye kaydı tamamlandı.\n",style="")
             
        # c.print (f"""\n[dark_orange3]Tupleyi Sözlükleştirdim[/]\n[turquoise2]☢️  İstatistiklerim: ☢️ [/]
        # \t[yellow1]Sözlük listenin tipi:[/]{type(Veri_Yolu.SozluklerListesi_)}
        # \t[yellow1]Herbir elemanın tipi[0]:[/]{type(Veri_Yolu.SozluklerListesi_[0])}
        # \t[yellow1]Sözlüğün uzunluğu:[/]{len(Veri_Yolu.SozluklerListesi_)},
        # [dark_slate_gray2]\nHazırlanan SözlüklüListe [/]>>\n\t""", Veri_Yolu.SozluklerListesi_,end="\n")        """
    
    return Veri_Yolu.SozluklerListesi_ 
                
           
                
    

 