#FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.

import time, re
import AsistanFonksiyonlar.klavyeDinleme as klavyeyiDinle
import MenuTablo.tablolarPY as TablolarPY,VERI.emptyLists as EmptyLists 
import time
from rich import print as print  # ya da c.print kullanıyorsan onu bırak
from rich.console import Console; c=Console()
from rich.spinner import Spinner
from rich.live import Live
from rich.columns import Columns
from rich.panel import Panel
import AnaFonksiyonlar.JSON_jobs as AnaModul
import Widgetler.SayacAnimasyon.spinner as Sayac
import Widgetler.SayacAnimasyon.geriSayar as Geri_Sayar

EmptyLists.Bulunanlar=[]   #! boş bir sözlükler listesi.
kriter=""





def bul(GirisMesaji:int):
        listeleriCleanEt()
        JSONdan_Import()    #!  her seferinde baştan yükleniyor İyi mi Kötü mü ???
        
        birSTRING=InputwithESCAPE(GirisMesaji) 
        if birSTRING is not None:
            Parsing(birSTRING)  #! KlavyedenGirilenler_Liste=[]  dolduruldu.
            arama(EmptyLists.ParsedSTRING_Listesi)  #! Bulunanlar listesi dolduruldu.
        return birSTRING 








def listeleriCleanEt():
    EmptyLists.Bulunanlar.clear()  #!j - Her sorguda önce temizle 
    EmptyLists.Jsonda_Mevcut_Veriler=[]  #! Temizlik imandandır
    EmptyLists.Jsonda_Mevcut_Veriler.clear() 
def JSONdan_Import():
    AnaModul.JSONdanImport()  


def InputwithESCAPE(hangiMesajiSecelim:int=0):
    global kriter
    while True:
        kriter=klavyeyiDinle.Mesajlar(hangiMesajiSecelim)
        if kriter is  None:
            c.print("    Ana menüye hicret ediyoruz ...................................",style="magenta")
            Sayac.spinner(4,7)
            return None    
        elif kriter == "":
            c.print("<< \"  \" Hiçbir değer girmeden [red on green] Enter [/] tuşuna bastın Beni boşuna oyalama dostum, gazabım kötüdür",style="bright_yellow")
            continue
        elif kriter.isdigit():
            secilen = int(kriter)
            if 1< secilen  > len(EmptyLists.Jsonda_Mevcut_Veriler):
                c.print("  <<< [bright_white on green] Geçersiz öğrenci numarası. Aralık dışı![/]", style="")
                continue
            return kriter.strip().lower()
        else:    
            kriter=kriter.strip().lower()
           # c.print(f" << Arama kriteriniz: [bold bright_white]{Girilenler}[/]")
            return kriter


def Parsing(metin):
    metin=metin or ""
    EmptyLists.ParsedSTRING_Listesi = re.split(r'[,\s]+', metin) #! Klavyeden girilenler temizlenip liste yapıldı. Boşluklar veya virgüller atıldı. 
    


