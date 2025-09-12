#from veri import TupleliListe_,SözlüklüListe_
import VERI.veri as Veri_Yolu
from rich.console import Console; c = Console()


#ANCHOR -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükYap(yeniEklenenlerListesi_:list=Veri_Yolu.yeniEklenenlerListesi_Tuple):
    
    c.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] SözlüklüListe_ nin durumu:",end="")
    c.print(Veri_Yolu.SozlukluListe_)
        
    if Veri_Yolu.SozlukluListe_:  
        Veri_Yolu.SozlukluListe_.clear()           #FIXME - burada listebaştan yaratılıyor                                    
    
    for TupleClassNesnesi in yeniEklenenlerListesi_ :
        Veri_Yolu.SozlukluListe_.append({
            "id": TupleClassNesnesi[0],
            "ad": TupleClassNesnesi[1],
            "soyad": TupleClassNesnesi[2],
            "öğrenciNumarası":TupleClassNesnesi[3],
            "dogum_yili": TupleClassNesnesi[4],
            "sinif": TupleClassNesnesi[5],
            "kayıtTarihi":TupleClassNesnesi[6]
        })
    c.print("[bold yellow]TupleyiSözlükYap_():[/] Dolum sonrası SözlüklüListe_:",end="")
    if Veri_Yolu.SozlukluListe_:
        c.print("[...]" )
    
    #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız. 
    if Veri_Yolu.SozlukluListe_:
        Veri_Yolu.yedekSozlukluListe_=Veri_Yolu.SozlukluListe_.copy()
        Veri_Yolu.SozlukluListe_Kopya=Veri_Yolu.SozlukluListe_.copy()
        
         
        
       #^ c.print ("\n[bold magenta]Tupleyi Sözlükleştirme:[/] ♻️ ♻️  Tuplenin sözlüğe dönüştürülüp SözlüklüListe_ ye kayıt işlemi tamamlandı.\n",style="")
        
        c.print (f"""[bold magenta]Tupleyi Sözlükleştirme:[/]\n[bold black] ☢️  İstatistiklerim: ☢️ [/]
        \t\t[yellow]Sözlük listenin tipi:[/]{type(Veri_Yolu.SozlukluListe_)}
        \t\t[yellow]Herbir elemanın tipi[0]:[/]{type(Veri_Yolu.SozlukluListe_[0])}
        \t\t[yellow]Sözlüğün uzunluğu:[/]{len(Veri_Yolu.SozlukluListe_)}""",style="yellow")
         
        c.print ("\t\tistatistikteki SözlüklüListe >>\n", Veri_Yolu.SozlukluListe_[-1])
        
        """  if Veri.TupleliListe_:
                Veri.TupleliListe_.clear() """

    return Veri_Yolu.SozlukluListe_ 
                
           
                
    

 