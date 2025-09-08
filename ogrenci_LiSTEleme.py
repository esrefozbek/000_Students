from rich.panel import Panel
from rich.console import Console;console=Console()
from rich.table import Table
import tablolarPY
import veri
import dilimleme



# Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
def altAltaOgrenciListesi(value):
    kaçarKaçar = value if value is not None else 8  # kaçarlı dilimler yapalım        
    veri.TupleliListe_.sort()
    dilimleme.gptDilimleme(kaçarKaçar, liste=veri.TupleliListe_) 
    

def silinmişKayıtlılarListesiDökümü():
    menüTipi="Silinmişler"
    listeTipi="Silinmişler"
    if veri.silinmislerListesi_:
        tablolarPY.TABLO_6lı(veri.silinmislerListesi_,menüTipi, listeTipi )
    else:
        print( "Henüz Öğrenci Kayıdı silinmedi. ")


def yeniEklenenOgrencilerListesiDökümü():
    menüTipi="Yeni Eklenenler"
    listeTipi="Yeni Eklenenler"
    if veri.yeniEklenenlerListesi_:     
        tablolarPY.TABLO_6lı(veri.yeniEklenenlerListesi_,menüTipi, listeTipi )
    else:
        console.print("Henüz yeni öğrenci Kayıdı yapılmadı. ",style="bold green")



