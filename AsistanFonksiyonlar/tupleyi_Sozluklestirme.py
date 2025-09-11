#from veri import TupleliListe_,SözlüklüListe_
import veri
from rich.console import Console; console = Console()


#ANCHOR -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükYap(liste:list=veri.TupleliListe_):
    console.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] başlıyor......  ")
    console.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] SözlüklüListe_ nin durumu:",veri.SozlukluListe_)
        
    if veri.SozlukluListe_:  
        veri.SozlukluListe_.clear()                                              
    
    for TupleClassNesnesi in liste:
        veri.SozlukluListe_.append({
            "id": TupleClassNesnesi[0],
            "ad": TupleClassNesnesi[1],
            "soyad": TupleClassNesnesi[2],
            "öğrenciNumarası":TupleClassNesnesi[3],
            "dogum_yili": TupleClassNesnesi[4],
            "sinif": TupleClassNesnesi[5],
            "kayıtTarihi":TupleClassNesnesi[6]
        })
    console.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] Dolum sonrası SözlüklüListe_:↩️",veri.SozlukluListe_[-2:])
    
    #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız. 
    if veri.SozlukluListe_:
        veri.yedekSozlukluListe_=veri.SozlukluListe_.copy()
        
         
        
        console.print ("\n[bold magenta]Tupleyi Sözlükleştirme:[/bold magenta] ♻️ ♻️ Tuplenin sözlüğe dönüştürülüp SözlüklüListe_ ye kayıt işlemi tamamlandı Allah'ın izniyle  ,\n",style="")
        console.print (f"""[bold magenta]Tupleyi Sözlükleştirme:[/bold magenta]
\n[bold black]
☢️  İstatistiklerim: ☢️ [/bold black]
[yellow]Sözlük listenin tipi:[/yellow]{type(veri.SozlukluListe_)}
[yellow]Herbir elemanın tipi[0]:[/yellow]{type(veri.SozlukluListe_[0])}
[yellow]Sözlüğün uzunluğu:[/yellow]{len(veri.SozlukluListe_)}
[white]SözlüklüListeden bir örnek alınmış hali:[/white]\n""",style="yellow")
        console.print (f"""SözlüklüListe_nin ilk elemanı[0] ve son eleman[[-1]:\n""", veri.SozlukluListe_[0],"...",veri.SozlukluListe_[-1], style="yellow")
        
        if veri.TupleliListe_:
                veri.TupleliListe_.clear()

    return veri.SozlukluListe_ 
                
           
                
    

 