 #FIXME - mesela 16 yı silmek için 16 yazdım  Sonra 16yı değilde 17 yazmak için backspace ile geri gitmeye kalktım   Geri gitmedi, Esc'ye bastım.     BOOOOMMMMMMM     Normal çıkış için basılan ESc bile patladı !!!!!!
 
 #FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.   Bu tüm listeyi görmek için bir vantaj mı yoksa hata mı
 #FIXME -  Silmeden çıkmak için Esc ye bas,  Devam etmek için Enter  çıkmak için tekrar Esc ye bas seçeneği iyi olur.  
 #FIXME -  bu sayfadaki kodlar Revize edilmeli. 
 #FIXME - "İndeksler:"   kısmı "İndeksler or Esc"   olarak değiştirilmeli.  
 #NOTE -  Silinmediği halde jsona geri kayıt yapıldı. ????????
 
 
 
import AnaFonksiyonlar.ogrenci_LiSTEleme as Ogr_List
import AsistanFonksiyonlar.arama as Arama
import AsistanFonksiyonlar.klavyeDinleme as klavDinle
from rich.console import Console; c = Console()
import re
import AsistanFonksiyonlar.onayE_H as OnayE_H
import AnaFonksiyonlar.JSON_jobs as AnaModul

import VERI.emptyLists as VERIModul 
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as AsistanModul


def ogrenciSil():
    global metin1,metin2,bulunanlarListesi_
    VERIModul.YeniEklenenlerinSozluklerListesi_.clear()
    VERIModul.SilinenlerinTupleliListesi_.clear()
    VERIModul.silinmislerListesi_.clear()
    tekrar_sayacı=1
                                   
    
    aranan_ogrenci = klavDinle.klavyeDinlemesiÖncesiMesaj(2)  #klavyeden değer alınıyor   
    AnaModul.JSONdanYükleme_()   
    Arama.arama(aranan_ogrenci)     # Öğrenci sorgulama
    bulunanlarListesi_ = Arama.AramadaBulunanlarListesi_   #Kısaltma yaptım

    if not bulunanlarListesi_:
        c.print("[bold red]Aranan kritere uygun öğrenci bulunamadı.[/bold red]")
        return

    metin1=f"""
    [bold yellow]Silinecek öğrencilerin numaralarını girin. Sayıları boşluk veya virgül ile ayırabilirsiniz.          [/]        
    [bold magenta]Geçerli aralık:[/] 0 - {len(bulunanlarListesi_) - 1} 
    """  
    metin2=f""" 
            [bold white]
                Silinecek öğrencilerin numaralarını girin.
                Sayıları boşluk veya virgül ile ayırabilirsiniz.
            [italic yellow]
                Lütfen bu sefer dikkatli ol, Tanrı aşkına![/italic yellow] 🙏
                Geçerli aralık:[bold yellow] 0 - {len(bulunanlarListesi_) - 1}
            [/bold yellow]
            [/bold white]
    """
    
   
    while True:
         
        if tekrar_sayacı==1 :
            c.print(metin1)
        else:
            c.print(metin2)
        
        c.print("Silinmesini istediğiniz SIRA NUMARALARI || [bold red]Esc[/bold red] >>")
        girdi = klavDinle.klavyeGirisi()
        if girdi==None:
            c.print("Esc ile çıkılıyor...... ")
            break
        else:
            girdi=girdi.strip()
        if not girdi:
            c.print("Boş giriş yapıldı. Tekrar deneyin.", style="red")
            continue
        

        girilen_indeksler = re.split(r'[,\s]+', girdi)
        geçerli_girdiler_Listesi = []   # düzgün girilmiş indeks numaralarıdır.
        hatalı_var = False

        for girdi in girilen_indeksler:
            if girdi.isdigit():
                girdi = int(girdi)  # başlangıçta Stringdir .
                if 0 <= girdi < len(bulunanlarListesi_):
                    geçerli_girdiler_Listesi.append(girdi)
                else:
                    c.print(f"Hatalı indeks: {girdi}", style="bold red")
                    hatalı_var = True
            else:
                c.print(f"Geçersiz giriş: {girdi}", style="bold red")
                hatalı_var = True
           

        if hatalı_var:
            tekrar_sayacı+=1;
            continue

        # Aynı öğrenciyi 2 kez silme, tekrarlı indeksleri ayıkla
        geçerli_girdiler_Listesi = list(set(geçerli_girdiler_Listesi))
        silinecekler = [bulunanlarListesi_[i] for i in geçerli_girdiler_Listesi]
            
        silinen_öğrenci_sayısı:int=0           
        for ogr in silinecekler:
            c.print(f"Öğrenci kayıdı siliniyor!!!: {ogr}", style="bold blue")
            if OnayE_H.Evet_Hayır_OnayiAl(ogr):
                silinen_öğrenci_sayısı+=1
                VERIModul.silinmislerListesi_.append(ogr)
                VERIModul.SilinenlerinTupleliListesi_.remove(ogr)
            else:
                print("Kayıt işlemini iptal ettin")
        if silinen_öğrenci_sayısı:
            c.print(f"{silinen_öğrenci_sayısı} öğrenci başarıyla silindi. 😄😄 ", style="bold green")
            break
        else:
            c.print(f"Hiçbir TALEBE KAYDI silinmedi", style="red")
            break

    # Temizlik
    if girdi==None:
        return
    else:
        bulunanlarListesi_.clear()
        VERIModul.SilinenlerinSozluklerListesi_=AsistanModul.TupleyiSözlükYap(VERIModul.SilinenlerinTupleliListesi_)
        VERIModul.SilinenlerinTupleliListesi_.clear()
        AnaModul.JSONdanKayitSilme("VERI/students.json", VERIModul.SilinenlerinSozluklerListesi_)
        VERIModul.YeniEklenenlerinSozluklerListesi_.clear()
    #FIXME - JSON.JSONaKayıt("YEDEK.json",VERİ.yedekSözlüklüListe_)
    
    
    
    
    
   


   