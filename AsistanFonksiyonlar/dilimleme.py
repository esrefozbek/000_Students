from rich.console import Console; console = Console()
from rich.table import Table
from rich.panel import Panel
from rich import box
import AsistanFonksiyonlar.klavyeDinleme as klavDinle, VERI.emptyLists as VERIModul,math,time,Widgetler.SayacAnimasyon.sayacKronometre as Say_Kro
import  MenuTablo.tablolarPY as TablolarPY
 


#NOTE - Eşref DİLİMLEME
def dilimleme(value,liste):
    menüTipi="Dilimlenmiş Ana Liste"
    listeTipi="Dilimlenmiş Tüm Liste"
    kaçarKaçar = value if value is not None else 10  # kaçarlı dilimler yapalım
    VERIModul.dilimListe = []
    for idx, i in enumerate(liste):
        VERIModul.dilimListe.append(i)
        if (idx + 1) % kaçarKaçar == 0:  # Her 8 elemanda bir tablo yazdır
            TablolarPY.TABLO_6lı(VERIModul.dilimListe, menüTipi=f"Dilim {(idx // kaçarKaçar) + 1}", listeTipi=f"Liste Dilimi {(idx // kaçarKaçar) + 1}")
            VERIModul.dilimListe = []  # Dilimi sıfırla
            klavDinle.Enter_ile_devam_et()
    
    # Son dilimi yazdır (kalan elemanlar)
    if VERIModul.dilimListe:  # Eğer dilimListe boş değilse
        TablolarPY.TABLO_6lı(VERIModul.dilimListe, menüTipi=f"Dilim {(len(liste) // kaçarKaçar) + 1}", listeTipi=f"Liste Dilimi {(len(liste) // kaçarKaçar) + 1}")
        klavDinle.Enter_ile_devam_et()
        
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
        VERIModul.alt_liste = liste[baslangic:bitis] 
        TablolarPY.TABLO_6lı(VERIModul.alt_liste, menüTipi,  listeTipi)
        klavDinle.Enter_ile_devam_et()
        if i>1:
            print("\n\n")
        
        
         
"""         
if __name__ == "__main__":
    console.print("\n[bold yellow]gptDilimleme(value,liste: list):[/bold yellow]VERİ.TupleliListe_:",VERİ.TupleliListe_)
    console.print("[bold yellow]gptDilimleme(value,liste: list):[/bold yellow]VERİ.SözlüklüListe_:",VERİ.SözlüklüListe_)
    
    klavyeDinleme.Enter_ile_devam_et()
     """
    
        
        


