
 
 #FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.   Bu tüm listeyi görmek için bir vantaj mı yoksa hata mı
 #FIXME -  Silmeden çıkmak için Esc ye bas,  Devam etmek için Enter  çıkmak için tekrar Esc ye bas seçeneği iyi olur.  
 #FIXME -  bu sayfadaki kodlar Revize edilmeli. 
 #FIXME - "İndeksler:"   kısmı "İndeksler or Esc"   olarak değiştirilmeli.  

 
 
 

import re
import AsistanFonksiyonlar.arama as Arama
import AsistanFonksiyonlar.klavyeDinleme as klavyeyiDinle
from rich.console import Console; c = Console()
import AsistanFonksiyonlar.onayE_H as OnayE_H
import AnaFonksiyonlar.JSON_jobs as AnaModul

import VERI.emptyLists as EmptyLists 
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as AsistanModul
# import questionary


def ogrenciSil():
    global metin1,metin2
    EmptyLists.FARK_SozlukListesi.clear()
    EmptyLists.Jsonda_Mevcut_Veriler.clear()
    EmptyLists.silindilerListesi.clear()
    hatasizSecimleriniz = []   # düzgün girilmiş indeks numaralarıdır.
    aramaSayisi=1
    Arama.bul(1)
    
    EmptyLists.Bulunanlar=[] if EmptyLists.Bulunanlar is None else EmptyLists.Bulunanlar
   
   
   
   
    metin1=f"""[yellow]Silinecek öğrencilerin numaralarını girin. Sayıları boşluk veya virgül ile ayırabilirsiniz.[/]        
    [bold magenta]Geçerli aralık:[/] 0 - {len(EmptyLists.Bulunanlar) - 1} 
    """  
    metin2=f""" [bold white][italic yellow] Lütfen bu sefer dikkatli ol, Tanrı aşkına![/italic yellow] 🙏  Geçerli aralık:[bold yellow] 0 - {len(EmptyLists.Bulunanlar) - 1} [/] [/] """

   
    while True:   #!!!!   Ne döngüsü bu ??
         
        c.print(metin1 if aramaSayisi == 1 else metin2)

           
        
        c.print("Silinmesini istediğiniz SIRA NUMARALARI || [bold red]Esc[/] >>")
        silinmesi_istenilenler =Arama.InputwithESCAPE (0)
        silinmesi_istenilenler=silinmesi_istenilenler or ""
        

        silinmesi_istenilenler = re.split(r'[,\s]+', silinmesi_istenilenler) #! Klavyeden girilenler temizlenip liste yapıldı. Boşluklar veya virgüller atıldı.   
        hatalı_var = False    #? bayrak 

#NOTE aşağdaki for ile klavyeyle girilen sayıların Bulunanlar listesinde mevcudiyeti, sayı mı değil mi   inceleniyor. String sayı, int sayı yapılıyor.     
        for istenenlerdenBiri in silinmesi_istenilenler:  
            if istenenlerdenBiri.isdigit():
                istenenlerdenBiri = int(istenenlerdenBiri)  # başlangıçta Stringdir .
                if 0 <= istenenlerdenBiri < len(EmptyLists.Bulunanlar):
                    hatasizSecimleriniz.append(istenenlerdenBiri)
                else:
                    c.print(f"Hatalı indeks: {istenenlerdenBiri}", style="bold red")
                    hatalı_var = True
            else: #! isdigit()'in else'si. 
                c.print(f"Geçersiz giriş: {istenenlerdenBiri}", style="bold red")
                hatalı_var = True
           
        c.print("geçerli_girdiler_Listesi >>",hatasizSecimleriniz)
        
        if hatalı_var: aramaSayisi += 1; continue    #?  digit değilse veya yanlış sayı girildiyse CONTINUE yapılır.


        #! Aynı öğrenciyi 2 kez silmek için SET yapıyoruz, tekrarlı indeksleri ayıkla
        hatasizSecimleriniz = list(set(hatasizSecimleriniz))
        EmptyLists.FARK_TupleListesi = [EmptyLists.Bulunanlar[i] for i in hatasizSecimleriniz]
                
        
        c.print("SİLME:: hatasizSecimleriniz >>",hatasizSecimleriniz)
        c.print("SİLME:: silinecek_ogrenciler 1>>",EmptyLists.FARK_TupleListesi)
            
        silinen_öğrenci_sayısı:int=0           
  
        EmptyLists.silindilerListesi.append(EmptyLists.FARK_TupleListesi)
                
                
        
        EmptyLists.FARK_SozlukListesi=AsistanModul.TupleyiSözlükListesineEkle(EmptyLists.FARK_TupleListesi)
        AnaModul.SozluktenEksiltme(EmptyLists.Jsonda_Mevcut_Veriler,EmptyLists.FARK_SozlukListesi)
        
        
        
        
        EmptyLists.FARK_SozlukListesi.clear()
        #! BulunanlaR.clear()
        EmptyLists.FARK_SozlukListesi.clear()
        EmptyLists.Jsonda_Mevcut_Veriler.clear()
        #FIXME - JSON.JSONaKayıt("YEDEK.json",VERİ.yedekSözlüklüListe_)
    
        if silinen_öğrenci_sayısı>0:
            c.print(f"{silinen_öğrenci_sayısı} öğrenci başarıyla silindi. 😄😄 ", style="bold green")
        
        else:
            c.print(f"SİLME>> Hiçbir TALEBE KAYDI silinmedi", style="red")
        
    

