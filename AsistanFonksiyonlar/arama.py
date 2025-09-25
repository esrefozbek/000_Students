 #£  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
  #€  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
  #?  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
  #~   C:\Users\Markus\AppData\Roaming\Code\User\settings.json   
  #_  asdasdasdasdasda23423424242342       
  #** asddasdsadasadasdad2342342342342342            

# - ogrenci_SiLME.py de  " "  boşluk arattığımda tüm liste dökülüyor önüme.

from rich.text import Text
import  re
import AsistanFonksiyonlar.klavyeDinleme as KLAVYE_DINLE
import MenuTablo.tablolarPY as TABLOLAR
import VERI.emptyLists as EMPTY_LISTS 
import VERI.mesajlar as MESAJLAR

from rich import print as p # ya da c.print kullanıyorsan onu bırak
from rich.console import Console; c=Console()
from rich.columns import Columns
from rich.panel import Panel
import AnaFonksiyonlar.JSON_jobs as ANAMODUL
import Widgetler.SayacAnimasyon.spinner as SAYAC


EMPTY_LISTS.Bulunanlar=[]   #! boş bir sözlükler listesi.
kriter=""



EMPTY_LISTS.Bulunanlar=[]   #! boş bir sözlükler listesi.
EMPTY_LISTS.altAnaListeTeklerKriterli=[]
EMPTY_LISTS.altAnaListeTeklerKritersiz=[]

EMPTY_LISTS.altAnaListeTumKriterli=[]
EMPTY_LISTS.altAnaListeTumKritersiz= []

EMPTY_LISTS.Joined_altAnaListeTekler=[]
EMPTY_LISTS.Joined_altAnaListeTumKriterli=[]




def bul_AnaFonksiyon(GirisMesaji:int):
        
        listeleriCleanEt()
        JSONdan_Import()    #!  her seferinde baştan yükleniyor İyi mi Kötü mü ???
        
        kriter=InputwithESCAPE(GirisMesaji) 
        if kriter is not None:
            Parsing(kriter)  #! EmptyLists.ParsedSTRING_Listesi=[]  dolduruldu.
            KriterleriBul(EMPTY_LISTS.ParsedSTRING_Listesi)
#            tumKriterleriBul(EmptyLists.ParsedSTRING_Listesi)  #! EmptyLists.Bulunanlar listesi ve altAnaListe dolduruldu.
#            joinification(EmptyLists.altAnaListeTeklerKritersiz)
            joinification(EMPTY_LISTS.altAnaListeTeklerKriterli)
            panelisation(EMPTY_LISTS.Joined_altAnaListeTekler)
            TabloyaSozlukYap(EMPTY_LISTS.Joined_altAnaListeTekler)
            TABLOLAR.genel_TABLO(EMPTY_LISTS.Joined_TeklilerSozluk, ) 
            return kriter         
        else:
            return None
          


def listeleriCleanEt():
    EMPTY_LISTS.altAnaListeTeklerKritersiz=      [[],[],[],[],[],[],[]]
    EMPTY_LISTS.altAnaListeTeklerKriterli=       [[],[],[],[],[],[],[],[]]
    EMPTY_LISTS.altAnaListeTumKriterli=                  [[],[],[],[],[],[],[],[]]
    EMPTY_LISTS.altAnaListeTumKritersiz=                  [[],[],[],[],[],[],[]]
    
    EMPTY_LISTS.Joined_altAnaListeTekler.clear() 
    EMPTY_LISTS.Joined_altAnaListeTeklerKriterli.clear() 
    
    EMPTY_LISTS.Joined_altAnaListeTumKritersiz=   [[],[],[],[],[],[],[]]
    EMPTY_LISTS.Joined_altAnaListeTumKriterli=    [[],[],[],[],[],[],[],[]]
    
    EMPTY_LISTS.Bulunanlar.clear()  #!j - Her sorguda önce temizle 
    EMPTY_LISTS.BulunanIDler.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler=[]  #! Temizlik imandandır
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    
   
     
def JSONdan_Import():
    ANAMODUL.JSONdanImport()  

def InputwithESCAPE(mesaj:int=0):
    global kriter
    while True:
        MESAJLAR.Mesajlar(mesaj)
        kriter=KLAVYE_DINLE.KlavyeDinle()
        if kriter is  None:
#            c.print("    Ana menüye hicret ediyoruz ...................................",style="magenta")
            SAYAC.spinner(4,7)
            return None    
        elif kriter == "":
            c.print("<< \"  \" Hiçbir değer girmeden [red on green] Enter [/] tuşuna bastın Beni boşuna oyalama dostum, gazabım kötüdür",style="bright_yellow")
            continue
        else:    
           #_       kriter=str(kriter).strip().lower()         
            return kriter

