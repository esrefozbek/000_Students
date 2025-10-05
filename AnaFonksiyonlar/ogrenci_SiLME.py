#~  3 Silmeye girince bilgilendirme kısmında son eklenen Id numaraları gelsin !!!!!!!!
 
def Cleaning():
    EMPTY_LISTS.TekKriterinBulunanlari.clear()
    EMPTY_LISTS.FARK_SozlukListesi.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    EMPTY_LISTS.silindilerListesi.clear()   #??????  session süresince silinenleri değilde bir seferlik .....

#from prompt_toolkit.shortcuts import checkboxlist_dialog
import AnaFonksiyonlar.JSON_jobs as JSON_
import VERI.emptyLists as EMPTY_LISTS 
import VERI.mesajlar as MESAJLAR 
import AsistanFonksiyonlar.arama as Arama
import AsistanFonksiyonlar.onayE_H as OnayE_H

from rich.panel import Panel
from rich.console import Console; c = Console()
from rich.columns import Columns

from rich import print as p
import MenuTablo.tablolarPY as TABLO


#from InquirerPy import inquirer
#from prompt_toolkit.shortcuts import checkboxlist_dialog
#from prompt_toolkit.styles import Style
#from prompt_toolkit.key_binding import KeyBindings

 
def Silme_AnaFonksiyon():
  while True:
        klavye=Bul()   # returned:  aranan bir kelime girilmedi ESC ye basıldı demek . 
        if klavye is None:
            break
        else:
       #     c.print("\nSİL>>AnaFonksiyon():: Returned:",klavye,end="\n")
       #     c.print("\n")
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
   #     c.print("\n👌👌🐷🐷🐷  Sil>>Bul:   Returnned  <<1>>", klavye,end="\n")
        if klavye is None: #_ Nonw demek Esc ye basıldı demek.  Birşey bulunmaması ise "" demek. 
          c.print("\n ♥️♥️ 🐷🐷🐷  sil>> Bul() :  ESC ye basıldı  ",style="deep_sky_blue1",end="\n")
        return klavye
    
          
def WhichToDelete():
    from InquirerPy import inquirer
    EMPTY_LISTS.KellesiGidenler_Listesi.clear()
#    MESAJLAR.Mesajlar(22)
    
    #EMPTY_LISTS.silinmesi_istenilenler_Stringi =Arama.InputwithESCAPE () 
    
    from InquirerPy.base.control import Choice
    EMPTY_LISTS.KellesiGidenler_Listesi = inquirer.checkbox(
            message="Seçmek istediğiniz öğrencileri seçin:",
            choices=[Choice(name=f"{ogrenci['ad']} {ogrenci['soyad']} ({ogrenci['Id']})",value=(ogrenci["Id"], ogrenci["ad"], ogrenci["soyad"])) for ogrenci in EMPTY_LISTS.TotalBulunanlar]
            ).execute() 
    
    
    """ import questionary
    EMPTY_LISTS.KellesiGidenler_Listesi = questionary.checkbox(
    "Seçmek istediğiniz öğrencileri seçin:",
    choices=[
        questionary.Choice(
            title=f"{ogrenci['ad']} {ogrenci['soyad']} ({ogrenci['Id']})",
            value=(ogrenci["Id"], ogrenci["ad"], ogrenci["soyad"])
        )
        for ogrenci in EMPTY_LISTS.TotalBulunanlar
    ]
    ).ask()
      """


              
   # print(f"\nKellesiGidenler_Listesi 1: { EMPTY_LISTS.KellesiGidenler_Listesi} \n")
    EMPTY_LISTS.KellesiGidenler_Listesi=[str(ogr[0]) for ogr in EMPTY_LISTS.KellesiGidenler_Listesi ]
   # print(f"\n 💰💰💰 KellesiGidenler_Listesi2: { EMPTY_LISTS.KellesiGidenler_Listesi}\n")
    
    if EMPTY_LISTS.KellesiGidenler_Listesi:
        MESAJLAR.Mesajlar(10)
    
    

def farkListesiOlusturma():
    EMPTY_LISTS.FARK_SozlukListesi = [ogrenci for ogrenci in EMPTY_LISTS.TotalBulunanlar if ogrenci['Id'] in [int(i) for i in EMPTY_LISTS.KellesiGidenler_Listesi] ]
   
    
 #   c.print("\n 🇹🇷 🇹🇷 🏀🏀🏀  SS SİLME >>FArkListesi:: EMPTY_LISTS.FARK_SozlukListesi >>",EMPTY_LISTS.FARK_SozlukListesi,end="\n")
                         

def Sil():
    if EMPTY_LISTS.FARK_SozlukListesi:
        SilmeSureci(EMPTY_LISTS.Jsonda_Mevcut_Veriler, EMPTY_LISTS.FARK_SozlukListesi)
        if EMPTY_LISTS.FARK_SozlukListesi==[]:
            EMPTY_LISTS.silindilerListesi.extend(EMPTY_LISTS.FARK_SozlukListesi)
                            #/ tamam mı devam mı  soralım 
   
                            
def SilmeSureci(OGR_JSON:list,FarkListesi:list):
    toplamOgr=len(FarkListesi)  #
#    p("🍷🍷🍷 SİL>>SilmeSüreci:: FARK LİSTESİ len'i >>",len(FarkListesi) )
#    p("🍀🍀🍀 SİL>>SilmeSüreci:: FARK LİSTESİ >>", FarkListesi)
    
    silinen_öğrenci_sayısı=0 
    for ogr in FarkListesi: 
   #     ogrenci=ogr["ad"] +" "+ ogr["soyad"] +" "+ ogr["ogrenciNumarasi"]
#        c.print("🫑🫑🫑 SİL>>SilmeSüreci:: FarkListesi",FarkListesi, ogrenci)

        
        if OnayE_H.Evet_Hayır_OnayiAl(ogr): 
                JSON_.SozluktenEksiltme(OGR_JSON, ogr) 
                silinen_öğrenci_sayısı+=1 
        else:
            continue
    
    

    
  #  p("SİL>>SilmeSüreci:: Jsonda_Mevcut_Veriler[-2:] >>",EMPTY_LISTS.Jsonda_Mevcut_Veriler[-2:])
    EMPTY_LISTS.TekKriterinBulunanlari.clear()
    EMPTY_LISTS.FARK_SozlukListesi.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    
    if silinen_öğrenci_sayısı>0:
        c.print(f"\n{silinen_öğrenci_sayısı} öğrenci silindi. ", style="bold red")
      #  c.print(f"SİLME>> {toplamOgr-silinen_öğrenci_sayısı} TALEBEnin KAYDI silinmedi", style="bold green")
    else:
        p("🌽🌽Talebelere dokanılmadı🌽🌽")