def arama(aramaParametresi):
    EmptyLists.joinedListSozlukTek.clear()
    EmptyLists.joinedListSozlukCoklu.clear()
    
    c.print("\n")
    kriterListesi=[]
    altListeId=[]
    altListeAd= []
    altListeSoyad= []
    altListeNumarasi= []
    altListeDogTarihi= []
    altListeSinifi= []
    altListeKayitTarihi= []
    birOncekiToplam:int=0
    for metin in aramaParametresi:
        kriterListesi.append(metin)
        for ogrenci in EmptyLists.Jsonda_Mevcut_Veriler:
            if(aramaParametresi is not None and aramaParametresi!=""):
                if (metin == str(ogrenci["Id"]) or
                    metin in ogrenci["ad"].lower() or
                    metin in ogrenci["soyad"].lower() ):
                    EmptyLists.Bulunanlar.append(ogrenci)  
                    altListeId.append(str(ogrenci["Id"]));
                    altListeAd.append(ogrenci["ad"]);
                    altListeSoyad.append(ogrenci["soyad"]);
                    altListeNumarasi.append(ogrenci["ogrenciNumarasi"]);
                    altListeDogTarihi.append(ogrenci["dogumTarihi"]);
                    altListeSinifi.append(ogrenci["sinifi"]);
                    altListeKayitTarihi.append(ogrenci["kayitTarihi"]);
                else: continue
                
        joinedId="\n".join(altListeId)  
        joinedAd="\n".join(altListeAd) 
        joinedSoyad="\n".join(altListeSoyad)  
        joinedNumara="\n".join(altListeNumarasi) 
        joinedDogTar="\n".join(altListeDogTarihi)
        joinedSinif="\n".join(altListeSinifi)
        joinedKayitTarihi="\n".join(altListeKayitTarihi)
        EmptyLists.joinedListTek=[
                    metin,
                    joinedId,
                    joinedAd,
                    joinedSoyad,
                    joinedNumara,
                    joinedDogTar,
                    joinedSinif,
                    joinedKayitTarihi,
                               ]
        
        EmptyLists.joinedListSozlukTek=[{
                    "metin":metin,
                    "Id":joinedId,
                    "ad":joinedAd,
                    "soyad":joinedSoyad,
                    "ogrenciNumarasi":joinedNumara,
                    "dogumTarihi":joinedDogTar,
                    "sinifi":joinedSinif,
                    "kayitTarihi":joinedKayitTarihi,}
                                     ]
        
       #^ TablolarPY.TABLO_6lı(EmptyLists.joinedListSozlukTek, metin)    
        
        
        
        
        # c.print("Id: \n",joinedId, end="\n")
        # c.print("Ad: \n",joinedAd, end="\n")
        # c.print("Soyad:\n",joinedSoyad, end="\n")
        # c.print("Numara: \n",joinedNumara, end="\n")
        # c.print("Doğum Tarihi:\n",joinedDogTar, end="\n")
        # c.print("Sınıf: \n",joinedSinif, end="\n")
        # c.print("Kayıt Tarihi: \n",joinedKayitTarihi, end="\n")  
        
          
                
        if EmptyLists.Bulunanlar:
                    
                    # c.print(f"\n'[bright_yellow]{metin}[/]' kriterine uyan {len(EmptyLists.Bulunanlar)-birOncekiToplam} öğrenci bulundu.", end="\n")
                    from rich.panel import Panel
                    from rich.text import Text

                    text_joinedId = Text(joinedId, style="bold yellow")
                   
                    
                    
                    
                    
                    from rich.panel import Panel
                    icerikler=[ 
                    Panel(text_joinedId, title="Id",border_style="plum1"),
                    Panel(joinedAd, title="Ad",border_style="green1"),
                    Panel(joinedSoyad, title="Soyad"),
                    Panel(joinedNumara, title="No'su"),
                    Panel(joinedDogTar, title="Doğ Tarihi"),
                    Panel(joinedSinif, title="Sınıf"),
                    Panel(joinedKayitTarihi, title="Kayıt Tarihi",border_style="khaki1"),
                    ]
                    
                    
                    mesaj = f" \"  [bright_white on red]  {metin}  [/]  \" kriterine uyan [bold green]{len(EmptyLists.Bulunanlar) - birOncekiToplam}[/] öğrenci bulundu.{altListeAd}"
                    kolonlar=Columns(icerikler)
                    
                    mesaj=str(mesaj)
                   #^ c.print(Panel.fit(mesaj, title="", border_style="green"))
                   #^ c.print(kolonlar)
                    c.print(Panel.fit(kolonlar, title=mesaj, title_align="right", subtitle="Alt", subtitle_align="right",border_style="grey39"))
                    
                    
                   #^^ TablolarPY.TABLO_6lı(EmptyLists.joinedListSozlukTek, metin)    
                    EmptyLists.joinedListSozlukCoklu.append(EmptyLists.joinedListSozlukTek[0])    #^! listenin sözlük elemanını diğer listeye append ediyoruz. 
                   
                   
                   #^ c.print("joinedList\n",EmptyLists.joinedList)  
                  #  TablolarPY.TABLO_6lı()
                    
                #   TablolarPY.TABLO_6lı(EmptyLists.joinedListSozlukCoklu, )    
                  
                    birOncekiToplam=len(EmptyLists.Bulunanlar) 
                    altListeId.clear();joinedId=""
                    altListeAd.clear()
                    altListeSoyad.clear()
                    altListeNumarasi.clear()
                    altListeDogTarihi.clear()
                    altListeSinifi.clear()
                    altListeKayitTarihi.clear()
                    
                    joinedId=""
                    joinedAd=""
                    joinedSoyad=""
                    joinedNumara=""
                    joinedDogTar=""
                    joinedSinif=""
                    joinedKayitTarihi=""
        else:
                    c.print(f" {metin} kriteriyle uyuşan bir öğrenci bulamadım, Üzgünüm.")     

    
    return aramaParametresi


