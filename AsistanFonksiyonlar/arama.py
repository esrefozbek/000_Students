 #£  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
#€  C:\Users\Markus\AppData\Roaming\Code\User\settings.json     
#?  C:\Users\Markus\AppData\Roaming\Code\User\settings.json     
#~   C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
#_  asdasdasdasdasda23423424242342                              
#** asddasdsadasadasdad2342342342342342                         

#breakpoint()

import  re    #. importlar
import copy
import VERI.mesajlar as MESAJLAR
import VERI.emptyLists as EMPTY_LISTS 
import MenuTablo.tablolarPY as TABLOLAR
import AnaFonksiyonlar.JSON_jobs as ANAMODUL
import AsistanFonksiyonlar.klavyeDinleme as KLAVYE_DINLE

from rich import print as p # ya da c.print kullanıyorsan onu bırak
from rich.text import Text
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console; c=Console()

def reset_altListe_birKriter():
    return [[] for _ in range(8)]



def bul_AnaFonksiyon(GirisMesaji:int):
    Cleaning()
    JSONdan_Import()    #!  her seferinde baştan yükleniyor İyi mi Kötü mü ???
    MESAJLAR.Mesajlar(GirisMesaji)
    kriter=InputwithESCAPE()
    if kriter is None:
        return None
    else:
        Parsing(kriter)  #! EmptyLists.ParsedSTRING_Listesi=[]  dolduruldu.
   #     BirlesikKriterBul(EMPTY_LISTS.parsedKriterler_Listesi, EMPTY_LISTS.Jsonda_Mevcut_Veriler)
        KriterBul(EMPTY_LISTS.parsedKriterler_Listesi, EMPTY_LISTS.Jsonda_Mevcut_Veriler) #.  Sonuç bulunursa Bulunanlar listesi doldurulur . 
        #KriterleriBul(EMPTY_LISTS.parsedKriterler_Listesi, EMPTY_LISTS.Jsonda_Mevcut_Veriler) #.  Sonuç bulunursa Bulunanlar listesi doldurulur . 
        # joinification(EMPTY_LISTS.altAnaListeTekler)
        # panelisation(EMPTY_LISTS.Joined_altAnaListeTekler)
        # TabloyaSozlukYap(EMPTY_LISTS.Joined_altAnaListeTekler)
      #  TABLOLAR.genel_TABLO(EMPTY_LISTS.Joined_TeklilerSozluk ) 
        #p("Arama>>AnaFonk:    EMPTY_LISTS.altAnaListeTum",EMPTY_LISTS.altAnaListeTum)
        #p("Arama>>AnaFonk:    EMPTY_LISTS.altAnaListeTekKriterler",EMPTY_LISTS.altAnaListeTekler)
        return kriter         
          
 
def KriterBul(kriterler:list, sozlukListesi:list=EMPTY_LISTS.Jsonda_Mevcut_Veriler):
    EMPTY_LISTS.altListe_birKriter = [[],[],[],[],[],[],[],[]]

    for birKriter in kriterler: 
        birKriter= birKriter.lower()
        # 🔻🔻🔻 Bulunanlar'ı temizle 🔻🔻🔻
        EMPTY_LISTS.TekKriterinBulunanlari.clear()
        CORE_Bul(birKriter,sozlukListesi)
        EMPTY_LISTS.TotalBulunanlar.extend(EMPTY_LISTS.TekKriterinBulunanlari)  #~Bu işime yaramaz bir veri, sanırım.
        
        TekeApend(EMPTY_LISTS.TekKriterinBulunanlari)
        kriteriEkle(birKriter)
        
        c.print("Arama >>>KriterBUL::  altListe_birKriter Silme öncesi >>",EMPTY_LISTS.altListe_birKriter,style="cyan")
        EMPTY_LISTS.altListe_CokKriter.append(EMPTY_LISTS.altListe_birKriter)

        EMPTY_LISTS.altListe_birKriter = reset_altListe_birKriter()
              
        
        
        c.print("Arama >>>KriterBUL::  altListe_birKriter Silme sonrası >>",EMPTY_LISTS.altListe_birKriter,style="cyan")
        
        p("\n[bold yellow]Arama>>KriterBul[/] : [bold red]altListe_CokKriter doluyor[/] >>>  ",EMPTY_LISTS.altListe_CokKriter)
    #    c.print("\n[bold yellow]Arama>>KriterBul[/] EMPTY_LISTS.TotalBulunanlar>>",EMPTY_LISTS.TotalBulunanlar,style="orchid")
    c.rule("KriterBul bitti",style="bold yellow1")
    


