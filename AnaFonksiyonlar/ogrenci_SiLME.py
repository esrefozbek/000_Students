#~  3 Silmeye girince bilgilendirme kısmında son eklenen Id numaraları gelsin !!!!!!!!

 
#FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.   Bu tüm listeyi görmek için bir vantaj mı yoksa hata mı
#FIXME -  Silmeden çıkmak için Esc ye bas,  Devam etmek için Enter  çıkmak için tekrar Esc ye bas seçeneği iyi olur.  
#FIXME -  bu sayfadaki kodlar Revize edilmeli. 
#FIXME - "İndeksler:"   kısmı "İndeksler or Esc"   olarak değiştirilmeli.  
 

import AnaFonksiyonlar.JSON_jobs as ANAMODUL
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
        returned=Bul()   # returned:  aranan bir kelime girilmedi ESC ye basıldı demek . 
        if returned is None:
            break
        else:
            p("SİL>>Ana:: returned:",returned)
            if EMPTY_LISTS.TekKriterinBulunanlari:
                    WhichToDelete()
                    farkListesiOlusturma()
                    Sil()
            else:
                continue
                          

def Bul():
    
    while True:
        Cleaning()
        returned=Arama.bul_AnaFonksiyon(2)  #/ Bulunanlar listesi dolduruldu. Esc ile çıkılır Tekrar SilmeAnafonksiyona dönülür.   
        c.print("Sil>>Bul:   Returnned  << 1 >>", returned)
        if returned is None: #_ Nonw demek Esc ye basıldı demek.  Birşey bulunmaması ise "" demek. 
           c.print("sil>> bul :  ESC ye basıldı  ",style="deep_sky_blue1")
        
        
        return returned
    
          


def WhichToDelete():
    from InquirerPy import inquirer
    
    while True:
            EMPTY_LISTS.parsedKriterler_Listesi.clear()
            MESAJLAR.Mesajlar(22)
            
            #EMPTY_LISTS.silinmesi_istenilenler_Stringi =Arama.InputwithESCAPE () 
            
            
            EMPTY_LISTS.parsedKriterler_Listesi = inquirer.checkbox(
                message="??",
                choices=EMPTY_LISTS.BulunanAdSoyadIDler,
               ).execute()
            EMPTY_LISTS.BulunanAdSoyadIDler.clear()

          #  print(f"Seçilenler: {EMPTY_LISTS.silinmesi_istenilenler_Stringi}")
            print(f"KellesiGidenler_Listesi: { EMPTY_LISTS.parsedKriterler_Listesi}")
            EMPTY_LISTS.parsedKriterler_Listesi=[str(ogr[0]) for ogr in EMPTY_LISTS.parsedKriterler_Listesi ]
            print(f"KellesiGidenler_Listesi: { EMPTY_LISTS.parsedKriterler_Listesi}")
            
            
            print(f"KellesiGidenler_Listesi: { EMPTY_LISTS.parsedKriterler_Listesi}")
            
            if  EMPTY_LISTS.parsedKriterler_Listesi is None:
                break
            if EMPTY_LISTS.parsedKriterler_Listesi:
                
                MESAJLAR.Mesajlar(10)
            Silinmesi_istenilenlerinCTRL(EMPTY_LISTS.parsedKriterler_Listesi) #/  hatali ve hatasız istekler ayrışır.
            if EMPTY_LISTS.hatasizlar:
                break
            else:
                p(" geçerli bir Id girmelisin adamım" )
    
    
  
    
    
      
            


def farkListesiOlusturma():
    if EMPTY_LISTS.hatasizlar is not None:
        hatasizlar = list(set(EMPTY_LISTS.hatasizlar))
        EMPTY_LISTS.FARK_SozlukListesi = [ogrenci for ogrenci in EMPTY_LISTS.TekKriterinBulunanlari if ogrenci['Id'] in [int(i) for i in hatasizlar] ]
                         

def Sil():
    if EMPTY_LISTS.FARK_SozlukListesi:
        SilmeSureci(EMPTY_LISTS.FARK_SozlukListesi)
        EMPTY_LISTS.silindilerListesi.extend(EMPTY_LISTS.FARK_SozlukListesi)
                            #/ tamam mı devam mı  soralım 
    

    

           #silinen_öğrenci_sayısı:int=0     


def    Silinmesi_istenilenlerinCTRL(liste): 
    global aramaSayisi
    hatalı_var = False    #? bayrak 
    
    for istenenlerdenBiri in liste :  #/ istenenlerdenBiri liste de mi , listede ise.... 
        if not istenenlerdenBiri.isdigit():
            EMPTY_LISTS.hatalilar.append(istenenlerdenBiri)
            hatalı_var = True
        else:
                if int(istenenlerdenBiri) in EMPTY_LISTS.BulunanIDler:
                    EMPTY_LISTS.hatasizlar.append(istenenlerdenBiri)
                else:
                    EMPTY_LISTS.hatalilar.append(istenenlerdenBiri)
        
        if EMPTY_LISTS.hatasizlar or EMPTY_LISTS.hatalilar: EMPTY_LISTS.aramaSayisi += 1; 
        continue   #/  digit değilse veya yanlış sayı girildiyse CONTINUE yapılır. 
    
    panel1=Panel.fit(f"{EMPTY_LISTS.hatasizlar}",title="[red]Hatasızlar[/]",   border_style="bright_white",    style="green")
    panel2=Panel.fit(f"{EMPTY_LISTS.hatalilar}",title="[green]Hatalılar[/]",   border_style="bright_yellow",    style="magenta")
    # Yan yana göstermek için Columns kullan
    c.print(Columns([panel1, panel2], equal=True, expand=False))
        
        


def SilmeSureci(liste):
    toplamOgr=len(liste)
    p("sil>>silmeSüreci>> liste len'i:",len(liste) )
    liste = [dict(t) for t in {tuple(sorted(d.items())) for d in liste}] #. tekrar eden şahısları listeden çıkardık, tek örnek bıraktık.
    
    p("sil>>silmeSüreci>> liste len'i:",len(liste) )

    p("sil>>silmeSüreci>> liste:", liste      )
    silinen_öğrenci_sayısı=0 
    for  sozluk  in liste:
        ogr=sozluk["ad"] +" "+ sozluk["soyad"] +" "+ sozluk["ogrenciNumarasi"]
        if OnayE_H.Evet_Hayır_OnayiAl(ogr): 
                ANAMODUL.SozluktenEksiltme(EMPTY_LISTS.Jsonda_Mevcut_Veriler, sozluk ) 
                silinen_öğrenci_sayısı+=1 
        else:
            continue
    
    EMPTY_LISTS.TekKriterinBulunanlari.clear()
    EMPTY_LISTS.FARK_SozlukListesi.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    
    if silinen_öğrenci_sayısı>0:
        c.print(f"\n{silinen_öğrenci_sayısı} öğrenci silindi. ", style="bold red")
        c.print(f"SİLME>> {toplamOgr-silinen_öğrenci_sayısı} TALEBEnin KAYDI silinmedi", style="bold green")
    else:
        p("Talebelere dokanılmadı")




def Cleaning():
    EMPTY_LISTS.TekKriterinBulunanlari.clear()
    EMPTY_LISTS.hatalilar=[] 
    EMPTY_LISTS.hatasizlar=[]
    EMPTY_LISTS.FARK_SozlukListesi.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    EMPTY_LISTS.silindilerListesi.clear()