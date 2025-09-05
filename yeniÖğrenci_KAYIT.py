import ogrenci_LiSTEleme
import JSON
import klavyeDinleme
import VERİ 
import  tupleyi_Sözlükleştirme
from ÖĞRENCİLER_KLASI import Ogrenciler
from rich.console import Console ;console=Console()

def yeniÖğrenciKayıdı():
        toplamKaçKayıtGirildi=0
        if VERİ.TupleliListe_:
                VERİ.TupleliListe_.clear()   #program ilk açıldığında JSONdanYükleme yapıldığında veri.TupleliListe_ dolu hale geliyor.  Bu da Çift kayıda sebep oluyor. Bu sebeple SIFIRLANMALIdır.
        
        
        while True:
                if toplamKaçKayıtGirildi==0:
                        console.print("\n[bold magenta underline]📝 Yeni Öğrenci Girişi  📝[/bold magenta underline]")
                                
                        console.print(
                        "\n[bold yellow]📕📕🗝️🗝️ TupleliListe_:[/bold yellow]",  VERİ.TupleliListe_[-2:], style="" )

                        
                        console.print("\n[bold yellow]📙📙 🔑🔑 SözlüklüListe_:[/bold yellow]", VERİ.SözlüklüListe_[-2:])
                else:
                        pass
                              
                #NOTE -  Burada normalde bir ad giriliyor, 'Esc'  ye basılırsa yeni öğrenci kayıdı sonlandırılıyor.
                ad = klavyeDinleme.klavyeÖncesiMesaj(3)  
                
                if ad is None :  #NOTE - None, Esc ye basıldı anlamına geliyor. 
                        console.print(f"📤[bold red] Kullanıcı [bold yellow]ESC[/bold yellow]'ye bastı. Giriş iptal edildi.[/bold red]\n [bold white]{toplamKaçKayıtGirildi}[/bold white] [bold magenta]kayıt girdiniz, Tebrik eder, hayatında başarılar dilerim[/bold magenta]")
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
                console.print("\n[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]♥️ ♥️TupleClassNesnesi görünüşüm: \n",TupleClassNesnesi,style="white")
                          
                #NOTE - tupleye çevrilen klas nesnesi tupleli listeye kaydediliyor ???????
                #NOTE - yeni öğrenci nesne tuplesi,  boş  VERİ.TupleliListe_ sine kaydediliyor. TupleliListe_ bu aşamada dolmaya başlıyor. 
                console.print("\n[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]⭐⭐ Tupleli listenin Nesne appendi öncesi:",VERİ.TupleliListe_[-1:],end="")
                VERİ.TupleliListe_.append(TupleClassNesnesi) 
                console.print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]👑👑 Tupleli listenin Nesne appendi SONRASI :",VERİ.TupleliListe_[-2:],end="")
                
                   
                VERİ.yeniEklenenlerListesi_.append(TupleClassNesnesi)  
                
                  

                
         #NOTE - Esc ile çıktık ve elimizdeki VERİ.TupleliListe_ yi  sözlük yaparak JSON'a kaydedeceğiz.
        tupleyi_Sözlükleştirme.TupleyiSözlükYap(liste=VERİ.TupleliListe_)
        VERİ.TupleliListe_.clear()
        
        
        
        if VERİ.SözlüklüListe_:
                console.print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow]💛💛💛 SözlüklüListe başarıyla oluşturuldu Şimdi json'a gömüyorum...",style="")
          
                klavyeDinleme.ENTER()  
                toplamKaçKayıtGirildi += len(VERİ.SözlüklüListe_)
                                  
                JSON.JSONaKayıt("öğrenciler.json",VERİ.SözlüklüListe_ );
                VERİ.SözlüklüListe_.clear(); 
                    
                #FIXME - JSON.JSONaKayıt("YEDEK.json",VERİ.yedekSözlüklüListe_);                 VERİ.yedekSözlüklüListe_.clear()   
        
        # else:
        #         print("[bold yellow]yeniÖğrenciKayıdı():[/bold yellow] SözlüklüListe boş")
          
    
       
    
        


          
          
        
    
    
        
        
        
        
        

