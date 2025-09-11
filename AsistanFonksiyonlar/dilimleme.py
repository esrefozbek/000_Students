from rich.console import Console; console = Console()
from rich.table import Table
from rich.panel import Panel
from rich import box
import klavyeDinleme, tablolarPY, veri,math,time,sayacKronometre
 


#NOTE - Eşref DİLİMLEME
def dilimleme(value,liste):
    menüTipi="Dilimlenmiş Ana Liste"
    listeTipi="Dilimlenmiş Tüm Liste"
    kaçarKaçar = value if value is not None else 10  # kaçarlı dilimler yapalım
    veri.dilimListe = []
    for idx, i in enumerate(liste):
        veri.dilimListe.append(i)
        if (idx + 1) % kaçarKaçar == 0:  # Her 8 elemanda bir tablo yazdır
            tablolarPY.TABLO_6lı(veri.dilimListe, menüTipi=f"Dilim {(idx // kaçarKaçar) + 1}", listeTipi=f"Liste Dilimi {(idx // kaçarKaçar) + 1}")
            veri.dilimListe = []  # Dilimi sıfırla
            klavyeDinleme.Enter_ile_devam_et()
    
    # Son dilimi yazdır (kalan elemanlar)
    if veri.dilimListe:  # Eğer dilimListe boş değilse
        tablolarPY.TABLO_6lı(veri.dilimListe, menüTipi=f"Dilim {(len(liste) // kaçarKaçar) + 1}", listeTipi=f"Liste Dilimi {(len(liste) // kaçarKaçar) + 1}")
        klavyeDinleme.Enter_ile_devam_et()
        
#NOTE - gptDilimleme      
def gptDilimleme(value,liste: list):
    menüTipi="Dilimlenmiş Ana Liste"
    listeTipi="Dilimlenmiş Tüm Liste"
    console.print(f"\n[white][[/white] Toplam {len(liste)} TALEBE bulundu[white]][/white] ", style=" bold magenta")
    kaçarlıDilimleme = value if value is not None else 5
    toplam_sayfa = math.ceil(len(liste) / kaçarlıDilimleme)

    for i in range(toplam_sayfa):
        baslangic = i * kaçarlıDilimleme
        bitis = baslangic + kaçarlıDilimleme
        veri.alt_liste = liste[baslangic:bitis] 
        tablolarPY.TABLO_6lı(veri.alt_liste, menüTipi,  listeTipi)
        klavyeDinleme.Enter_ile_devam_et()
        if i>1:
            print("\n\n")
        
        
         
"""         
if __name__ == "__main__":
    console.print("\n[bold yellow]gptDilimleme(value,liste: list):[/bold yellow]VERİ.TupleliListe_:",VERİ.TupleliListe_)
    console.print("[bold yellow]gptDilimleme(value,liste: list):[/bold yellow]VERİ.SözlüklüListe_:",VERİ.SözlüklüListe_)
    
    klavyeDinleme.Enter_ile_devam_et()
     """
    
        
        


