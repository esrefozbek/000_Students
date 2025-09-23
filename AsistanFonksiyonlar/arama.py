 #£  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
  #€  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
  #?  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
  #~   C:\Users\Markus\AppData\Roaming\Code\User\settings.json   
  #_  asdasdasdasdasda23423424242342       
  #** asddasdsadasadasdad2342342342342342            


from rich.text import Text
# - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.

import time, re
import AsistanFonksiyonlar.klavyeDinleme as klavyeyiDinle
import MenuTablo.tablolarPY as TablolarPY,VERI.emptyLists as veriYolu 
import time
from rich import print as p # ya da c.print kullanıyorsan onu bırak
from rich.console import Console; c=Console()
from rich.spinner import Spinner
from rich.live import Live
from rich.columns import Columns
from rich.panel import Panel
from rich.panel import Panel
import AnaFonksiyonlar.JSON_jobs as AnaModul
import Widgetler.SayacAnimasyon.spinner as Sayac
import Widgetler.SayacAnimasyon.geriSayar as Geri_Sayar

veriYolu.Bulunanlar=[]   #! boş bir sözlükler listesi.
kriter=""



veriYolu.Bulunanlar=[]   #! boş bir sözlükler listesi.
veriYolu.altAnaListeTeklerKriterli=[]
veriYolu.altAnaListeTeklerKritersiz=[]

veriYolu.altAnaListeTumKriterli=[]
veriYolu.altAnaListeTumKritersiz= []

veriYolu.Joined_altAnaListeTekler=[]
veriYolu.Joined_altAnaListeTumKriterli=[]




def bul(GirisMesaji:int):
        
        listeleriCleanEt()
        JSONdan_Import()    #!  her seferinde baştan yükleniyor İyi mi Kötü mü ???
        
        kriter=InputwithESCAPE(GirisMesaji) 
#        if kriter is not None:
        Parsing(kriter)  #! EmptyLists.ParsedSTRING_Listesi=[]  dolduruldu.
        KriterleriBul(veriYolu.ParsedSTRING_Listesi)
#        tumKriterleriBul(EmptyLists.ParsedSTRING_Listesi)  #! EmptyLists.Bulunanlar listesi ve altAnaListe dolduruldu.
#        joinification(EmptyLists.altAnaListeTeklerKritersiz)
        joinification(veriYolu.altAnaListeTeklerKriterli)
        panelisation(veriYolu.Joined_altAnaListeTekler)
        TabloyaSozlukYap(veriYolu.Joined_altAnaListeTekler)
        
        return  


def listeleriCleanEt():
    veriYolu.altAnaListeTeklerKritersiz=      [[],[],[],[],[],[],[]]
    veriYolu.altAnaListeTeklerKriterli=       [[],[],[],[],[],[],[],[]]
    veriYolu.altAnaListeTumKriterli=                  [[],[],[],[],[],[],[],[]]
    veriYolu.altAnaListeTumKritersiz=                  [[],[],[],[],[],[],[]]
    
    veriYolu.Joined_altAnaListeTekler.clear() 
    veriYolu.Joined_altAnaListeTeklerKriterli.clear() 
    
    veriYolu.Joined_altAnaListeTumKritersiz=   [[],[],[],[],[],[],[]]
    veriYolu.Joined_altAnaListeTumKriterli=    [[],[],[],[],[],[],[],[]]
    
    veriYolu.Bulunanlar.clear()  #!j - Her sorguda önce temizle 
    veriYolu.BulunanIDler.clear()
    veriYolu.Jsonda_Mevcut_Veriler=[]  #! Temizlik imandandır
    veriYolu.Jsonda_Mevcut_Veriler.clear()
    
   
     
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
            if 1< secilen  > len(veriYolu.Jsonda_Mevcut_Veriler):
                c.print("  <<< [bright_white on green] Geçersiz öğrenci numarası. Aralık dışı![/]", style="")
                continue
            return kriter.strip().lower()
        else:    
            kriter=kriter.strip().lower()
           # c.print(f" << Arama kriteriniz: [bold bright_white]{Girilenler}[/]")
            return kriter

def Parsing(kriter):
    kriter=kriter or ""
    veriYolu.ParsedSTRING_Listesi=[]
    veriYolu.ParsedSTRING_Listesi = re.split(r'[,\s]+', kriter) #! Klavyeden girilenler temizlenip liste yapıldı. Boşluklar veya virgüller atıldı. 
        
