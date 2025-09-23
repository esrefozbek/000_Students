#FIXME -  çıkışta girlen öğrenciyi/öğrencileri kaydedeyim mi  Evet/Enter    Hayır/Esc seçeneği olsun. 
#FIXME - ilk öğrenci tamamlandığında yeni öğrenci girişi BANNER i yerine "Yeni öğrencinin ADINI giriniz:(Bu aşamada 'Esc' ile kayıttan çıkabilirsin):"  seçeneği tekrar gelsin.
#FIXME - çıkmak için Esc ye bastığında "Devam etmek için ENTER tuşuna bas..."  yerine "Girilen öğrencileri kaydetmek için Enter/e   kayıttan vazgeçmek için Esc/H  seçin"   gelsin

#breakpoint()

import AnaFonksiyonlar.ogrenci_LiSTEleme as Ogr_List
import AnaFonksiyonlar.JSON_jobs as AnaModul
import AsistanFonksiyonlar.klavyeDinleme as klavyeyiDinle
import VERI.emptyLists as veriYolu 
import  AsistanFonksiyonlar.tupleyi_Sozluklestirme as AsistanModul
from AnaFonksiyonlar.student_class import Ogrenciler
from rich.console import Console ;c=Console()
from rich.prompt import Prompt
import Widgetler.SayacAnimasyon.spinner as SpinnerPY 
from rich.panel import Panel
from rich.columns import Columns


lastID=0
toplamKayit=0

def yeniOgrenciKayidi():
        veriYolu.FARK_SozlukListesi.clear();
        veriYolu.FARK_SozlukListesi.clear(); 
        while True:            
                ogrenci=inputOgr() 
                if ogrenci is None: break
                nesne=klasSureci(ogrenci)
                FarkSozlukListesineAppend(nesne) 
        FarkiJsonSozlugeEkle()
        
def inputOgr():
        global toplamKayit
        
        while True:
                if toplamKayit==0:
                        c.print(Panel.fit("[bold][yellow2]📝 Yeni Öğrenci Girişi [/][/][italic grey30]\n📌 Anamenü'ye [bold orange_red1]Esc[/] ile dönebilirsin.[/]", border_style="green_yellow"), end="")
                else:
                        pass
                              
                #NOTE -  Burada ad giriliyor, 'Esc'  ye basılırsa yeni öğrenci kayıdı sonlandırılıyor.
                ad = klavyeyiDinle.Mesajlar(3)  
                if ad is None :  #NOTE - None, Esc ye basıldı anlamına geliyor. 
                        c.print(f"\n{toplamKayit} öğrenci bilgisi sağladınız...\n",style="",end="\n")
                        SpinnerPY.spinner(4,4) if toplamKayit>0  else SpinnerPY.spinner(3,6) 
                        c.print("kayıt::inputOgr: toplamKayit 1>>",toplamKayit)
                        return None
                else:
                        ad=ad.strip()
                
                # print("\n")       
                c.print("\n\t[green]SOYADI[/] ",end="    >> "); soyad = input().strip()
                c.print("\t[green]NUMARASI[/] ",end="  >> ");  ogrenciNumarasi = input().strip()
                #c.print("\t[green]Doğum Tarihi[/] ",end=" >> "); 
                c.print("\t[green]Doğum Tarihi[/] [grey23][01/01/2000][/]",end=" >> ");dogumTarihi =input().strip()
                c.print("\t[green]SINIFI[/] ",end="    >> "); sinifi = input().strip()
        
                ogrenci=(ad, soyad, ogrenciNumarasi, dogumTarihi, sinifi)
                toplamKayit +=1 
                c.print("kayıt::inputOgr: toplamKayit 2>>",toplamKayit)
                return ogrenci 



def klasSureci(ogrenci):
              
              #  OgrenciTuple = ogrenci  
                OgrenciNesnesi = Ogrenciler(*ogrenci)   
                nesne=OgrenciNesnesi.toDict()
                return nesne
           
   

def FarkSozlukListesineAppend(nesne):  
       
        veriYolu.FARK_SozlukListesi.append(nesne) #! append to Tuple
                
        c.print(f"{toplamKayit}, [white]öğrencinin bilgileri geçici hafızaya alındı[/] \n")
        c.print(f"KAYIT:: '{len(veriYolu.FARK_SozlukListesi)}' [bold bright_white] 'FARK_SozlukListesi' >>[/]\n",veriYolu.FARK_SozlukListesi,end="\n")
                #klavDinle.ENTER()
        veriYolu.eklendilerListesi.append(veriYolu.FARK_SozlukListesi) #! Kopyaya kayıt 
   
  
def FarkiJsonSozlugeEkle():        
    if veriYolu.FARK_SozlukListesi: 
        AnaModul.SozlugeEkleme("VERI/students.json",veriYolu.FARK_SozlukListesi ) #! Sözlüğe ekle
        
        c.print("""[bold yellow]yeniÖğrenciKayıdı():[/]
                💛💛💛 SözlüklüListe başarıyla oluşturuldu Şimdi json'a ekleniyor...""",style="")
        
        c.print("KAYIT:FarkiJsonSozlugeEkle: EmptyLists.FARK_SozlukListesi >> ",veriYolu.FARK_SozlukListesi,end="\n")
                        

                
        paneller = []
        for item in veriYolu.FARK_SozlukListesi:
                for key, value in item.items(): #ANCHOR [-1] 1. ve sonradan gelen 2. 3 .4 . .... elemana ulaştım. 
                        paneller.append(Panel(str(value), title=key, border_style="yellow")   )
                        
        c.print(Columns(paneller))        
                
               
       
    
       