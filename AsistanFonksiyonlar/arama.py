#FIXME - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.

import time, re
import AsistanFonksiyonlar.klavyeDinleme as klavyeyiDinle
from rich.console import Console; console = Console()
import MenuTablo.tablolarPY as TablolarPY,VERI.emptyLists as EmptyLists 
from rich.live import Live
import time
from rich.console import Console; c=Console()
from rich.spinner import Spinner
import AnaFonksiyonlar.JSON_jobs as AnaModul
import Widgetler.SayacAnimasyon.spinner as Sayac
import Widgetler.SayacAnimasyon.geriSayar as Geri_Sayar

EmptyLists.Bulunanlar=[]   #! boş bir sözlükler listesi.
kriter=""





def bul(GirisMesaji:int):
        EmptyLists.Bulunanlar.clear()  #!j - Her sorguda önce temizle 
        listeleriCleanEt()
        JSONdan_Import()    #!  her seferinde baştan yükleniyor İyi mi Kötü mü ???
        
        birSTRING=InputwithESCAPE(GirisMesaji) 
        if birSTRING is not None:
            Parsing(birSTRING)  #! KlavyedenGirilenler_Liste=[]  dolduruldu.
            arama(EmptyLists.birSTRING_Parsing_Listesi)  #! Bulunanlar listesi dolduruldu.
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
    EmptyLists.birSTRING_Parsing_Listesi = re.split(r'[,\s]+', metin) #! Klavyeden girilenler temizlenip liste yapıldı. Boşluklar veya virgüller atıldı. 
    


def arama(aramaParametresi):
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
                    altListeId.append(ogrenci["Id"])
                    altListeAd.append(ogrenci["ad"])
                    altListeSoyad.append(ogrenci["soyad"])
                    altListeNumarasi.append(ogrenci["ogrenciNumarasi"])
                    altListeDogTarihi.append(ogrenci["dogumTarihi"])
                    altListeSinifi.append(ogrenci["sinifi"])
                    altListeKayitTarihi.append(ogrenci["kayitTarihi"])
                else: continue
       # cizgi=len(str(len( altListeAd)))*'-'+  (sum(len(s)+4 for s in altListeAd)-2)*'-' + len(metin)*'-' + 36*'-'
      #  if len(cizgi)>110: cizgi='-'*115
        
        if EmptyLists.Bulunanlar:
               #     c.print("\n",cizgi, style="bold green", end="\n")
                    
                    from rich.panel import Panel
                    from rich import print as print  # ya da c.print kullanıyorsan onu bırak

                    
                    mesaj = f"[bold yellow]{metin}[/] kriterine uyan [bold green]{len(EmptyLists.Bulunanlar) - birOncekiToplam}[/] öğrenci bulundu.{altListeAd}"
                    c.print(Panel.fit(mesaj, title="", border_style="green"))
                    
                  #  c.print(f" {metin} kriterine uyan {len(EmptyLists.Bulunanlar)-birOncekiToplam} öğrenci bulundu. {altListeAd} ", end="")
                    birOncekiToplam=len(EmptyLists.Bulunanlar) 
                    altListeId.clear()
                    altListeAd.clear()
                    altListeSoyad.clear()
                    altListeNumarasi.clear()
                    altListeDogTarihi.clear()
                    altListeSinifi.clear()
                    altListeKayitTarihi.clear()
        else:
                    c.print(f" {aramaParametresi} Bu kritere uyan bir öğrenci bulamadım, Üzgünüm.")     
        

    return aramaParametresi


