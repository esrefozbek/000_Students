#from veri import TupleliListe_,SözlüklüListe_
import VERİ
from rich.console import Console; console = Console()


#ANCHOR -  tuple içeren liste SÖZLÜĞE dönüştürülüyor. 

def TupleyiSözlükYap(liste:list=VERİ.TupleliListe_):
    console.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] başlıyor......  ")
    console.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] SözlüklüListe_ nin durumu:",VERİ.SözlüklüListe_)
        
    if VERİ.SözlüklüListe_:  
        VERİ.SözlüklüListe_.clear()                                              
    
    for TupleClassNesnesi in liste:
        VERİ.SözlüklüListe_.append({
            "id": TupleClassNesnesi[0],
            "ad": TupleClassNesnesi[1],
            "soyad": TupleClassNesnesi[2],
            "öğrenciNumarası":TupleClassNesnesi[3],
            "dogum_yili": TupleClassNesnesi[4],
            "sinif": TupleClassNesnesi[5],
            "kayıtTarihi":TupleClassNesnesi[6]
        })
    console.print("[bold yellow]TupleyiSözlükYap_():[/bold yellow] Dolum sonrası SözlüklüListe_:↩️",VERİ.SözlüklüListe_[-2:])
    
    #NOTE - VERİ.SözlüklüListe_ nin bir kopyasını oluşturarak YEDEK.json dosyasına  kayıt işleminde kullanacağız. 
    if VERİ.SözlüklüListe_:
        VERİ.yedekSözlüklüListe_=VERİ.SözlüklüListe_.copy()
        
         
        
        console.print ("\n[bold magenta]Tupleyi Sözlükleştirme:[/bold magenta] ♻️ ♻️ Tuplenin sözlüğe dönüştürülüp SözlüklüListe_ ye kayıt işlemi tamamlandı Allah'ın izniyle  ,\n",style="")
        console.print (f"""[bold magenta]Tupleyi Sözlükleştirme:[/bold magenta]
\n[bold black]
☢️  İstatistiklerim: ☢️ [/bold black]
[yellow]Sözlük listenin tipi:[/yellow]{type(VERİ.SözlüklüListe_)}
[yellow]Herbir elemanın tipi[0]:[/yellow]{type(VERİ.SözlüklüListe_[0])}
[yellow]Sözlüğün uzunluğu:[/yellow]{len(VERİ.SözlüklüListe_)}
[white]SözlüklüListeden bir örnek alınmış hali:[/white]\n""",style="yellow")
        console.print (f"""SözlüklüListe_nin ilk elemanı[0] ve son eleman[[-1]:\n""", VERİ.SözlüklüListe_[0],"...",VERİ.SözlüklüListe_[-1], style="yellow")
        
        if VERİ.TupleliListe_:
                VERİ.TupleliListe_.clear()

    return VERİ.SözlüklüListe_ 
                
           
                
    

 