 #FIXME - mesela 16 yı silmek için 16 yazdım  Sonra 16yı değilde 17 yazmak için backspace ile geri gitmeye kalktım   Geri gitmedi, Esc'ye bastım.     BOOOOMMMMMMM     Normal çıkış için basılan ESc bile patladı !!!!!!
 
 #FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.   Bu tüm listeyi görmek için bir vantaj mı yoksa hata mı
 #FIXME -  Silmeden çıkmak için Esc ye bas,  Devam etmek için Enter  çıkmak için tekrar Esc ye bas seçeneği iyi olur.  
 #FIXME -  bu sayfadaki kodlar Revize edilmeli. 
 #FIXME - "İndeksler:"   kısmı "İndeksler or Esc"   olarak değiştirilmeli.  
 
 
 
import AnaFonksiyonlar.ogrenci_LiSTEleme as Ogr_List
import AsistanFonksiyonlar.arama as Arama
import AsistanFonksiyonlar.klavyeDinleme as klavDinle
from rich.console import Console; k = Console()
import re
import AsistanFonksiyonlar.onayE_H as OnayE_H
import AnaFonksiyonlar.JSON_jobs as Json
import VERI.emptyLists as Veri_Yolu 
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as Tup_Soz


def ogrenciSil():
    aranan_ogrenci = klavDinle.klavyeDinlemesiÖncesiMesaj(2)  #klavyeden değer alınıyor   
    Arama.arama(aranan_ogrenci)     # Öğrenci sorgulama
    bulunanlarListesi_ = Arama.AramadaBulunanlarListesi_   #Kısaltma yaptım

    if not bulunanlarListesi_:
        k.print("[bold red]Hiçbir öğrenci bulunamadı.[/bold red]")
        return

    tekrar_sayacı=1
    
    metin1=f"""
    [bold yellow] Silinecek öğrencilerin numaralarını girin. Sayıları boşluk veya virgül ile ayırabilirsiniz.          [/bold yellow]        
    [bold magenta]Geçerli aralık:[/bold magenta] 0 - {len(bulunanlarListesi_) - 1} 
    """  
    metin2=f""" 
            [bold white on blue]
                Silinecek öğrencilerin numaralarını girin.
                Sayıları boşluk veya virgül ile ayırabilirsiniz.

            [italic yellow]
                Lütfen bu sefer dikkatli ol, Tanrı aşkına![/italic yellow] 🙏
                Geçerli aralık:[bold yellow] 0 - {len(bulunanlarListesi_) - 1}
            [/bold yellow]

            [/bold white on blue]
    """
   
   
    while True:
        if tekrar_sayacı==1 :
            k.print(metin1)
        else:
            k.print(metin2)

        girdi = input("İndeksler: ")
        girdi=girdi.strip()
        if not girdi:
            k.print("Boş giriş yapıldı. Tekrar deneyin.", style="red")
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
                    k.print(f"Hatalı indeks: {girdi}", style="bold red")
                    hatalı_var = True
            else:
                k.print(f"Geçersiz giriş: {girdi}", style="bold red")
                hatalı_var = True
           

        if hatalı_var:
            tekrar_sayacı+=1;
            continue

        # Aynı öğrenciyi 2 kez silme, tekrarlı indeksleri ayıkla
        geçerli_girdiler_Listesi = list(set(geçerli_girdiler_Listesi))
        silinecekler = [bulunanlarListesi_[i] for i in geçerli_girdiler_Listesi]
            
        silinen_öğrenci_sayısı:int=0           
        for ogr in silinecekler:
            k.print(f"Öğrenci kayıdı siliniyor!!!: {ogr}", style="bold blue")
            if OnayE_H.Evet_Hayır_OnayiAl(ogr):
                silinen_öğrenci_sayısı+=1
                Veri_Yolu.silinmislerListesi_.append(ogr)
                Veri_Yolu.TupleliListe_.remove(ogr)
            else:
                print("Kayıt işlemini iptal ettin")
        if silinen_öğrenci_sayısı:
            k.print(f"{silinen_öğrenci_sayısı} öğrenci başarıyla silindi. 😄😄 ", style="bold green")
            break
        else:
            k.print(f"Hiçbir TALEBE KAYDI silinmedi", style="red")
            break

    # Temizlik
    bulunanlarListesi_.clear()
    Tup_Soz.TupleyiSözlükYap(Veri_Yolu.TupleliListe_)
    Json.JSONaKayıt("VERI/students.json",Veri_Yolu.SozluklerListesi_)
    #FIXME - JSON.JSONaKayıt("YEDEK.json",VERİ.yedekSözlüklüListe_)
    Veri_Yolu.TupleliListe_.clear()
    Veri_Yolu.SozluklerListesi_.clear()
    
    

