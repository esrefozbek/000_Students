#~  3 Silmeye girince bilgilendirme kısmında son eklenen Id numaraları gelsin !!!!!!!!

 
#FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.   Bu tüm listeyi görmek için bir vantaj mı yoksa hata mı
#FIXME -  Silmeden çıkmak için Esc ye bas,  Devam etmek için Enter  çıkmak için tekrar Esc ye bas seçeneği iyi olur.  
#FIXME -  bu sayfadaki kodlar Revize edilmeli. 
#FIXME - "İndeksler:"   kısmı "İndeksler or Esc"   olarak değiştirilmeli.  
 

import AnaFonksiyonlar.JSON_jobs as JSON_
import VERI.emptyLists as EMPTY_LISTS 
import VERI.mesajlar as MESAJLAR 
import AsistanFonksiyonlar.arama as Arama
import AsistanFonksiyonlar.onayE_H as OnayE_H

from rich.panel import Panel
from rich.console import Console; c = Console()
from rich.columns import Columns

from InquirerPy import inquirer
from rich import print as p


  
def Silme_AnaFonksiyon():
  while True:
        klavye=Bul()   # returned:  aranan bir kelime girilmedi ESC ye basıldı demek . 
        if klavye is None:
            break
        else:
            p("SİL>>AnaFonksiyon():: returned:",klavye)
            if EMPTY_LISTS.TekKriterinBulunanlari:
                    WhichToDelete()
                    farkListesiOlusturma()
                    Sil()
            else:
                continue
    
    
    
                          

def Bul():
    
    while True:
        Cleaning()
        klavye=Arama.bul_AnaFonksiyon(2)  #/ Bulunanlar listesi dolduruldu. Esc ile çıkılır Tekrar SilmeAnafonksiyona dönülür.   
        c.print("Sil>>Bul:   Returnned  <<1>>", klavye)
        if klavye is None: #_ Nonw demek Esc ye basıldı demek.  Birşey bulunmaması ise "" demek. 
           c.print("sil>> Bul() :  ESC ye basıldı  ",style="deep_sky_blue1")
        return klavye
    
          


def WhichToDelete():
    from InquirerPy import inquirer
    EMPTY_LISTS.KellesiGidenler_Listesi.clear()
    MESAJLAR.Mesajlar(22)
    
    #EMPTY_LISTS.silinmesi_istenilenler_Stringi =Arama.InputwithESCAPE () 
    
    from InquirerPy.base.control import Choice
    EMPTY_LISTS.KellesiGidenler_Listesi = inquirer.checkbox(
            message="Seçmek istediğiniz öğrencileri seçin:",
            choices=[Choice(name=f"{ogrenci['ad']} {ogrenci['soyad']} ({ogrenci['Id']})",value=(ogrenci["Id"], ogrenci["ad"], ogrenci["soyad"])) for ogrenci in EMPTY_LISTS.TotalBulunanlar]
            ).execute()
              
    print(f"KellesiGidenler_Listesi1: { EMPTY_LISTS.KellesiGidenler_Listesi}")
    EMPTY_LISTS.KellesiGidenler_Listesi=[str(ogr[0]) for ogr in EMPTY_LISTS.KellesiGidenler_Listesi ]
    print(f"KellesiGidenler_Listesi2: { EMPTY_LISTS.KellesiGidenler_Listesi}")
    
    if EMPTY_LISTS.KellesiGidenler_Listesi:
        MESAJLAR.Mesajlar(10)
    
        
    
    
  

def farkListesiOlusturma():
    EMPTY_LISTS.FARK_SozlukListesi = [ogrenci for ogrenci in EMPTY_LISTS.TotalBulunanlar if ogrenci['Id'] in [int(i) for i in EMPTY_LISTS.KellesiGidenler_Listesi] ]
    
    c.print(" SİLME >>FArkListesi:: EMPTY_LISTS.FARK_SozlukListesi >>",EMPTY_LISTS.FARK_SozlukListesi)
                         

def Sil():
    if EMPTY_LISTS.FARK_SozlukListesi:
        SilmeSureci(EMPTY_LISTS.FARK_SozlukListesi)
        if EMPTY_LISTS.FARK_SozlukListesi==[]:
            EMPTY_LISTS.silindilerListesi.extend(EMPTY_LISTS.FARK_SozlukListesi)
                            #/ tamam mı devam mı  soralım 
def SilmeSureci(liste):
    toplamOgr=len(liste)
    p("SİL>>SilmeSüreci:: liste len'i:",len(liste) )
    #liste = [dict(t) for t in {tuple(sorted(d.items())) for d in liste}] #. tekrar eden şahısları listeden çıkardık, tek örnek bıraktık.
    
    p(">>silmeSüreci>> liste len'i:",len(liste) )

    p("SİL>>SilmeSüreci>> liste:", liste      )
    silinen_öğrenci_sayısı=0 
    for ogr in liste:
        ogr=ogr["ad"] +" "+ ogr["soyad"] +" "+ ogr["ogrenciNumarasi"]
        if OnayE_H.Evet_Hayır_OnayiAl(ogr): 
                JSON_.SozluktenEksiltme(EMPTY_LISTS.Jsonda_Mevcut_Veriler, ogr ) 
                silinen_öğrenci_sayısı+=1 
        else:
            continue
    
    EMPTY_LISTS.TekKriterinBulunanlari.clear()
    EMPTY_LISTS.FARK_SozlukListesi.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    
    if silinen_öğrenci_sayısı>0:
        c.print(f"\n{silinen_öğrenci_sayısı} öğrenci silindi. ", style="bold red")
      #  c.print(f"SİLME>> {toplamOgr-silinen_öğrenci_sayısı} TALEBEnin KAYDI silinmedi", style="bold green")
    else:
        p("Talebelere dokanılmadı")




def Cleaning():
    EMPTY_LISTS.TekKriterinBulunanlari.clear()
    EMPTY_LISTS.FARK_SozlukListesi.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    EMPTY_LISTS.silindilerListesi.clear()   #??????  session süresince silinenleri değilde bir seferlik .....