def KriterleriBul(aramaParametresi:list):   #~           TEK KRİTER              
    kriterListesi=[]
    birOncekiToplam:int=0
    veriYolu.altAnaListeTeklerKriterli = [[[] for _ in range(8)] for _ in range(len(aramaParametresi))]
    veriYolu.altAnaListeTeklerKritersiz = [[[] for _ in range(7)] for _ in range(len(aramaParametresi))]
    
    for i, metin in enumerate(aramaParametresi):
        veriYolu.altAnaListeTeklerKriterli[i][0]=[metin]
        veriYolu.altAnaListeTumKriterli[0]=aramaParametresi
        for ogrenci in veriYolu.Jsonda_Mevcut_Veriler:
            if(metin is not None and metin!=""):
                if (metin == str(ogrenci["Id"]) or
                    metin in ogrenci["ad"].lower() or
                    metin in ogrenci["soyad"].lower() ):             

                    veriYolu.Bulunanlar.append(ogrenci) 
                    veriYolu.BulunanIDler.append(ogrenci["Id"]) 
                    
                    for j,val in enumerate(ogrenci.values() ):
                        veriYolu.altAnaListeTeklerKriterli[i][j+1].append(str(val))
                        veriYolu.altAnaListeTeklerKritersiz[i][j].append(str(val))
                        veriYolu.altAnaListeTumKriterli[j+1].append(str(val))
                        veriYolu.altAnaListeTumKritersiz[j].append(str(val))
                else: 
                    continue
                           
    p("\n");c.rule("    SONUÇLAR    ",style="red") ;
    
""" 
        p("Arama>kriterleriBul: EmptyLists.altAnaListeTeklerKriterli >>",EmptyLists.altAnaListeTeklerKriterli)
        p("Arama>kriterleriBul: EmptyLists.altAnaListeTeklerKritersiz >>",EmptyLists.altAnaListeTeklerKritersiz)
        p("Arama>kriterleriBul: EmptyLists.altAnaListeTumKriterli >>",EmptyLists.altAnaListeTumKriterli)
        p("Arama>kriterleriBul: EmptyLists.altAnaListeTumKritersiz >>",EmptyLists.altAnaListeTumKritersiz)
        # p("Arama>kriterleriBul: EmptyLists.Bulunanlar >>",EmptyLists.Bulunanlar)
 """


       
def joinification(liste:list):
    veriYolu.Joined_altAnaListeTekler= [["" for _ in range(len(liste[0]))] for _ in range(len(liste))]   
    for i,grup in enumerate(liste):
        for j,sutun  in enumerate(grup):      
            veriYolu.Joined_altAnaListeTekler[i][j]="\n".join(sutun)
    p("\nArama>joynlama: EmptyLists.Joined_altAnaListeTekler  >> ",veriYolu.Joined_altAnaListeTekler)

        
def panelisation(joinedLists):
    icerikler = []
    renk=["yellow","plum1","green1","light_goldenrod2","dark_olive_green2","khaki1","dodger_blue2","green4"]
    basliklar=["kriter","Id","Ad","Soyad","No'su","Doğ Tarihi","Sınıf","Kayıt Tarihi"]
    
    for j, joinedList in enumerate(joinedLists):
        paneller=[]
        for i,longString in enumerate(joinedList):
            pan=(Panel(Text(longString, style="bold yellow"), title=basliklar[i], border_style=renk[i]))
            paneller.append(pan)
        icerikler.append(Panel(Columns(paneller), title="başlık parası", border_style="white"))
    p(Columns(icerikler),end="\n")
  




def TabloyaSozlukYap(liste):
    basliklar = ["kriter", "Id", "ad", "soyad", "ogrenciNumarasi", "dogumTarihi", "sinifi", "kayitTarihi"]
    
    veriYolu.Joined_altAnaListeTeklilerSozluk = []

    for item in liste:
        sozluk = {}
        for j in range(len(item)):
            sozluk[basliklar[j]] = item[j]
        veriYolu.Joined_altAnaListeTeklilerSozluk.append(sozluk)

  #  p(EmptyLists.Joined_altAnaListeTeklilerSozluk)
    
    TablolarPY.genel_TABLO(veriYolu.Joined_altAnaListeTeklilerSozluk, )    
    
"""
        
         
        
 


                    
                                        
                      
        for sozluk in EmptyLists.joinedListSozlukCoklu:
            for k, v in sozluk.items():
                if v.strip() == "":
                    sozluk[k] = "+++++++++??"
                
     #^CTRL    c.print("arama>arama> joinedListSozlukCoklu >>",EmptyLists.joinedListSozlukCoklu)
     
           
        
        
        
        
        
    return aramaParametresi


 """    