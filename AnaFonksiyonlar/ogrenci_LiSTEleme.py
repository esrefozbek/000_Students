from rich.panel import Panel
from rich.console import Console;console=Console()
from rich.table import Table
import MenuTablo.tablolarPY as TablolarPY
import VERI.emptyLists as VERIModul
import AsistanFonksiyonlar.dilimleme as Dilimleme



# Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
def altAltaOgrenciListesi(value):
    kaçarKaçar = value if value is not None else 8  # kaçarlı dilimler yapalım        
    VERIModul.SilinenlerinTupleliListesi_.sort()
    Dilimleme.gptDilimleme(kaçarKaçar, liste=VERIModul.SilinenlerinTupleliListesi_) 
    

def silinmişKayıtlılarListesiDökümü():
    menüTipi="Silinmişler"
    listeTipi="Silinmişler"
    if VERIModul.silinmislerListesi_:
        TablolarPY.TABLO_6lı(VERIModul.silinmislerListesi_,menüTipi, listeTipi )
    else:
        print( "Henüz Öğrenci Kayıdı silinmedi. ")


def yeniOgrListesiDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if VERIModul.yeniEklenenlerTupleListesi_Kopyasi:     
        TablolarPY.TABLO_6lı(VERIModul.yeniEklenenlerTupleListesi_Kopyasi,menüTipi, listeTipi )
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")
        

def yeniOgrListesiSözlükDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if VERIModul.SozlukluListe_Kopya:     
        TablolarPY.TABLO_6lı(VERIModul.SozlukluListe_Kopya,menüTipi, listeTipi )
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")



