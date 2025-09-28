#FIXME -  çıkışta girlen öğrenciyi/öğrencileri kaydedeyim mi  Evet/Enter    Hayır/Esc seçeneği olsun. 
#FIXME - ilk öğrenci tamamlandığında yeni öğrenci girişi BANNER i yerine "Yeni öğrencinin ADINI giriniz:(Bu aşamada 'Esc' ile kayıttan çıkabilirsin):"  seçeneği tekrar gelsin.
#FIXME - çıkmak için Esc ye bastığında "Devam etmek için ENTER tuşuna bas..."  yerine "Girilen öğrencileri kaydetmek için Enter/e   kayıttan vazgeçmek için Esc/H  seçin"   gelsin

#breakpoint()
import Widgetler.SayacAnimasyon.spinner as SpinnerPY 
import AnaFonksiyonlar.JSON_jobs as ANAMODUL
import AsistanFonksiyonlar.klavyeDinleme as KLAVYEDINLE
import VERI.emptyLists as EMPTY_LISTS 
from AnaFonksiyonlar.student_class import Ogrenciler
from rich.console import Console ;c=Console()
from rich.prompt import Prompt
from rich.panel import Panel
from rich.columns import Columns
import VERI.mesajlar as MESAJLAR


lastID=0
toplamKayit=0

def yeniOgrenciKayidi():
        EMPTY_LISTS.FARK_SozlukListesi.clear();
        EMPTY_LISTS.FARK_SozlukListesi.clear(); 
        while True:            
                ogrenci=inputOgr() 
                if ogrenci is None: break
                nesne=klasSureci(ogrenci)
                FarkSozlukListesineAppend(nesne) 
        FarkiJsonSozlugeEkle()
        
def inputOgr():
        
        while True:
                MESAJLAR.Mesajlar(8)
                ad = KLAVYEDINLE.KlavyeDinle()
                if ad is None :  #NOTE - None, Esc ye basıldı anlamına geliyor. 
                        c.print(f"\n{toplamKayit} öğrenci bilgisi sağladınız...\n",style="",end="\n")
                        SpinnerPY.spinner(4,4) if toplamKayit>0  else SpinnerPY.spinner(3,6) 
                        c.print("kayıt::inputOgr: toplamKayit ->>",toplamKayit)
                        return None
                else:
                        ad=ad.strip()
                
                # print("\n")       
                c.print("\n\t[dark_slate_gray1]SOYADI[/] ",end="       ➡️ "); soyad = input().strip()
                c.print("\t[dark_slate_gray1]NUMARASI[/] ",end="     ➡️ ");  ogrenciNumarasi = input().strip()
                c.print("\t[dark_slate_gray1]Doğum Tarihi[/] [grey23][01/01/2000][/]",end=" ➡️ ");dogumTarihi =input().strip()
                c.print("\t[dark_slate_gray1]SINIFI[/] ",end="       ➡️ "); sinifi = input().strip()
        
                ogrenci=(ad, soyad, ogrenciNumarasi, dogumTarihi, sinifi)
                c.print("kayıt::inputOgr: toplamKayit -->>",toplamKayit)
                return ogrenci 

def klasSureci(ogrenci):
              
              #  OgrenciTuple = ogrenci  
                OgrenciNesnesi = Ogrenciler(*ogrenci)   
                nesne=OgrenciNesnesi.toDict()
                return nesne
           
   

def FarkSozlukListesineAppend(nesne):  
       
        EMPTY_LISTS.FARK_SozlukListesi.append(nesne) #! append to Tuple
                
        c.print(f"{toplamKayit}, [white]öğrencinin bilgileri geçici hafızaya alındı[/] \n")
        c.print(f"KAYIT:: '{len(EMPTY_LISTS.FARK_SozlukListesi)}' [bold bright_white] 'FARK_SozlukListesi' >>[/]\n",EMPTY_LISTS.FARK_SozlukListesi,end="\n")
                #klavDinle.ENTER()
        EMPTY_LISTS.eklendilerListesi.append(EMPTY_LISTS.FARK_SozlukListesi) #! Kopyaya kayıt 
   
  
def FarkiJsonSozlugeEkle():        
    if EMPTY_LISTS.FARK_SozlukListesi: 
        ANAMODUL.SozlugeEkleme("VERI/students.json",EMPTY_LISTS.FARK_SozlukListesi ) #! Sözlüğe ekle
        
        c.print("""[bold yellow]yeniÖğrenciKayıdı():[/]
                💛💛💛 SözlüklüListe başarıyla oluşturuldu Şimdi json'a ekleniyor...""",style="")
        
        c.print("KAYIT:FarkiJsonSozlugeEkle: EmptyLists.FARK_SozlukListesi >> ",EMPTY_LISTS.FARK_SozlukListesi,end="\n")
                        

                
        paneller = []
        for item in EMPTY_LISTS.FARK_SozlukListesi:
                for key, value in item.items(): #ANCHOR [-1] 1. ve sonradan gelen 2. 3 .4 . .... elemana ulaştım. 
                        paneller.append(Panel(str(value), title=key, border_style="yellow")   )
                        
        c.print(Columns(paneller))        
                
               
       
    
       