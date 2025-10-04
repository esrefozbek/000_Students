from rich.panel import Panel
from rich.console import Console;console=Console()
from rich.table import Table
import MenuTablo.tablolarPY as TABLO
import VERI.emptyLists as E_LISTS
import AsistanFonksiyonlar.dilimleme as Dilimleme



# Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
def altAltaOgrenciListesi(value):
    kaçarKaçar = value if value is not None else 8  # kaçarlı dilimler yapalım        
    E_LISTS.Jsonda_Mevcut_Veriler
    if E_LISTS.Jsonda_Mevcut_Veriler: 
        Dilimleme.gptDilimleme(kaçarKaçar, liste=E_LISTS.Jsonda_Mevcut_Veriler) 
    else:
        print("EMPTY_LISTS.Jsonda_Mevcut_Veriler  BOŞŞ")

def silinmişKayıtlılarListesiDökümü():
    menüTipi="Silinmişler"
    listeTipi="Silinmişler"
    if E_LISTS.silindilerListesi:
        TABLO.tabloyaGonder(E_LISTS.silindilerListesi)
    else:
        print( "Henüz Öğrenci Kayıdı silinmedi. ")


def yeniOgrListesiDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if E_LISTS.eklendilerListesi:     
        TABLO.tabloyaGonder(E_LISTS.silindilerListesi)
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")
        

def yeniOgrListesiSözlükDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if E_LISTS.SozlukluListe_Kopya:     
        TABLO.tabloyaGonder(E_LISTS.silindilerListesi)
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")



