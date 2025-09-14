#FIXME -  çıkışta girlen öğrenciyi/öğrencileri kaydedeyim mi  Evet/Enter    Hayır/Esc seçeneği olsun. 
#FIXME - ilk öğrenci tamamlandığında yeni öğrenci girişi BANNER i yerine "Yeni öğrencinin ADINI giriniz:(Bu aşamada 'Esc' ile kayıttan çıkabilirsin):"  seçeneği tekrar gelsin.
#FIXME - çıkmak için Esc ye bastığında "Devam etmek için ENTER tuşuna bas..."  yerine "Girilen öğrencileri kaydetmek için Enter/e   kayıttan vazgeçmek için Esc/H  seçin"   gelsin

#breakpoint()

import AnaFonksiyonlar.ogrenci_LiSTEleme as Ogr_List
import AnaFonksiyonlar.JSON_jobs as Json
import AsistanFonksiyonlar.klavyeDinleme as klavDinle
import VERI.emptyLists as Veri_Yolu 
from rich.panel import Panel
import  AsistanFonksiyonlar.tupleyi_Sozluklestirme as Tup_Soz
from AnaFonksiyonlar.student_class import Ogrenciler
from rich.console import Console ;c=Console()
lastID=0

def yeniOgrenciKayidi():
        toplamKaçKayıtGirildi=0
        if Veri_Yolu.TupleliListe_:
                Veri_Yolu.SozluklerListesi_.clear(); 
                Veri_Yolu.YeniEklenenlerinTupleListesi_.clear();
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
                   
                Veri_Yolu.YeniEklenenlerinTupleListesi_.append(TupleClassNesnesi) 
                toplamKaçKayıtGirildi +=1 
                # c.print(f"{toplamKaçKayıtGirildi}. [grey3]öğrencinin bilgileri geçici hafızaya alındı[/] \n")
                c.print(f"'{len(Veri_Yolu.YeniEklenenlerinTupleListesi_)}' [grey54]öğrencinin bilgileri geçici hafızaya alındı[/]\n",Veri_Yolu.YeniEklenenlerinTupleListesi_,end="")
                #klavDinle.ENTER()
                
                
                  

        Veri_Yolu.yeniEklenenlerTupleListesi_Kopyasi.extend(Veri_Yolu.YeniEklenenlerinTupleListesi_) 
      
        Tup_Soz.TupleyiSözlükYap(Veri_Yolu.YeniEklenenlerinTupleListesi_)  #^  
        
        if Veri_Yolu.SozluklerListesi_:
                #c.print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]💛💛💛 SözlüklüListe başarıyla oluşturuldu Şimdi json'a ekleniyor...",style="")
          
            
                getlastID=Json.JSONaKayıt("VERI/students.json",Veri_Yolu.SozluklerListesi_ ) ###FIXME - 

                
                
                
               
       
    
       
    
        


          
          
        
    
    
        
        
        
        
        

