from rich.panel import Panel
from rich.console import Console;console=Console()
from rich.table import Table
import tablolarPY
import VERİ
import dilimleme



# Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
def altAltaOgrenciListesi(value):
    kaçarKaçar = value if value is not None else 8  # kaçarlı dilimler yapalım        
    VERİ.TupleliListe_.sort()
    dilimleme.gptDilimleme(kaçarKaçar, liste=VERİ.TupleliListe_) 
    

def silinmişKayıtlılarListesiDökümü():
    menüTipi="Silinmişler"
    listeTipi="Silinmişler"
    if VERİ.silinmişlerListesi_:
        tablolarPY.TABLO_6lı(VERİ.silinmişlerListesi_,menüTipi, listeTipi )
    else:
        print( "Henüz Öğrenci Kayıdı silinmedi. ")


def yeniEklenenOgrencilerListesiDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if VERİ.yeniEklenenlerListesi_:     
        tablolarPY.TABLO_6lı(VERİ.yeniEklenenlerListesi_,menüTipi, listeTipi )
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")



