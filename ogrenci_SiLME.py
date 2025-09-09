import ogrenci_LiSTEleme
import arama
import klavyeDinleme
from rich.console import Console;console = Console()
import re
import onayE_H
import JSON
import veri 
import tupleyi_Sozluklestirme


def ogrenciSil():
    aranan_ogrenci = klavyeDinleme.klavyeÖncesiMesaj(2)  #klavyeden değer alınıyor   
    arama.arama(aranan_ogrenci)     # Öğrenci sorgulama
    bulunanlarListesi_ = arama.AramadaBulunanlarListesi_   #Kısaltma yaptım

    if not bulunanlarListesi_:
        console.print("[bold red]Hiçbir öğrenci bulunamadı.[/bold red]")
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
            console.print(metin1)
        else:
            console.print(metin2)

        girdi = input("İndeksler: ")
        girdi=girdi.strip()
        if not girdi:
            console.print("Boş giriş yapıldı. Tekrar deneyin.", style="red")
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
                    console.print(f"Hatalı indeks: {girdi}", style="bold red")
                    hatalı_var = True
            else:
                console.print(f"Geçersiz giriş: {girdi}", style="bold red")
                hatalı_var = True
           

        if hatalı_var:
            tekrar_sayacı+=1;
            continue

        # Aynı öğrenciyi 2 kez silme, tekrarlı indeksleri ayıkla
        geçerli_girdiler_Listesi = list(set(geçerli_girdiler_Listesi))
        silinecekler = [bulunanlarListesi_[i] for i in geçerli_girdiler_Listesi]
            
        silinen_öğrenci_sayısı:int=0           
        for ogr in silinecekler:
            console.print(f"Öğrenci kayıdı siliniyor!!!: {ogr}", style="bold blue")
            if onayE_H.Evet_Hayır_OnayiAl(ogr):
                silinen_öğrenci_sayısı+=1
                veri.silinmislerListesi_.append(ogr)
                veri.TupleliListe_.remove(ogr)
            else:
                print("Kayıt işlemini iptal ettin")
        if silinen_öğrenci_sayısı:
            console.print(f"{silinen_öğrenci_sayısı} öğrenci başarıyla silindi. 😄😄 ", style="bold green")
            break
        else:
            console.print(f"Hiçbir TALEBE KAYDI silinmedi", style="red")
            break

    # Temizlik
    bulunanlarListesi_.clear()
    tupleyi_Sozluklestirme.TupleyiSözlükYap(liste=veri.TupleliListe_)
    JSON.JSONaKayıt("öğrenciler.json",veri.SozlukluListe_)
    #FIXME - JSON.JSONaKayıt("YEDEK.json",VERİ.yedekSözlüklüListe_)
    veri.TupleliListe_.clear()
    veri.SozlukluListe_.clear()
    
    
 

