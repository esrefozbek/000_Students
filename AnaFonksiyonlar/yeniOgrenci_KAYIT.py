#FIXME -  çıkışta girlen öğrenciyi/öğrencileri kaydedeyim mi  Evet/Enter    Hayır/Esc seçeneği olsun. 
#FIXME - ilk öğrenci tamamlandığında yeni öğrenci girişi BANNER i yerine "Yeni öğrencinin ADINI giriniz:(Bu aşamada 'Esc' ile kayıttan çıkabilirsin):"  seçeneği tekrar gelsin.
#FIXME - çıkmak için Esc ye bastığında "Devam etmek için ENTER tuşuna bas..."  yerine "Girilen öğrencileri kaydetmek için Enter/e   kayıttan vazgeçmek için Esc/H  seçin"   gelsin

#breakpoint()

import AnaFonksiyonlar.ogrenci_LiSTEleme as Ogr_List
import AnaFonksiyonlar.JSON_jobs as AnaModul
import AsistanFonksiyonlar.klavyeDinleme as klavDinle
import VERI.emptyLists as VERIModul 
from rich.panel import Panel
import  AsistanFonksiyonlar.tupleyi_Sozluklestirme as AsistanModul
from AnaFonksiyonlar.student_class import Ogrenciler
from rich.console import Console ;c=Console()
lastID=0

def yeniOgrenciKayidi():
        toplamKaçKayıtGirildi=0
        if VERIModul.SilinenlerinTupleliListesi_:
                VERIModul.YeniEklenenlerinSozluklerListesi_.clear(); 
                VERIModul.YeniEklenenlerinTupleListesi_.clear();
        while True:
                if toplamKaçKayıtGirildi==0:
                        c.print(Panel.fit("[bold][yellow2]📝 Yeni Öğrenci Girişi [/][/][italic grey30]\n📌 Anamenü'ye [bold orange_red1]Esc[/] ile dönebilirsin.[/]", border_style="green_yellow"), end="")
                else:
                        pass
                              
                #NOTE -  Burada normalde bir ad giriliyor, 'Esc'  ye basılırsa yeni öğrenci kayıdı sonlandırılıyor.
                ad = klavDinle.klavyeDinlemesiÖncesiMesaj(3)  
                

                if ad is None :  #NOTE - None, Esc ye basıldı anlamına geliyor. 
                        c.print(f"\n{toplamKaçKayıtGirildi} öğrenci bilgisi girdiniz...",style="")
                        break
                else:
                        ad=ad.strip()
                # print("\n")       
                c.print("\n\t[green]SOYADI[/] ",end=": "); soyad = input().strip()
                c.print("\t[green]NUMARASI[/] ",end=": ");  öğrenciNumarası = input().strip()
                c.print("\t[green]Doğum Tarihi[/] ",end=": "); dogumTarihi = input().strip()
                c.print("\t[green]SINIFI[/] ",end=": "); sinifi = input().strip()

                        
              
                OgrenciTuple = ad, soyad, öğrenciNumarası,dogumTarihi, sinifi 
                OgrenciNesnesi = Ogrenciler(*OgrenciTuple)   
                TupleClassNesnesi=OgrenciNesnesi.toTuple()
                 
                #c.print("\n[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]♥️ ♥️TupleClassNesnesi görünüşüm: \n",TupleClassNesnesi,style="white")
                #  input("kayıtta yatış 1")
                #c.print("\n[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]⭐⭐ Tupleli listenin Nesne appendi öncesi:",                        Veri_Yolu.TupleliListe_[-1:],end="")
                #  input("kayıtta yatış 2")
                
                #c.print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]👑👑 Tupleli listenin Nesne appendi SONRASI :",Veri_Yolu.TupleliListe_[-2:],end="") 
                #  input("kayıtta yatış 3")
                   
                VERIModul.YeniEklenenlerinTupleListesi_.append(TupleClassNesnesi) 
                toplamKaçKayıtGirildi +=1 
                # c.print(f"{toplamKaçKayıtGirildi}. [grey3]öğrencinin bilgileri geçici hafızaya alındı[/] \n")
                c.print(f"'{len(VERIModul.YeniEklenenlerinTupleListesi_)}' [grey54]öğrencinin bilgileri geçici hafızaya alındı[/]\n",VERIModul.YeniEklenenlerinTupleListesi_,end="")
                #klavDinle.ENTER()
                
                
                  

        VERIModul.yeniEklenenlerTupleListesi_Kopyasi.extend(VERIModul.YeniEklenenlerinTupleListesi_) 
      
        AsistanModul.TupleyiSözlükYap(VERIModul.YeniEklenenlerinTupleListesi_)  #^  
        
        if VERIModul.YeniEklenenlerinSozluklerListesi_:
                #c.print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]💛💛💛 SözlüklüListe başarıyla oluşturuldu Şimdi json'a ekleniyor...",style="")
          
            
                getlastID=AnaModul.JSONaKayıt("VERI/students.json",VERIModul.YeniEklenenlerinSozluklerListesi_ ) ###FIXME - 

                
                
                
               
       
    
       
    
        


          
          
        
    
    
        
        
        
        
        

