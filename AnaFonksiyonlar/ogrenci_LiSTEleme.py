from rich.panel import Panel
from rich.console import Console;console=Console()
from rich.table import Table
import MenuTablo.tablolarPY as TablolarPY
import VERI.emptyLists as Veri_Yolu
import AsistanFonksiyonlar.dilimleme as Dilimleme



# Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
def altAltaOgrenciListesi(value):
    kaçarKaçar = value if value is not None else 8  # kaçarlı dilimler yapalım        
    Veri_Yolu.TupleliListe_.sort()
    Dilimleme.gptDilimleme(kaçarKaçar, liste=Veri_Yolu.TupleliListe_) 
    

def silinmişKayıtlılarListesiDökümü():
    menüTipi="Silinmişler"
    listeTipi="Silinmişler"
    if Veri_Yolu.silinmislerListesi_:
        TablolarPY.TABLO_6lı(Veri_Yolu.silinmislerListesi_,menüTipi, listeTipi )
    else:
        print( "Henüz Öğrenci Kayıdı silinmedi. ")


def yeniOgrListesiDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if Veri_Yolu.yeniEklenenlerTupleListesi_Kopyasi:     
        TablolarPY.TABLO_6lı(Veri_Yolu.yeniEklenenlerTupleListesi_Kopyasi,menüTipi, listeTipi )
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")
        

def yeniOgrListesiSözlükDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if Veri_Yolu.SozlukluListe_Kopya:     
        TablolarPY.TABLO_6lı(Veri_Yolu.SozlukluListe_Kopya,menüTipi, listeTipi )
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")



