#FIXME -  çıkışta girlen öğrenciyi/öğrencileri kaydedeyim mi  Evet/Enter    Hayır/Esc seçeneği olsun. 
#FIXME - ilk öğrenci tamamlandığında yeni öğrenci girişi BANNER i yerine "Yeni öğrencinin ADINI giriniz:(Bu aşamada 'Esc' ile kayıttan çıkabilirsin):"  seçeneği tekrar gelsin.
#FIXME - çıkmak için Esc ye bastığında "Devam etmek için ENTER tuşuna bas..."  yerine "Girilen öğrencileri kaydetmek için Enter/e   kayıttan vazgeçmek için Esc/H  seçin"   gelsin

#breakpoint()

import AnaFonksiyonlar.ogrenci_LiSTEleme as Ogr_List
import AnaFonksiyonlar.JSON as Json
import AsistanFonksiyonlar.klavyeDinleme as klavDinle
import VERI.veri as Veri_Yolu 
from rich.panel import Panel
import  AsistanFonksiyonlar.tupleyi_Sozluklestirme as Tup_Soz
from AnaFonksiyonlar.student_class import Ogrenciler
from rich.console import Console ;c=Console()

def yeniOgrenciKayidi():
        toplamKaçKayıtGirildi=0
        if Veri_Yolu.TupleliListe_:
                Veri_Yolu.SozlukluListe_.clear(); 
                Veri_Yolu.yeniEklenenlerListesi_Tuple.clear();
                #program ilk açıldığında JSONdanYükleme yapıldığında veri.TupleliListe_ dolu hale geliyor.  Bu da Çift kayıda sebep oluyor. Bu sebeple SIFIRLANMALIdır. Bre gafil, sıfırlama yapacaksan neden çağırıyorsun, çağırma boş bir liste üret ve onla  devame et.
        
        
        while True:
                if toplamKaçKayıtGirildi==0:
                        c.print(Panel.fit("[bold][yellow2]📝 Yeni Öğrenci Girişi [/][/][italic grey7] 📌 Anamenü'ye dönmek için [bold orange_red1]Esc[/] tuşuna bas.[/]", border_style="green_yellow"), end="")
                else:
                        pass
                              
                #NOTE -  Burada normalde bir ad giriliyor, 'Esc'  ye basılırsa yeni öğrenci kayıdı sonlandırılıyor.
                ad = klavDinle.klavyeDinlemesiÖncesiMesaj(3)  
                
                if ad is None :  #NOTE - None, Esc ye basıldı anlamına geliyor. 
                        c.print(f"📤[bold red] Kullanıcı [bold yellow]ESC[/bold yellow]'ye bastı. Giriş iptal edildi.[/bold red]\n [bold white]{toplamKaçKayıtGirildi}[/bold white] [bold magenta]kayıt girdiniz, Tebrik eder, hayatında başarılar dilerim[/bold magenta]")
                        break
                else:
                        ad=ad.strip()
                # print("\n")       
                c.print("\n\t[green3]SOYADINI[/] giriniz ",end=">> "); soyad = input().strip()
                c.print("\t[green3]NUMARASINI[/] giriniz ",end=">> ");  öğrenciNumarası = input().strip()
                c.print("\t[green3]Doğum Tarihini[/] giriniz ",end=">> "); dogumTarihi = input().strip()
                c.print("\t[green3]SINIFINI[/] giriniz ",end=">> "); sinifi = input().strip()

              
                OgrenciTuple = ad, soyad, öğrenciNumarası,dogumTarihi, sinifi 
                OgrenciNesnesi = Ogrenciler(*OgrenciTuple)   
                TupleClassNesnesi=OgrenciNesnesi.toTuple()
                
                """   
                c.print("\n[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]♥️ ♥️TupleClassNesnesi görünüşüm: \n",TupleClassNesnesi,style="white")
                c.print("\n[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]⭐⭐ Tupleli listenin Nesne appendi öncesi:",
                        Veri_Yolu.TupleliListe_[-1:],end="")
                
                c.print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]👑👑 Tupleli listenin Nesne appendi SONRASI :",Veri_Yolu.TupleliListe_[-2:],end="") 
                 """
                   
                Veri_Yolu.yeniEklenenlerListesi_Tuple.append(TupleClassNesnesi) 
                toplamKaçKayıtGirildi +=1 
                c.print(f"  {toplamKaçKayıtGirildi}. [grey3]öğrencinin bilgileri geçici hafızaya alındı[/] \n")
                
                  

        Veri_Yolu.yeniEklenenlerListesi_Tuple_Kopya=Veri_Yolu.yeniEklenenlerListesi_Tuple.copy() 
                
         #NOTE - Esc ile çıktık ve elimizdeki VERİ.TupleliListe_ yi  sözlük yaparak JSON'a kaydedeceğiz.
        Tup_Soz.TupleyiSözlükYap(yeniEklenenlerListesi_=Veri_Yolu.yeniEklenenlerListesi_Tuple)  #^  tupleyi_Sözlükleştirme.py ye gidiyor ve returnla geri geliyoruz

                #^^   Veri.TupleliListe_.clear()
        
        
        #^toplamKaçKayıtGirildi += len(Veri.SozlukluListe_)
        
        if Veri_Yolu.SozlukluListe_:
                c.print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]💛💛💛 SözlüklüListe başarıyla oluşturuldu Şimdi json'a gömüyorum...",style="")
          
              #^  klavDinle.ENTER()  
              #^  c.print("yeni öğrenci kayıttaki verisözlüklü liste: \n",Veri_Yolu.SozlukluListe_)   
              #^  input("burada bir duralım")              
              #^  klavDinle.ENTER()  
              #^  Json.JSONaKayıt("VERI/students.json",Veri_Yolu.SozlukluListe_ );
               
       
    
       
    
        


          
          
        
    
    
        
        
        
        
        