def TekeApend(TekKriterinBulunanlari:list):#. Bulunanlarda  ne varsa altListe_birKriter e döşer.  Bulunanlar srekli arttığı için 2. 3. kriterle birlikte bulunanalar artar ve tüm liste TekeApend edilir. Bu sebeple 2. ve sonrası listeler sürekli daha fazlalaşır. 
    for ogr in TekKriterinBulunanlari:
        
        for j,val in enumerate(ogr.values()):
            EMPTY_LISTS.altListe_birKriter[j].append(val)
          #  EMPTY_LISTS.altListe_Butun[j].append(val)
    c.rule("TekeApend bitti")




def BirlesikKriterBul(Kriterler,liste):
        EMPTY_LISTS.TekKriterinBulunanlari.clear()
                
        for i, kriter in enumerate(Kriterler):
            if i==0:
                liste=EMPTY_LISTS.Jsonda_Mevcut_Veriler    
            else:
                liste=EMPTY_LISTS.TekKriterinBulunanlari
                
            CORE_Bul(kriter,liste)
            liste=EMPTY_LISTS.TekKriterinBulunanlari
            
    

        c.print("\nArama>>BirleşikKriter:   Birleşik Bulunanlar:>>>",EMPTY_LISTS.Bulunanlar,style="magenta")        
  
    
   
   
def kriteriEkle(birKriter):
    EMPTY_LISTS.altListe_birKriter[-1]=[birKriter] #. kriter alt dikey listeye eklendi.
  #  EMPTY_LISTS.altListe_Butun[-1].append([birKriter])
  #  c.print("\n++++ EMPTY_LISTS.altAnaListeTek kriter   ++++", birKriter, EMPTY_LISTS.altListe_birKriter,style="turquoise2")
    
   

def CORE_Bul(birKriter,liste:list):
    for ogrenci in liste:
       if(birKriter is not None and birKriter!=""):
           if (birKriter == str(ogrenci["Id"]) or
               birKriter in ogrenci["ad"].lower() or
               birKriter in ogrenci["soyad"].lower()or
               birKriter == ogrenci["ogrenciNumarasi"] or
               birKriter == ogrenci["dogumTarihi"]  or 
               (len(birKriter)==4 and birKriter in ogrenci["dogumTarihi"]) or
               birKriter == (ogrenci["sinifi"].lower()) or                           
               (len(birKriter)==4 and birKriter == ogrenci["kayitTarihi"])): 
               EMPTY_LISTS.TekKriterinBulunanlari.append(ogrenci) 
               EMPTY_LISTS.BulunanAdSoyadIDler.append((ogrenci["Id"], ogrenci["ad"], ogrenci["soyad"])) 
           else: 
            continue
   # c.print(f"\n\nCORE>>>>>>> [yellow]birKriter[/] ve Bulunanlar >>> [yellow]{birKriter}[/]",EMPTY_LISTS.TekKriterinBulunanlari[:], style="bright_white")
    #if EMPTY_LISTS.Bulunanlar: 
    c.print("\n")
    c.rule("CORE bitti")
    return 

def Cleaning():
    EMPTY_LISTS.altListe_birKriter = reset_altListe_birKriter()
    EMPTY_LISTS.altListe_birKriter.clear() 
    EMPTY_LISTS.altListe_CokKriter=       []
    EMPTY_LISTS.altListe_Butun=          [[],[],[],[],[],[],[],[]]
    EMPTY_LISTS.Joined_altAnaListeTum=   [[],[],[],[],[],[],[],[]]
    
    EMPTY_LISTS.Joined_altAnaListeTekler.clear() 
    EMPTY_LISTS.Joined_altAnaListeTekler.clear() 
    
    EMPTY_LISTS.TekKriterinBulunanlari.clear()  #!j - Her sorguda önce temizle 
    EMPTY_LISTS.BulunanIDler.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    
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
    EMPTY_LISTS.parsedKriterler_Listesi=[]
    EMPTY_LISTS.parsedKriterler_Listesi = re.split(r'[,\s]+', kriterStringi) 
    #! Klavyeden girilenler temizlenip liste yapıldı. Boşluklar veya virgüller atıldı. 
     












     
     
