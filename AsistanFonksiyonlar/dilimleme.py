from rich.console import Console; console = Console()
from rich.table import Table
from rich.panel import Panel
from rich import box
import AsistanFonksiyonlar.klavyeDinleme as KLAVYE_DINLE, VERI.emptyLists as EMPTY,math,time,Widgetler.SayacAnimasyon.sayacKronometre as Say_Kro
import  MenuTablo.tablolarPY as TABLO
 


#NOTE - Eşref DİLİMLEME
def dilimleme(value,liste):
    menüTipi="Dilimlenmiş Ana Liste"
    listeTipi="Dilimlenmiş Tüm Liste"
    kaçarKaçar = value if value is not None else 10  # kaçarlı dilimler yapalım
    EMPTY.ListeDilimi = []
    for idx, i in enumerate(liste):
        EMPTY.ListeDilimi.append(i)
        if (idx + 1) % kaçarKaçar == 0:  # Her 8 elemanda bir tablo yazdır
            TABLO.genel_TABLO(EMPTY.ListeDilimi, )
            EMPTY.ListeDilimi = []  # Dilimi sıfırla
            KLAVYE_DINLE.Enter_ile_devam_et()
    
    # Son dilimi yazdır (kalan elemanlar)
    if EMPTY.ListeDilimi:  # Eğer dilimListe boş değilse
        TABLO.genel_TABLO(EMPTY.ListeDilimi, )
        KLAVYE_DINLE.Enter_ile_devam_et()
        
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
        EMPTY.Dilimlenmiş_alt_liste = liste[baslangic:bitis] 
        TABLO.genel_TABLO(EMPTY.Dilimlenmiş_alt_liste, )
        KLAVYE_DINLE.Enter_ile_devam_et()
        if i>1:
            print("\n\n")
        
        
         
"""         
if __name__ == "__main__":
    console.print("\n[bold yellow]gptDilimleme(value,liste: list):[/bold yellow]VERİ.TupleliListe_:",VERİ.TupleliListe_)
    console.print("[bold yellow]gptDilimleme(value,liste: list):[/bold yellow]VERİ.SözlüklüListe_:",VERİ.SözlüklüListe_)
    
    klavyeDinleme.Enter_ile_devam_et()
     """
    
        
        


