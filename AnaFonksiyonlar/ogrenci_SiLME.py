
 
 #FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.   Bu tüm listeyi görmek için bir vantaj mı yoksa hata mı
 #FIXME -  Silmeden çıkmak için Esc ye bas,  Devam etmek için Enter  çıkmak için tekrar Esc ye bas seçeneği iyi olur.  
 #FIXME -  bu sayfadaki kodlar Revize edilmeli. 
 #FIXME - "İndeksler:"   kısmı "İndeksler or Esc"   olarak değiştirilmeli.  
 

import AnaFonksiyonlar.JSON_jobs as ANAMODUL
import VERI.emptyLists as EMPTY_LISTS 
import VERI.mesajlar as MESAJLAR 
import re
import AsistanFonksiyonlar.arama as Arama
import AsistanFonksiyonlar.klavyeDinleme as KLAVYE_DINLE
import AsistanFonksiyonlar.onayE_H as OnayE_H
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as AsistanModul

from rich.console import Console; c = Console()
from rich import print as p
from rich.panel import Panel


# import questionary


aramaSayisi=1
hatalilar=[] 
hatasizlar=[]
    
def Silme_AnaFonksiyon():
    global metin1,metin2,aramaSayisi, hatalilar, hatasizlar
    EMPTY_LISTS.FARK_SozlukListesi.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    EMPTY_LISTS.silindilerListesi.clear()

    sonuc=Arama.bul_AnaFonksiyon(2)  #_     Bulunanlar listesi dolduruldu.  
    #veriYolu.Bulunanlar=[] if veriYolu.Bulunanlar is None else veriYolu.Bulunanlar
   
    EMPTY_LISTS.silinmesi_istenilenler =Arama.InputwithESCAPE (2)
    Arama.Parsing(EMPTY_LISTS.silinmesi_istenilenler) ;p("\n")  
    p(Panel.fit(str(EMPTY_LISTS.ParsedSTRING_Listesi), title=" ParsedSTRING_Listesi ",     style="white"))   
    Silinmesi_istenilenlerinCTRL(EMPTY_LISTS.ParsedSTRING_Listesi)
    if hatasizlar==[]:
        Silme_AnaFonksiyon()
        MESAJLAR.Mesajlar(22)   #Silinmesini istediğiniz ID NUMARALARI 
        MESAJLAR.Mesajlar(4) # Silinecek öğrencilerin numaralarını girin. Sayıları boşluk veya virgül ile ayırabilirsiniz.
    
    else:
        #_    p("\nSilme>ogrSil:  VeriYolu.Bulunanlar>>", VERI.Bulunanlar) 
        hatasizlar = list(set(hatasizlar))
        EMPTY_LISTS.FARK_SozlukListesi = [ogrenci for ogrenci in EMPTY_LISTS.Bulunanlar if ogrenci['Id'] in [int(i) for i in hatasizlar] ]
        
        SilmeSureci(EMPTY_LISTS.FARK_SozlukListesi)
        
        
    #_   c.print("",VERI.FARK_SozlukListesi,style="magenta")  
    
    

        c.print(MESAJLAR.Mesajlar(6) if aramaSayisi != 1 else MESAJLAR.Mesajlar(7))


                
            
        #! tekrar tekrar girilmiş sayıyı  silmek için SET yapıyoruz, tekrarlı indeksleri ayıkla
                        
                
                    
        silinen_öğrenci_sayısı:int=0           
        
        EMPTY_LISTS.silindilerListesi.extend(EMPTY_LISTS.FARK_SozlukListesi)
                    
                    
            
#~    VERI.FARK_SozlukListesi=AsistanModul.TupleyiSözlükListesineEkle(VERI.FARK_SozlukListesi) tupleleri yedim Bitti o iş.
#~    p("silme  :   veriYolu.FARK_SozlukListesi >> ",VERI.FARK_SozlukListesi)        


def SilmeSureci(liste):
    silinen_öğrenci_sayısı=0 
    for silinen_öğrenci_sayısı, sozluk  in enumerate(liste, start=1):
        ogr=sozluk["ad"], sozluk["soyad"], sozluk["ogrenciNumarasi"]
        if OnayE_H.Evet_Hayır_OnayiAl(ogr): 
                ANAMODUL.SozluktenEksiltme(EMPTY_LISTS.Jsonda_Mevcut_Veriler, sozluk ) 
        else:
            silinen_öğrenci_sayısı=0 
            continue
            
        
    EMPTY_LISTS.FARK_SozlukListesi.clear()
    EMPTY_LISTS.Bulunanlar.clear()
    EMPTY_LISTS.FARK_SozlukListesi.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
            
        
    if silinen_öğrenci_sayısı>0:
        c.print(f"{silinen_öğrenci_sayısı} öğrenci başarıyla silindi. 😄😄 ", style="bold red")
    else:
        c.print(f"SİLME>> Hiçbir TALEBE KAYDI silinmedi", style="bold green")
            
        
#~  3 Silmeye girince bilgilendirme kısmında son eklenen Id numaraları gelsin !!!!!!!!





def    Silinmesi_istenilenlerinCTRL(veri): 
        global hatalilar, hatasizlar , aramaSayisi
        hatalilar=[] 
        hatasizlar=[]
        hatalı_var = False    #? bayrak 
        hatalı_var = False
        for istenenlerdenBiri in veri : 
            if istenenlerdenBiri.isdigit():
                if 0 <= int(istenenlerdenBiri) < len(EMPTY_LISTS.Jsonda_Mevcut_Veriler):
                    pass
                else:
                    hatalilar.append(istenenlerdenBiri)
                    hatalı_var = True
                if int(istenenlerdenBiri) in EMPTY_LISTS.BulunanIDler:
                    hatasizlar.append(istenenlerdenBiri)
                else:
                    hatalilar.append(istenenlerdenBiri)
            else: #_ isdigit()'in else'si. 
                hatalilar.append(istenenlerdenBiri)
                hatalı_var = True
            if hatalı_var: aramaSayisi += 1; continue    #?  digit değilse veya yanlış sayı girildiyse CONTINUE yapılır.
        
        
        p(Panel.fit(f"{hatalilar}",title="  hatalı girişler  ",     style="grey89"))
        p(Panel.fit(f"{hatasizlar}",title=" hatasizSecimleriniz ",     style="grey39"))
        