"""    
def joinification(liste:list):
            EMPTY_LISTS.Joined_altAnaListeTekler= [["" for _ in range(len(liste[0]))] for _ in range(len(liste))]   
            for i,grup in enumerate(liste):
                for j,sutun  in enumerate(grup):      
                    EMPTY_LISTS.Joined_altAnaListeTekler[i][j]="\n".join(sutun)
        #.    p("\nArama>joynlama: EmptyLists.Joined_altAnaListeTekler  >> ",veriYolu.Joined_altAnaListeTekler)     

def panelisation(joinedLists):
        #    p("panel>>joinedLists >> ",joinedLists)
            icerikler = []
            renk=["yellow","orange1","green1","light_goldenrod2","dark_olive_green2","khaki1","dodger_blue2","green4"]
            basliklar=["kriter","Id","Ad","Soyad","No'su","Doğ Tarihi","Sınıf","Kayıt Tarihi"]
            
            print("🧪 basliklar:", len(basliklar))
            print("🧪 renk:", len(renk))
            print("🧪 Joined_altAnaListeTekler:", len(EMPTY_LISTS.Joined_altAnaListeTekler[0]))
            print("🧪 EMPTY_LISTS.altAnaListeTekler:", len(joinedLists[0]) if isinstance(joinedLists, list) else "veri liste değil")

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
 """
#.    p("Arama>>TabloyaSozluk: VERI.Joined_TeklilerSozluk ",VERI.Joined_TeklilerSozluk)
    

    
"""           
        for sozluk in EmptyLists.joinedListSozlukCoklu:
            for k, v in sozluk.items():
                if v.strip() == "":
                    sozluk[k] = "+++++++++??"
                
     #^CTRL    c.print("arama>arama> joinedListSozlukCoklu >>",EmptyLists.joinedListSozlukCoklu)
     
    return aramaParametresi

 """    
     
def KriterleriBul(parsedKriterStringi_Listesi:list, neredeAranacak:list=EMPTY_LISTS.Jsonda_Mevcut_Veriler):   
    kriterListesi=[]
    birOncekiToplam:int=0
    p("\n\n✈️📌 Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",len(EMPTY_LISTS.altListe_CokKriter)) 
    p("✈️📌📌 Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",EMPTY_LISTS.altListe_CokKriter) 
    
    #EMPTY_LISTS.altAnaListeBirCokKriterYanyana = [[[] for _ in range(len(EMPTY_LISTS.altAnaListeBirCokKriterYanyana))] for _ in range(len(parsedKriterStringi_Listesi))] #_ Boş 2 boyutlu liste oluşturuldu. (altAnaListeTekler[0] X parsedKriterStringi_Listesi)
    
    p("\n✈️  ✈️  Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",len(EMPTY_LISTS.altListe_CokKriter[0]),"X",len(parsedKriterStringi_Listesi)) 
    
    KriterBul(parsedKriterStringi_Listesi, neredeAranacak)  #_  
    
    p("\n✈️✈️ Arama>>kriterBul >> parsedKriterStringi_Listesi uzunluğu: >>", len(parsedKriterStringi_Listesi))
    p("✈️✈️ Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler uzunluğu: >>", len(EMPTY_LISTS.altListe_CokKriter[0]))
    p("⤵️arama>>kriterleriBul     EMPTY_LISTS.Bulunanlar>>",EMPTY_LISTS.TekKriterinBulunanlari)
    p("⤵️⤵️arama>>kriterleriBul     EMPTY_LISTS.BulunanAdSoyadIDler>>",EMPTY_LISTS.BulunanAdSoyadIDler)
    p("\n✈️✈️✈️    Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>", EMPTY_LISTS.altListe_CokKriter)
    
    p("\n");c.rule(" SONUÇLAR ",style="red") ;
                    