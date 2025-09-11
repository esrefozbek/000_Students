#from veri import TupleliListe_,SözlüklüListe_
import VERI.veri as Veri
from rich.console import Console; console = Console()


#ANCHOR -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükYap(liste:list=Veri.TupleliListe_):
    console.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] başlıyor......  ")
    console.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] SözlüklüListe_ nin durumu:",Veri.SozlukluListe_)
        
    if Veri.SozlukluListe_:  
        Veri.SozlukluListe_.clear()                                              
    
    for TupleClassNesnesi in liste:
        Veri.SozlukluListe_.append({
            "id": TupleClassNesnesi[0],
            "ad": TupleClassNesnesi[1],
            "soyad": TupleClassNesnesi[2],
            "öğrenciNumarası":TupleClassNesnesi[3],
            "dogum_yili": TupleClassNesnesi[4],
            "sinif": TupleClassNesnesi[5],
            "kayıtTarihi":TupleClassNesnesi[6]
        })
    console.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] Dolum sonrası SözlüklüListe_:↩️",Veri.SozlukluListe_[-2:])
    
    #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız. 
    if Veri.SozlukluListe_:
        Veri.yedekSozlukluListe_=Veri.SozlukluListe_.copy()
        
         
        
        console.print ("\n[bold magenta]Tupleyi Sözlükleştirme:[/bold magenta] ♻️ ♻️ Tuplenin sözlüğe dönüştürülüp SözlüklüListe_ ye kayıt işlemi tamamlandı Allah'ın izniyle  ,\n",style="")
        console.print (f"""[bold magenta]Tupleyi Sözlükleştirme:[/bold magenta]
\n[bold black]
☢️  İstatistiklerim: ☢️ [/bold black]
[yellow]Sözlük listenin tipi:[/yellow]{type(Veri.SozlukluListe_)}
[yellow]Herbir elemanın tipi[0]:[/yellow]{type(Veri.SozlukluListe_[0])}
[yellow]Sözlüğün uzunluğu:[/yellow]{len(Veri.SozlukluListe_)}
[white]SözlüklüListeden bir örnek alınmış hali:[/white]\n""",style="yellow")
        console.print (f"""SözlüklüListe_nin ilk elemanı[0] ve son eleman[[-1]:\n""", Veri.SozlukluListe_[0],"...",Veri.SozlukluListe_[-1], style="yellow")
        
        if Veri.TupleliListe_:
                Veri.TupleliListe_.clear()

    return Veri.SozlukluListe_ 
                
           
                
    

 