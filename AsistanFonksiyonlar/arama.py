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


EMPTY_LISTS.Bulunanlar=[]   #! boş bir sözlükler listesi.
kriterStringi=""




def Cleaning():


    EMPTY_LISTS.Joined_altAnaListeTekler=[]
    EMPTY_LISTS.Joined_altAnaListeTumKriterli=[]
    EMPTY_LISTS.altAnaListeTeklerKritersiz=[]
    EMPTY_LISTS.altAnaListeTeklerKritersiz=      [[],[],[],[],[],[],[]]
    EMPTY_LISTS.altAnaListeTeklerKriterli=[]
    EMPTY_LISTS.altAnaListeTeklerKriterli=       [[],[],[],[],[],[],[],[]]
    EMPTY_LISTS.altAnaListeTumKriterli=[]
    EMPTY_LISTS.altAnaListeTumKriterli=                  [[],[],[],[],[],[],[],[]]
    EMPTY_LISTS.altAnaListeTumKritersiz= []
    EMPTY_LISTS.altAnaListeTumKritersiz=                  [[],[],[],[],[],[],[]]
    
    EMPTY_LISTS.Joined_altAnaListeTekler.clear() 
    EMPTY_LISTS.Joined_altAnaListeTeklerKriterli.clear() 
    
    EMPTY_LISTS.Joined_altAnaListeTumKritersiz=   [[],[],[],[],[],[],[]]
    EMPTY_LISTS.Joined_altAnaListeTumKriterli=    [[],[],[],[],[],[],[],[]]
    
    EMPTY_LISTS.Bulunanlar.clear()  #!j - Her sorguda önce temizle 
    EMPTY_LISTS.BulunanIDler.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler=[]  #! Temizlik imandandır
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()



def bul_AnaFonksiyon(GirisMesaji:int):
        
        Cleaning()
        JSONdan_Import()    #!  her seferinde baştan yükleniyor İyi mi Kötü mü ???
        MESAJLAR.Mesajlar(GirisMesaji)
        kriter=InputwithESCAPE()
        if kriter is None:
            return None
        else:
            Parsing(kriter)  #! EmptyLists.ParsedSTRING_Listesi=[]  dolduruldu.
            KriterleriBul(EMPTY_LISTS.parsedKriterStringi_Listesi) #/  Sonuç bulunursa Bulunanlar listesi doldurulur . 
            joinification(EMPTY_LISTS.altAnaListeTeklerKriterli)
            panelisation(EMPTY_LISTS.Joined_altAnaListeTekler)
            TabloyaSozlukYap(EMPTY_LISTS.Joined_altAnaListeTekler)
            TABLOLAR.genel_TABLO(EMPTY_LISTS.Joined_TeklilerSozluk, ) 
            return kriter         
          


    
def JSONdan_Import():
    ANAMODUL.JSONdanImport()  



def InputwithESCAPE():
    global kriterStringi
    while True:
        
        kriterStringi=KLAVYE_DINLE.KlavyeDinle()
        if kriterStringi is  None:
          #  SAYAC.spinner(4,3)
            return None    
        elif kriterStringi == "":
            c.print("<< \"  \" Hiçbir değer girmeden [red on green] Enter [/] tuşuna bastın Beni boşuna oyalama dostum, gazabım kötüdür",style="bright_yellow")
            continue
        else:    
            kriter=str(kriterStringi).strip().lower()         
            return kriterStringi




def Parsing(kriterStringi):
    kriterStringi=kriterStringi or ""
    EMPTY_LISTS.parsedKriterStringi_Listesi=[]
    EMPTY_LISTS.parsedKriterStringi_Listesi = re.split(r'[,\s]+', kriterStringi) 
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
#/    p("\nArama>joynlama: EmptyLists.Joined_altAnaListeTekler  >> ",veriYolu.Joined_altAnaListeTekler)     

def panelisation(joinedLists):
#    p("panel>>joinedLists >> ",joinedLists)
    icerikler = []
    renk=["yellow","orange1","green1","light_goldenrod2","dark_olive_green2","khaki1","dodger_blue2","green4"]
    basliklar=["kriter","Id","Ad","Soyad","No'su","Doğ Tarihi","Sınıf","Kayıt Tarihi"]
    
    for j, joinedList in enumerate(joinedLists):
        paneller=[]
        if joinedList[1]!="":
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

#/    p("Arama>>TabloyaSozluk: VERI.Joined_TeklilerSozluk ",VERI.Joined_TeklilerSozluk)
    

    
"""
        
         
        
 


                    
                                        
                      
        for sozluk in EmptyLists.joinedListSozlukCoklu:
            for k, v in sozluk.items():
                if v.strip() == "":
                    sozluk[k] = "+++++++++??"
                
     #^CTRL    c.print("arama>arama> joinedListSozlukCoklu >>",EmptyLists.joinedListSozlukCoklu)
     
           
        
        
        
        
        
    return aramaParametresi


 """    