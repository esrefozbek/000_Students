 #£  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
  #€  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
  #?  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
  #~   C:\Users\Markus\AppData\Roaming\Code\User\settings.json   
  #_  asdasdasdasdasda23423424242342       
  #** asddasdsadasadasdad2342342342342342            
 
 #FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.   Bu tüm listeyi görmek için bir vantaj mı yoksa hata mı
 #FIXME -  Silmeden çıkmak için Esc ye bas,  Devam etmek için Enter  çıkmak için tekrar Esc ye bas seçeneği iyi olur.  
 #FIXME -  bu sayfadaki kodlar Revize edilmeli. 
 #FIXME - "İndeksler:"   kısmı "İndeksler or Esc"   olarak değiştirilmeli.  
 

import re
import AsistanFonksiyonlar.arama as Arama
import AsistanFonksiyonlar.klavyeDinleme as klavyeyiDinle
from rich.console import Console; c = Console()
from rich import print as p
import AsistanFonksiyonlar.onayE_H as OnayE_H
import AnaFonksiyonlar.JSON_jobs as AnaModul

import VERI.emptyLists as veriYolu 
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as AsistanModul

# import questionary


aramaSayisi=1
hatalilar=[] 
hatasizlar=[]
    
#~  Evet Hayır onayı nerede ????
#~  3 Silmeye girince bilgilendirme kısmında son eklenen Id numaraları gelsin !!!!!!!!
def ogrenciSil():
    global metin1,metin2,aramaSayisi, hatalilar, hatasizlar
    veriYolu.FARK_SozlukListesi.clear()
    veriYolu.Jsonda_Mevcut_Veriler.clear()
    veriYolu.silindilerListesi.clear()

    
    
    Arama.bul(1)  #_     Bulunanlar listesi dolduruldu.   
    #veriYolu.Bulunanlar=[] if veriYolu.Bulunanlar is None else veriYolu.Bulunanlar
    c.print("Silinmesini istediğiniz ID NUMARALARI || [bold red]Esc[/] >>")
    veriYolu.silinmesi_istenilenler =Arama.InputwithESCAPE (0)
    p("\nSİLME>>str59: silinmesi_istenilenler>>", veriYolu.silinmesi_istenilenler)   
    Arama.Parsing(veriYolu.silinmesi_istenilenler)   #_     EmptyLists.ParsedSTRING_Listesi     
    p("\nSİLME>>str60: EmptyLists.ParsedSTRING_Listesi >>", veriYolu.ParsedSTRING_Listesi )   
    silinmesi_istenilenlerinCTRL(veriYolu.ParsedSTRING_Listesi)
   
    p("\nSilme>ogrSil:  VeriYolu.Bulunanlar>>", veriYolu.Bulunanlar) 
    hatasizlar = list(set(hatasizlar))
    veriYolu.FARK_SozlukListesi = [
    ogrenci for ogrenci in veriYolu.Bulunanlar 
    if ogrenci['Id'] in [int(i) for i in hatasizlar]
]
   
    c.print("SİLME>>str85: hatasizSecimleriniz >>",hatasizlar)
    c.print("SİLME>>str86: EmptyLists.FARK_SozlukListesi  <<1>>",veriYolu.FARK_SozlukListesi)
   
   
   
    
    
    metin1=f"""[yellow]Silinecek öğrencilerin Id numaralarını girin. Sayıları boşluk veya virgül ile ayırabilirsiniz.[/]        
        [bold magenta]Geçerli aralık:[/] 0 - {len(veriYolu.Bulunanlar) - 1} 
        """  
    metin2=f""" [bold white][italic yellow] Lütfen bu sefer dikkatli ol, Tanrı aşkına![/italic yellow] 🙏  Geçerli aralık:[bold yellow] 0 - {len(veriYolu.Bulunanlar) - 1} [/] [/] """

    c.print(metin1 if aramaSayisi != 1 else metin2)


            
        
    #! tekrar tekrar girilmiş sayıyı  silmek için SET yapıyoruz, tekrarlı indeksleri ayıkla
                    
            
                
    silinen_öğrenci_sayısı:int=0           
    
    veriYolu.silindilerListesi.append(veriYolu.FARK_SozlukListesi)
                    
                    
            
#    veriYolu.FARK_SozlukListesi=AsistanModul.TupleyiSözlükListesineEkle(veriYolu.FARK_SozlukListesi)
    p("silme  :   veriYolu.FARK_SozlukListesi >> ",veriYolu.FARK_SozlukListesi)
    AnaModul.SozluktenEksiltme(veriYolu.Jsonda_Mevcut_Veriler,veriYolu.FARK_SozlukListesi)
            
            
            
            
    veriYolu.FARK_SozlukListesi.clear()
            #! BulunanlaR.clear()
    veriYolu.FARK_SozlukListesi.clear()
    veriYolu.Jsonda_Mevcut_Veriler.clear()
            #FIXME - JSON.JSONaKayıt("YEDEK.json",VERİ.yedekSözlüklüListe_)
        
    if silinen_öğrenci_sayısı>0:
                c.print(f"{silinen_öğrenci_sayısı} öğrenci başarıyla silindi. 😄😄 ", style="bold green")
            
    else:
                c.print(f"SİLME>> Hiçbir TALEBE KAYDI silinmedi", style="red")
            
        
#~  3 Silmeye girince bilgilendirme kısmında son eklenen Id numaraları gelsin !!!!!!!!





def    silinmesi_istenilenlerinCTRL(veri): 
        global hatalilar, hatasizlar , aramaSayisi
        hatalilar=[] 
        hatasizlar=[]
        hatalı_var = False    #? bayrak 
        hatalı_var = False
        for istenenlerdenBiri in veri : 
            if istenenlerdenBiri.isdigit():
                if 0 <= int(istenenlerdenBiri) < len(veriYolu.Jsonda_Mevcut_Veriler):
                    pass
                else:
                    hatalilar.append(istenenlerdenBiri)
                    hatalı_var = True
                if int(istenenlerdenBiri) in veriYolu.BulunanIDler:
                    hatasizlar.append(istenenlerdenBiri)
                else:
                    hatalilar.append(istenenlerdenBiri)
            else: #_ isdigit()'in else'si. 
                hatalilar.append(istenenlerdenBiri)
                hatalı_var = True
            if hatalı_var: aramaSayisi += 1; continue    #?  digit değilse veya yanlış sayı girildiyse CONTINUE yapılır.
        p(f"hatalı girişler >> {hatalilar}")
        p(f"hatasizSecimleriniz >> {hatasizlar}")
        