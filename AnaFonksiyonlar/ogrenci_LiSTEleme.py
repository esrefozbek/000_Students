from rich.panel import Panel
from rich.console import Console;console=Console()
from rich.table import Table
import MenuTablo.tablolarPY as TablolarPY
import VERI.emptyLists as veriYolu
import AsistanFonksiyonlar.dilimleme as Dilimleme



# Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
def altAltaOgrenciListesi(value):
    kaçarKaçar = value if value is not None else 8  # kaçarlı dilimler yapalım        
    veriYolu.Jsonda_Mevcut_Veriler
    Dilimleme.gptDilimleme(kaçarKaçar, liste=veriYolu.Jsonda_Mevcut_Veriler) 
    

def silinmişKayıtlılarListesiDökümü():
    menüTipi="Silinmişler"
    listeTipi="Silinmişler"
    if veriYolu.silindilerListesi:
        TablolarPY.genel_TABLO(veriYolu.silindilerListesi, )
    else:
        print( "Henüz Öğrenci Kayıdı silinmedi. ")


def yeniOgrListesiDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if veriYolu.eklendilerListesi:     
        TablolarPY.genel_TABLO(veriYolu.eklendilerListesi, )
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")
        

def yeniOgrListesiSözlükDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if veriYolu.SozlukluListe_Kopya:     
        TablolarPY.genel_TABLO(veriYolu.SozlukluListe_Kopya,)
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")



