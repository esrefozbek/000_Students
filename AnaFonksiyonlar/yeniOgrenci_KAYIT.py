#FIXME -  çıkışta girlen öğrenciyi/öğrencileri kaydedeyim mi  Evet/Enter    Hayır/Esc seçeneği olsun. 
#FIXME - ilk öğrenci tamamlandığında yeni öğrenci girişi BANNER i yerine "Yeni öğrencinin ADINI giriniz:(Bu aşamada 'Esc' ile kayıttan çıkabilirsin):"  seçeneği tekrar gelsin.
#FIXME - çıkmak için Esc ye bastığında "Devam etmek için ENTER tuşuna bas..."  yerine "Girilen öğrencileri kaydetmek için Enter/e   kayıttan vazgeçmek için Esc/H  seçin"   gelsin

#breakpoint()
import Widgetler.SayacAnimasyon.spinner as SpinnerPY 
import Widgetler.randomRenk as RR
import AnaFonksiyonlar.JSON_jobs as JSON_
import AsistanFonksiyonlar.klavyeDinleme as KLAVYEDINLE
import VERI.emptyLists as E_LISTS 
from AnaFonksiyonlar.student_class import Ogrenciler
import MenuTablo.tablolarPY as TABLO
from rich.console import Console ;c=Console()
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
import VERI.mesajlar as MESAJLAR
from typing import Dict, Any



lastID=0
ogrenciDatasi=0

def yeniOgrenciKayidi():
        E_LISTS.FARK_SozlukListesi.clear();
        E_LISTS.FARK_SozlukListesi.clear(); 
        while True:            
                ogrenci=inputOgr() 
                if ogrenci is None: break
                nesne=klasSureci(ogrenci)
                FarkSozlukListesineAppend(nesne) 
        FarkiJsonSozlugeEkle()
       
def inputOgr():
        global ogrenciDatasi
        rengim=E_LISTS.renk
        while True:
                MESAJLAR.Mesajlar(8)
                ad=KLAVYEDINLE.KlavyeDinle()
                if ad is None: break
                
                c.print("\n \t↳ ↳ SOYADI          > ", style=rengim, end="")
                soyad=KLAVYEDINLE.KlavyeDinle()
                if soyad is None: break
                
                c.print("\n \t↳ ↳ Numara          > ", style=rengim, end="")
                ogrenciNumarasi=KLAVYEDINLE.KlavyeDinle()
                if ogrenciNumarasi is None: break
                
                c.print("\n \t↳ ↳ Şube            > ", style=rengim, end="")
                sinifi=KLAVYEDINLE.KlavyeDinle()
                if sinifi is None: break
  
                c.print("\n \t↳ ↳ Doğum Tarihi    > ", style=rengim, end="") 
                dogumTarihi=KLAVYEDINLE.KlavyeDinle()
                if dogumTarihi is None: break
                
                ogrenci=(ad.capitalize(), soyad.capitalize(), ogrenciNumarasi, dogumTarihi, sinifi.capitalize()  )
                ogrenciDatasi+=1
                
                return ogrenci  # Return ile döngüden çıkılıyor, nesne=klasSureci(ogrenci)                 FarkSozlukListesineAppend(nesne)  süreçleri uygulanıyor VE tekrar  
  
        if E_LISTS.FARK_SozlukListesi:
                c.print(f"\n🌟🌟🌟 Hafızada {len(E_LISTS.FARK_SozlukListesi)} adet kayıt bekleyen öğrenci verisi var. 💛💛💛✨✨\n ")
  
  
        
        
def klasSureci(ogrenci):
        #  OgrenciTuple = ogrenci  
        OgrenciNesnesi = Ogrenciler(*ogrenci)   
        nesne=OgrenciNesnesi.toDict()
        return nesne
           
   

def FarkSozlukListesineAppend(nesne):  
        
        E_LISTS.FARK_SozlukListesi.append(nesne) #! append to Tuple
        #c.print(f"\t{ogrenciDatasi}, [white]öğrencinin bilgileri geçici hafızaya alındı![/] ")
        
    #    c.print("👇👇👇🛍️🛍️",ogrenci_panel())

                    #klavDinle.ENTER()
        E_LISTS.eklendilerListesi.append(E_LISTS.FARK_SozlukListesi) #! Kopyaya kayıt 
        print("\n")
        

def FarkiJsonSozlugeEkle():   
        c.print("\n👇👇👇 Eklenenler: \n",TABLO.ogrenci_panel())  # Farklistesi alttaki JSON_.SozlugeEkleme de silindiği için burada verdim.
        
        JSON_.SozlugeEkleme("VERI/students.json",E_LISTS.FARK_SozlukListesi ) #! Sözlüğe ekle
        
     #   c.print("""🌟🌟🌟🦀🦀\n💛💛💛 [bold turquoise2]SözlüklüListe başarıyla oluşturuldu Şimdi sisteme ekleniyor...[/] 📉📉""",style="")
        
               
       
        

def iptal(girdi):
        if girdi is None :  #NOTE - None, Esc ye basıldı anlamına geliyor. 
                c.print(f"🚢🚢 🤔🚜 {ogrenciDatasi} öğrenci bilgisi sağladınız...💕💕👑👑\n",style="yellow",end="\n")
                
#                SpinnerPY.spinner(1,4) if ogrenciDatasi>0  else SpinnerPY.spinner(1,6) 
                #        c.print("KAYIT>>inputOgr: Toplam Kayit -->",ogrenciDatasi,style="green")
                return None
        else:
                girdi=girdi.strip()