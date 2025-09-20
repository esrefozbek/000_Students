# - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.

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
                if (metin == str(ogrenci["Id"]) or metin in ogrenci["ad"].lower() or metin in ogrenci["soyad"].lower() ):
                    EmptyLists.Bulunanlar.append(ogrenci)  
                    altListeId.append(str(ogrenci["Id"]))
                    altListeAd.append(ogrenci["ad"])
                    altListeSoyad.append(ogrenci["soyad"])
                    altListeNumarasi.append(ogrenci["ogrenciNumarasi"])
                    altListeDogTarihi.append(ogrenci["dogumTarihi"])
                    altListeSinifi.append(ogrenci["sinifi"])
                    altListeKayitTarihi.append(ogrenci["kayitTarihi"])
                else: 
                    continue
                
        joinedId="\n".join(altListeId)  
        joinedAd="\n".join(altListeAd) 
        joinedSoyad="\n".join(altListeSoyad)  
        joinedNumara="\n".join(altListeNumarasi) 
        joinedDogTar="\n".join(altListeDogTarihi)
        joinedSinif="\n".join(altListeSinifi)
        joinedKayitTarihi="\n".join(altListeKayitTarihi)
        
        EmptyLists.joinedListTek=[ metin,joinedId,joinedAd,joinedSoyad,joinedNumara,joinedDogTar,joinedSinif,joinedKayitTarihi ]
        
        from rich.panel import Panel
        from rich.text import Text
                   
        text_joinedId = Text(joinedId, style="bold yellow")
                   
        icerikler=[ 
                    Panel(metin, title="metin",border_style="gold1"),
                    Panel(text_joinedId, title="Id",border_style="plum1"),
                    Panel(joinedAd, title="Ad",border_style="green1"),
                    Panel(joinedSoyad, title="Soyad",border_style=""),
                    Panel(joinedNumara, title="No'su",border_style="light_goldenrod2"),
                    Panel(joinedDogTar, title="Doğ Tarihi",border_style="dark_olive_green2"),
                    Panel(joinedSinif, title="Sınıf"),
                    Panel(joinedKayitTarihi, title="Kayıt Tarihi",border_style="khaki1"),
                    ]
        
        EmptyLists.joinedListSozlukTek=[{
                    "metin":metin,
                    "Id":joinedId,
                    "ad":joinedAd,
                    "soyad":joinedSoyad,
                    "ogrenciNumarasi":joinedNumara,
                    "dogumTarihi":joinedDogTar,
                    "sinifi":joinedSinif,
                    "kayitTarihi":joinedKayitTarihi,}        ]
        
        
        
        
       #^ TablolarPY.TABLO_6lı(EmptyLists.joinedListSozlukTek, metin)    
        
        
        
        c.print(f"\n[underline yellow]{metin}[/]\n ")
        # c.print("Id: \n",joinedId, end="\n")
        # c.print("\nAd: \n",joinedAd, end="\n")
        # c.print("\nSoyad:\n",joinedSoyad, end="\n")
        # c.print("\nNumara: \n",joinedNumara, end="\n")
        # c.print("\nDoğum Tarihi:\n",joinedDogTar, end="\n")
        # c.print("\nSınıf: \n",joinedSinif, end="\n")
        # c.print("\nKayıt Tarihi: \n",joinedKayitTarihi, end="\n")  
        # c.print("\n")
        
        
        
        
        
          
                
        if EmptyLists.joinedListSozlukTek:
                    
                    # c.print(f"\n'[bright_yellow]{metin}[/]' kriterine uyan {len(EmptyLists.Bulunanlar)-birOncekiToplam} öğrenci bulundu.", end="\n")
                    
                    
                    
                    renk="bright_white on green"
                    mesaj = f"[{renk}]   {metin}   [/] kriterine uyan [bold green]{len(EmptyLists.Bulunanlar) - birOncekiToplam}[/] öğrenci bulundu.{altListeAd}\n"
                    
                    kolonlar=Columns(icerikler)
                    
                   # mesaj=str(mesaj)      #!!!!  panel String kabul ettiği için.....
                   #^ c.print(Panel.fit(mesaj, title="", border_style="green"))
                   #^ c.print(kolonlar)
                  #  if joinedId :
                    renk="bright_white on green"
                    c.print(Panel.fit(kolonlar, title=mesaj, title_align="left", subtitle="Değişken", subtitle_align="right",border_style="grey39"))
                    #else:
                   # c.print(f" [white on red]   {metin}   [/] kriteriyle uyuşan bir öğrenci bulamadım, Üzgünüm.\n")  
                    
                        
                    
                    
                    from rich.panel import Panel
                    paneller = []
                    for key, value in EmptyLists.joinedListSozlukTek[-1].items():   #ANCHOR - -  - [-1] 1. ve sonradan gelen 2. 3 .4 . .... elemana ulaştım. Çok önemli bir hile.  
                            paneller.append(Panel(value, title=key, border_style="green")   )
                    #if joinedId: 
                    renk="bright_white on green"
                    c.print(Columns(paneller))
                    # else:
                    #     c.print(f" [bright_white on red]   {metin}   [/] kriteriyle uyuşan bir öğrenci bulamadım, Üzgünüm.")  
                           
                    
                    
                   #^^ TablolarPY.TABLO_6lı(EmptyLists.joinedListSozlukTek, metin)    
                    EmptyLists.joinedListSozlukCoklu.append(EmptyLists.joinedListSozlukTek[0])    #^! listenin sözlük elemanını diğer listeye append ediyoruz. 
                   
                                        
                    birOncekiToplam=len(EmptyLists.Bulunanlar) 
                    altListeId.clear();
                    joinedId=""
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
                    c.print(f" [bold cyan on red]   {metin}   [/] kriterinde bir veri yok.\n")     

        
        for sozluk in EmptyLists.joinedListSozlukCoklu:
            for k, v in sozluk.items():
                if v.strip() == "":
                    sozluk[k] = "+++++++++??"
                
     #^CTRL    c.print("arama>arama> joinedListSozlukCoklu >>",EmptyLists.joinedListSozlukCoklu)
     
    from rich import  print as rprint
    
    rprint("Eşref özbek 5454")
       
            
        
        
        
        
        
    return aramaParametresi


