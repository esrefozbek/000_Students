#from veri import TupleliListe_,SözlüklüListe_
import VERI.emptyLists as Veri_Yolu
from rich.console import Console; c = Console()


#NOTE -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükYap(yeniEklenenlerListesi_):
    
    c.print("[bold yellow]TupleyiSözlükYap_():[/] SözlüklüListe_ nin durumu:",end="")
    c.print(Veri_Yolu.SozluklerListesi_)
        
    if Veri_Yolu.SozluklerListesi_:  
        Veri_Yolu.SozluklerListesi_.clear() #FIXME -burada listebaştan yaratılıyor.
    
    for TupleClassNesnesi in yeniEklenenlerListesi_ :
        Veri_Yolu.SozluklerListesi_.append({
            "id": TupleClassNesnesi[0],
            "ad": TupleClassNesnesi[1],
            "soyad": TupleClassNesnesi[2],
            "öğrenciNumarası":TupleClassNesnesi[3],
            "dogum_yili": TupleClassNesnesi[4],
            "sinif": TupleClassNesnesi[5],
            "kayıtTarihi":TupleClassNesnesi[6] })
        
    c.print("[bold yellow]TupleyiSözlükYap_():[/] Dolum sonrası SözlüklüListe_:",end="")
    if Veri_Yolu.SozluklerListesi_:
        c.print("[...]" )
    
   
    if Veri_Yolu.SozluklerListesi_:  #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız.
        Veri_Yolu.yedekSozlukluListe_=Veri_Yolu.SozluklerListesi_.copy()
        Veri_Yolu.SozlukluListe_Kopya=Veri_Yolu.SozluklerListesi_.copy()
        
        c.print ("\n[bold magenta]Tupleyi Sözlükleştirme:[/] Tuplenin sözlüğe dönüştürülüp SözlüklüListe_ ye kaydı tamamlandı.\n",style="")
        
        c.print (f"""[bold magenta]Tupleyi Sözlükleştirme:[/]\n[bold black] ☢️  İstatistiklerim: ☢️ [/]
        \t\t[yellow]Sözlük listenin tipi:[/]{type(Veri_Yolu.SozluklerListesi_)}
        \t\t[yellow]Herbir elemanın tipi[0]:[/]{type(Veri_Yolu.SozluklerListesi_[0])}
        \t\t[yellow]Sözlüğün uzunluğu:[/]{len(Veri_Yolu.SozluklerListesi_)}""",style="yellow")
         
        c.print ("\t\tistatistikteki SözlüklüListe >>\n", Veri_Yolu.SozluklerListesi_)
    
    return Veri_Yolu.SozluklerListesi_ 
                
           
                
    

 