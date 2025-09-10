import ogrenci_LiSTEleme
import JSON
import klavyeDinleme
import veri 
from rich.panel import Panel
import  tupleyi_Sozluklestirme
from student_class import Ogrenciler
from rich.console import Console ;c=Console()

def yeniOgrenciKayidi():
        toplamKaçKayıtGirildi=0
        if veri.TupleliListe_:
                veri.TupleliListe_.clear()   #program ilk açıldığında JSONdanYükleme yapıldığında veri.TupleliListe_ dolu hale geliyor.  Bu da Çift kayıda sebep oluyor. Bu sebeple SIFIRLANMALIdır.
        
        
        while True:
                if toplamKaçKayıtGirildi==0:
                        c.print(Panel.fit(
        "[yellow2]📝 Yeni Öğrenci Girişi [/][italic grey27] 📌 Anamenü'ye dönmek için [bold orange_red1]Esc[/] tuşuna bas.[/]",
        border_style="green_yellow"  # ← dış çerçevenin rengi burada
    ),
    end=""
)
                                
                  #      console.print(                        "\n[bold yellow]📕📕🗝️🗝️ TupleliListe_:[/bold yellow]",  veri.TupleliListe_[-2:], style="" )

                        
          #              console.print("\n[bold yellow]📙📙 🔑🔑 SözlüklüListe_:[/bold yellow]", veri.SozlukluListe_[-2:])
                else:
                        pass
                              
                #NOTE -  Burada normalde bir ad giriliyor, 'Esc'  ye basılırsa yeni öğrenci kayıdı sonlandırılıyor.
                ad = klavyeDinleme.klavyeDinlemesiÖncesiMesaj(3)  
                
                if ad is None :  #NOTE - None, Esc ye basıldı anlamına geliyor. 
                        c.print(f"📤[bold red] Kullanıcı [bold yellow]ESC[/bold yellow]'ye bastı. Giriş iptal edildi.[/bold red]\n [bold white]{toplamKaçKayıtGirildi}[/bold white] [bold magenta]kayıt girdiniz, Tebrik eder, hayatında başarılar dilerim[/bold magenta]")
                        break
                else:
                        ad=ad.strip()
                soyad = input("\n🧑‍🎓 Öğrencinin soyadını giriniz:").strip()
                öğrenciNumarası = input("🔢 Öğrenci numarasını giriniz:").strip()
                dogumTarihi = input("📆📆 Doğum tarihini giriniz:").strip()
                sinifi = input("🏛️🏛️ Sınıfını giriniz:").strip()
                 
                
                #NOTE - Burada 4 değikeni bir değişken olarak kaydediyoruz, 4 ardışık kayıt Tuple olarak kaydedilir, parantez olmasa bile. 
                ogrenciTuple = ad, soyad, öğrenciNumarası,dogumTarihi, sinifi 
                #NOTE - Burada bu tupleyi klasa gönderip klas nesnesi yapıyoruz.  def __init__(self,  ad, soyad, dogTarihi,sinifi):
                OgrenciNesnesi = Ogrenciler(*ogrenciTuple)   
                
                #NOTE - öğrenci nesnesi tipinde geri dönen ve 4ten 6ya çıkmış elemanlı nesneyi tekrar tuple tipine çeviriyoruz. Klasta, Tupleye Id ve Kayıt Tarihi bilgileri ekleniyor.
                TupleClassNesnesi=OgrenciNesnesi.toTuple()
              #^  console.print("\n[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]♥️ ♥️TupleClassNesnesi görünüşüm: \n",TupleClassNesnesi,style="white")
                          
                #NOTE - tupleye çevrilen klas nesnesi tupleli listeye kaydediliyor ???????
                #NOTE - yeni öğrenci nesne tuplesi,  boş  VERİ.TupleliListe_ sine kaydediliyor. TupleliListe_ bu aşamada dolmaya başlıyor. 
               #^ console.print("\n[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]⭐⭐ Tupleli listenin Nesne appendi öncesi:",veri.TupleliListe_[-1:],end="")
                veri.TupleliListe_.append(TupleClassNesnesi) 
                c.print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]👑👑 Tupleli listenin Nesne appendi SONRASI :",veri.TupleliListe_[-2:],end="")
                
                   
                veri.yeniEklenenlerListesi_.append(TupleClassNesnesi)  
                
                  

                
         #NOTE - Esc ile çıktık ve elimizdeki VERİ.TupleliListe_ yi  sözlük yaparak JSON'a kaydedeceğiz.
        tupleyi_Sozluklestirme.TupleyiSözlükYap(liste=veri.TupleliListe_)
        veri.TupleliListe_.clear()
        
        
        
        if veri.SozlukluListe_:
                c.print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]💛💛💛 SözlüklüListe başarıyla oluşturuldu Şimdi json'a gömüyorum...",style="")
          
                klavyeDinleme.ENTER()  
                toplamKaçKayıtGirildi += len(veri.SozlukluListe_)
                                  
                JSON.JSONaKayıt("students.json",veri.SozlukluListe_ );
                veri.SozlukluListe_.clear(); 
                    
                #FIXME - JSON.JSONaKayıt("YEDEK.json",VERİ.yedekSözlüklüListe_);                 VERİ.yedekSözlüklüListe_.clear()   
        
        # else:
        #         print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow] SözlüklüListe boş")
          
    
       
    
        


          
          
        
    
    
        
        
        
        
        

