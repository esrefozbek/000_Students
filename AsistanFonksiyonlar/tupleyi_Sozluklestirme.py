#from veri import TupleliListe_,SözlüklüListe_
import VERI.veri as Veri
from rich.console import Console; c = Console()


#ANCHOR -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükYap(yeniEklenenlerListesi_:list=Veri.yeniEklenenlerListesi_Tuple):
    c.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] SözlüklüListe_ nin durumu:",Veri.SozlukluListe_)
        
    if Veri.SozlukluListe_:  
        Veri.SozlukluListe_.clear()           #FIXME - burada listebaştan yaratılıyor                                    
    
    for TupleClassNesnesi in yeniEklenenlerListesi_ :
        Veri.SozlukluListe_.append({
            "id": TupleClassNesnesi[0],
            "ad": TupleClassNesnesi[1],
            "soyad": TupleClassNesnesi[2],
            "öğrenciNumarası":TupleClassNesnesi[3],
            "dogum_yili": TupleClassNesnesi[4],
            "sinif": TupleClassNesnesi[5],
            "kayıtTarihi":TupleClassNesnesi[6]
        })
    c.print("[bold yellow]TupleyiSözlükYap_():[/] Dolum sonrası SözlüklüListe_:↩️",Veri.SozlukluListe_[0:])
    
    #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız. 
    if Veri.SozlukluListe_:
        Veri.yedekSozlukluListe_=Veri.SozlukluListe_.copy()
        Veri.SozlukluListe_Kopya=Veri.SozlukluListe_.copy()
        
         
        
        c.print ("\n[bold magenta]Tupleyi Sözlükleştirme:[/] ♻️ ♻️ Tuplenin sözlüğe dönüştürülüp SözlüklüListe_ ye kayıt işlemi tamamlandı,\n",style="")
        
        c.print (f"""[bold magenta]Tupleyi Sözlükleştirme:[/]
\n[bold black]
☢️  İstatistiklerim: ☢️ [/]
[yellow]Sözlük listenin tipi:[/]{type(Veri.SozlukluListe_)}
[yellow]Herbir elemanın tipi[0]:[/]{type(Veri.SozlukluListe_[0])}
[yellow]Sözlüğün uzunluğu:[/]{len(Veri.SozlukluListe_)}
[white]SözlüklüListe hali:[/]\n""",style="yellow")
        c.print (f"""istatistikteki SözlüklüListe_ :\n""", Veri.SozlukluListe_, style="yellow")
        
        """  if Veri.TupleliListe_:
                Veri.TupleliListe_.clear() """

    return Veri.SozlukluListe_ 
                
           
                
    

 