def Parsing(kriter):
    kriter=kriter or ""
    EMPTY_LISTS.ParsedSTRING_Listesi=[]
    EMPTY_LISTS.ParsedSTRING_Listesi = re.split(r'[,\s]+', kriter) 
    #! Klavyeden girilenler temizlenip liste yapıldı. Boşluklar veya virgüller atıldı. 
        
def KriterleriBul(aramaParametresi:list):   #~           TEK KRİTER              
    kriterListesi=[]
    birOncekiToplam:int=0
    EMPTY_LISTS.altAnaListeTeklerKriterli = [[[] for _ in range(8)] for _ in range(len(aramaParametresi))]
    EMPTY_LISTS.altAnaListeTeklerKritersiz =[[[] for _ in range(7)] for _ in range(len(aramaParametresi))]
    
    for i, metin in enumerate(aramaParametresi):
        EMPTY_LISTS.altAnaListeTeklerKriterli[i][0]=[metin]
        EMPTY_LISTS.altAnaListeTumKriterli[0]=aramaParametresi
        for ogrenci in EMPTY_LISTS.Jsonda_Mevcut_Veriler:
            if(metin is not None and metin!=""):
                if (metin == str(ogrenci["Id"]) or
                    metin in ogrenci["ad"].lower() or
                    metin in ogrenci["soyad"].lower()or
                    metin in ogrenci["ogrenciNumarasi"] or
                    metin in ogrenci["dogumTarihi"] or
                    metin in ogrenci["sinifi"].lower() or
                    metin in ogrenci["kayitTarihi"]
                    
                    ):             

                    EMPTY_LISTS.Bulunanlar.append(ogrenci) 
                    EMPTY_LISTS.BulunanIDler.append(ogrenci["Id"]) 
                    
                    for j,val in enumerate(ogrenci.values() ):
                        EMPTY_LISTS.altAnaListeTeklerKriterli[i][j+1].append(str(val))
                        EMPTY_LISTS.altAnaListeTeklerKritersiz[i][j].append(str(val))
                        EMPTY_LISTS.altAnaListeTumKriterli[j+1].append(str(val))
                        EMPTY_LISTS.altAnaListeTumKritersiz[j].append(str(val))
                else: 
                    continue
                           
    p("\n");c.rule("    SONUÇLAR    ",style="red") ;
 
def joinification(liste:list):
    EMPTY_LISTS.Joined_altAnaListeTekler= [["" for _ in range(len(liste[0]))] for _ in range(len(liste))]   
    for i,grup in enumerate(liste):
        for j,sutun  in enumerate(grup):      
            EMPTY_LISTS.Joined_altAnaListeTekler[i][j]="\n".join(sutun)
#_    p("\nArama>joynlama: EmptyLists.Joined_altAnaListeTekler  >> ",veriYolu.Joined_altAnaListeTekler)     

def panelisation(joinedLists):
    icerikler = []
    renk=["yellow","orange1","green1","light_goldenrod2","dark_olive_green2","khaki1","dodger_blue2","green4"]
    basliklar=["kriter","Id","Ad","Soyad","No'su","Doğ Tarihi","Sınıf","Kayıt Tarihi"]
    
    for j, joinedList in enumerate(joinedLists):
        paneller=[]
        for i,longString in enumerate(joinedList):
            pan=(Panel.fit(Text(longString, style="grey35"), title=basliklar[i], border_style=renk[i]))
            paneller.append(pan)
        icerikler.append(Panel.fit(Columns(paneller), title="başlık ", border_style="grey15"))
    col=Columns(icerikler)
    p(col,end="\n")
  
def TabloyaSozlukYap(liste):
    basliklar = ["kriter", "Id", "ad", "soyad", "ogrenciNumarasi", "dogumTarihi", "sinifi", "kayitTarihi"]
    
    EMPTY_LISTS.Joined_TeklilerSozluk = []

    for item in liste:
        sozluk = {}
        for j in range(len(item)):
            sozluk[basliklar[j]] = item[j]  #_ key:value yapıdı. 
        EMPTY_LISTS.Joined_TeklilerSozluk.append(sozluk)

#_    p("Arama>>TabloyaSozluk: VERI.Joined_TeklilerSozluk ",VERI.Joined_TeklilerSozluk)
    

    
"""
        
         
        
 


                    
                                        
                      
        for sozluk in EmptyLists.joinedListSozlukCoklu:
            for k, v in sozluk.items():
                if v.strip() == "":
                    sozluk[k] = "+++++++++??"
                
     #^CTRL    c.print("arama>arama> joinedListSozlukCoklu >>",EmptyLists.joinedListSozlukCoklu)
     
           
        
        
        
        
        
    return aramaParametresi


 """    