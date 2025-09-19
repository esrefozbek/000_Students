from rich.panel import Panel
from rich.console import Console;console=Console()
from rich.table import Table
import MenuTablo.tablolarPY as TablolarPY
import VERI.emptyLists as EmptyLists
import AsistanFonksiyonlar.dilimleme as Dilimleme



# Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
def altAltaOgrenciListesi(value):
    kaçarKaçar = value if value is not None else 8  # kaçarlı dilimler yapalım        
    EmptyLists.Jsonda_Mevcut_Veriler.sort()
    Dilimleme.gptDilimleme(kaçarKaçar, liste=EmptyLists.Jsonda_Mevcut_Veriler) 
    

def silinmişKayıtlılarListesiDökümü():
    menüTipi="Silinmişler"
    listeTipi="Silinmişler"
    if EmptyLists.silindilerListesi:
        TablolarPY.TABLO_6lı(EmptyLists.silindilerListesi,menüTipi, listeTipi )
    else:
        print( "Henüz Öğrenci Kayıdı silinmedi. ")


def yeniOgrListesiDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if EmptyLists.eklendilerListesi:     
        TablolarPY.TABLO_6lı(EmptyLists.eklendilerListesi,menüTipi, listeTipi )
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")
        

def yeniOgrListesiSözlükDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if EmptyLists.SozlukluListe_Kopya:     
        TablolarPY.TABLO_6lı(EmptyLists.SozlukluListe_Kopya,menüTipi, listeTipi )
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")



