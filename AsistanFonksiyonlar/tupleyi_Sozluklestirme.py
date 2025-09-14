#from veri import TupleliListe_,SözlüklüListe_
import VERI.emptyLists as VERIModul
from rich.console import Console; c = Console()


#NOTE -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükYap(YeniEklenenlerinTupleListesi_):
        
    if VERIModul.YeniEklenenlerinSozluklerListesi_:  
        VERIModul.YeniEklenenlerinSozluklerListesi_.clear() #FIXME -burada listebaştan yaratılıyor.
        c.print("TupleyiSözlükYap>>yeniEklenenlerListesi_>>", YeniEklenenlerinTupleListesi_)
    for TupleClassNesnesi in YeniEklenenlerinTupleListesi_ :
        VERIModul.YeniEklenenlerinSozluklerListesi_.append({
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
    
   
    if VERIModul.YeniEklenenlerinSozluklerListesi_:  #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız.
        VERIModul.yedekSozlukluListe_.extend(VERIModul.YeniEklenenlerinSozluklerListesi_)
        VERIModul.SozlukluListe_Kopya.extend(VERIModul.YeniEklenenlerinSozluklerListesi_)
        
        
        
       # c.print ("\n[bold magenta]Tupleyi Sözlükleştirme:[/] Tuplenin sözlüğe dönüştürülüp SözlüklüListe_ ye kaydı tamamlandı.\n",style="")
             
        # c.print (f"""\n[dark_orange3]Tupleyi Sözlükleştirdim[/]\n[turquoise2]☢️  İstatistiklerim: ☢️ [/]
        # \t[yellow1]Sözlük listenin tipi:[/]{type(Veri_Yolu.SozluklerListesi_)}
        # \t[yellow1]Herbir elemanın tipi[0]:[/]{type(Veri_Yolu.SozluklerListesi_[0])}
        # \t[yellow1]Sözlüğün uzunluğu:[/]{len(Veri_Yolu.SozluklerListesi_)},
        # [dark_slate_gray2]\nHazırlanan SözlüklüListe [/]>>\n\t""", Veri_Yolu.SozluklerListesi_,end="\n")        """
    
    return VERIModul.YeniEklenenlerinSozluklerListesi_ 
                
           
                
    

 