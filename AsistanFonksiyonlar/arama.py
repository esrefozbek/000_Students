#FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.

import time
import AsistanFonksiyonlar.klavyeDinleme as klavyeyiDinle
from rich.console import Console; console = Console()
import MenuTablo.tablolarPY as TablolarPY,VERI.emptyLists as EmptyLists 
from rich.live import Live
import time
from rich.console import Console; c=Console()
from rich.spinner import Spinner
import AnaFonksiyonlar.JSON_jobs as AnaModul
import Widgetler.SayacAnimasyon.spinner as Sayac
import Widgetler.SayacAnimasyon.geriSayar as Geri_Sayar

menüTipi="Sorgu Menüsü"
listeTipi="Sorgu Listesi"
EmptyLists.Bulunanlar=[]   #! boş bir sözlükler listesi.



def bul(mesaj:int):
    while True:
        Aranan=InputwithESCAPE(mesaj) 
        if Aranan is None:break 
        arama(Aranan)
 #   Geri_Sayar.GeriSayar(2,"Ana menüye dönülecek (2 saniye)...")





def InputwithESCAPE(mesaj:int=0):
    while True:
        Girilenler=klavyeyiDinle.klavyeÖncesiMesaj(mesaj)
        if Girilenler is  None:
            c.print("Çıkıyoruz...................................",style="green")
            return None    
        elif Girilenler == "":
            c.print("Hiçbir değer girmeden [bright_white]Enter[/] tuşuna bastın Beni boşuna oyalama dostum",style="green")
            continue
        else:    
            Girilenler=Girilenler.strip().lower()
            return Girilenler




def arama(aramaParametresi):
    EmptyLists.Bulunanlar.clear()  #!j - Her sorguda önce temizle 
    EmptyLists.Jsonda_Mevcut_Veriler=[]  #! Temizlik imandandır
    EmptyLists.Jsonda_Mevcut_Veriler.clear() 
    AnaModul.JSONdanImport()  
   
    c.print("arama:arama:  aramaParametresi >>",aramaParametresi)
    c.print("arama:arama: EmptyLists.Bulunanlar 1>>",EmptyLists.Bulunanlar)    
    c.print("arama:arama: EmptyLists.Jsonda_Mevcut_Veriler >>",EmptyLists.Jsonda_Mevcut_Veriler[-2:])    
    
    for ogrenci in EmptyLists.Jsonda_Mevcut_Veriler:
        if(aramaParametresi is not None and aramaParametresi!=""):
            if (aramaParametresi == str(ogrenci["Id"]) or
                aramaParametresi in ogrenci["ad"].lower() or
                aramaParametresi in ogrenci["soyad"].lower() ):
               EmptyLists.Bulunanlar.append(ogrenci)  
            else:
                continue
    c.print("arama::arama: EmptyLists.Bulunanlar [-1] 2>>",EmptyLists.Bulunanlar[-1])    
   
    Sayac.spinner(1,5)
    
    if EmptyLists.Bulunanlar:
        TablolarPY.TABLO_6lı(EmptyLists.Bulunanlar,menüTipi, listeTipi, aramaParametresi)
        
        #   return Bulunanlar
    else:
        c.print("Bu kritere uyan bir öğrenci bulamadım, Üzgünüm.")           
    
   # return Bulunanlar


