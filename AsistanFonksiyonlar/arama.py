import  re    #. importlar
import copy
import string
import VERI.mesajlar as MESAJLAR
import VERI.emptyLists as EMPTY_LISTS 
import MenuTablo.tablolarPY as TABLOLAR
import AnaFonksiyonlar.JSON_jobs as JSON_
import AsistanFonksiyonlar.klavyeDinleme as KLAVYE_DINLE
from rich import print as p # ya da c.print kullanıyorsan onu bırak
from rich.text import Text
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console; c=Console()

def reset_altListe_birKriter():
    return [[] for _ in range(8)]

def Cleaning():
    EMPTY_LISTS.altListe_birKriter = reset_altListe_birKriter()
    EMPTY_LISTS.altListe_birKriter.clear() 
    EMPTY_LISTS.verticalsReadyForJoin=       []
    EMPTY_LISTS.altListe_Butun=          [[],[],[],[],[],[],[],[]]
    EMPTY_LISTS.Joined_altAnaListeTum=   [[],[],[],[],[],[],[],[]]
    
    EMPTY_LISTS.Joined_altAnaListeTekler.clear() 
    EMPTY_LISTS.Joined_altAnaListeTekler.clear() 
    
    EMPTY_LISTS.TekKriterinBulunanlari.clear()  #!j - Her sorguda önce temizle 
    EMPTY_LISTS.BulunanIDler.clear()
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()



def bul_AnaFonksiyon(GirisMesaji:int):
    Cleaning()
    JSONdan_Import()                        #  her seferinde baştan yükleniyor İyi mi Kötü mü ???
    MESAJLAR.Mesajlar(GirisMesaji)
    klavye=InputwithESCAPE()
    if klavye is None:
        return None
    else:
        Parsing(klavye)  
        fonksiyon_secimi()
    return klavye         
          
 
def KriterleriAyriBul(kriterler:list, sozlukListesi:list=EMPTY_LISTS.Jsonda_Mevcut_Veriler):
   
    for birKriter in kriterler: 
        birKriter= birKriter.lower()
        # 🔻🔻🔻 TekKriterinBulunanlari'nı temizle 🔻🔻🔻
        EMPTY_LISTS.TekKriterinBulunanlari.clear()
        CORE_Bul(birKriter,sozlukListesi)
        EMPTY_LISTS.TotalBulunanlar.extend(EMPTY_LISTS.TekKriterinBulunanlari)  #~Bu işe yaramaz bir veri, sanırım.
        DikeyeGecis_TekKriter(EMPTY_LISTS.TekKriterinBulunanlari)
        DikeyeKriteriEkle(birKriter)
        EMPTY_LISTS.verticalsReadyForJoin.append(EMPTY_LISTS.altListe_birKriter)
        EMPTY_LISTS.altListe_birKriter = reset_altListe_birKriter()
       


def KriterleriBirlesikBul(Kriterler,liste):
    takas:list=[]
    for i, kriter in enumerate(Kriterler):
        if i!=0:
            EMPTY_LISTS.TekKriterinBulunanlari=[]
            liste=takas
        CORE_Bul(kriter,liste)
        takas=EMPTY_LISTS.TekKriterinBulunanlari
    #    c.print("Arama>>BirlesikKriterBul:: TekKriterinBulunanlari",EMPTY_LISTS.TekKriterinBulunanlari)
    EMPTY_LISTS.TotalBulunanlar.extend(EMPTY_LISTS.TekKriterinBulunanlari)  #~Bu işe yaramaz bir veri, sanırım. Buraya ne olur ne olmaz bulunsun diye ekledim.
    
    EMPTY_LISTS.TotalBulunanlar = list({tuple(sorted(d.items())): d for d in EMPTY_LISTS.TotalBulunanlar}.values())
    #c.print("Arama>>BirlesikKriterBul:: TotalBulunanlar",EMPTY_LISTS.TotalBulunanlar)    
    DikeyeGecis_TekKriter(EMPTY_LISTS.TekKriterinBulunanlari)
    DikeyeKriteriEkle(Kriterler)
    EMPTY_LISTS.verticalsReadyForJoin=[EMPTY_LISTS.altListe_birKriter] #. diğer yapı 3 katman   [[[]]]   şekklinde olduğu için  ve sonraki adımlara uyumluluk için 3 katman yaptım. 




def CORE_Bul(birKriter,liste:list):
    for ogrenci in liste:
       if(birKriter is not None and birKriter!=""):
           if (birKriter == str(ogrenci["Id"]) or
               birKriter in ogrenci["ad"].lower() or
               birKriter in ogrenci["soyad"].lower()or
               birKriter == ogrenci["ogrenciNumarasi"] or
               birKriter == ogrenci["dogumTarihi"]  or 
               (len(birKriter)==4 and birKriter in ogrenci["dogumTarihi"]) or
               birKriter == ((ogrenci["sinifi"]).lower() or  (ogrenci["sinifi"])) or                      
               (len(birKriter)==4 and birKriter == ogrenci["kayitTarihi"])): 
               EMPTY_LISTS.TekKriterinBulunanlari.append(ogrenci) #.Yatay
               
           else: 
            continue
    
   
   # c.print(f"\n\nCORE>>>>>>> [yellow]birKriter[/] ve Bulunanlar >>> [yellow]{birKriter}[/]",EMPTY_LISTS.TekKriterinBulunanlari[:], style="bright_white")
    #if EMPTY_LISTS.Bulunanlar: 
    c.print("\n")
    #c.rule("CORE bitti")
    return 

def DikeyeGecis_TekKriter(TekKriterinBulunanlari:list):
    for ogr in TekKriterinBulunanlari:
        for j,val in enumerate(ogr.values()):
            EMPTY_LISTS.altListe_birKriter[j+1].append(str(val))
            EMPTY_LISTS.altListe_Butun[j+1].append(str(val))
    

def DikeyeKriteriEkle(birKriter):
    EMPTY_LISTS.altListe_birKriter[0] = [birKriter] if isinstance(birKriter, str) else birKriter   #. kriter alt dikey listeye eklendi.
  

def joinification(liste:list):
            EMPTY_LISTS.Joined_altAnaListeTekler= [["" for _ in range(len(liste[0]))] for _ in range(len(liste))]   
            for i,grup in enumerate(liste):
                for j,sutun  in enumerate(grup):      
                    EMPTY_LISTS.Joined_altAnaListeTekler[i][j]="\n".join(sutun)

def panelisation(joinedLists):
            icerikler = []
            renk=["yellow","orange1","green1","light_goldenrod2","dark_olive_green2","khaki1","dodger_blue2","green4"]
            basliklar=["kriter","Id","Ad","Soyad","No'su","Doğ Tarihi","Sınıf","Kayıt Tarihi"]
            
            if EMPTY_LISTS.Joined_altAnaListeTekler: pass

            for j, joinedList in enumerate(joinedLists):
                paneller=[]
                if joinedList[1]!="":
                    for i,longString in enumerate(joinedList):
                        pan=(Panel.fit(Text(longString, style="grey35"), title=basliklar[i], border_style=renk[i]))
                        paneller.append(pan)
                    icerikler.append(Panel.fit(Columns(paneller), title="başlık ", border_style="grey15"))
            col=Columns(icerikler)
            p(col,end="\n")
            c.rule("Panel sonuçlar yukarıda verildi", style="green_yellow")
              
def TabloyaSozlukYap(liste):
    basliklar = ["kriter", "Id", "ad", "soyad", "ogrenciNumarasi", "dogumTarihi", "sinifi", "kayitTarihi"]
    EMPTY_LISTS.Joined_TeklilerSozluk = []
    for item in liste:
        sozluk = {}
        for j in range(len(item)):
            sozluk[basliklar[j]] = item[j]  #_ key:value yapıdı. 
        EMPTY_LISTS.Joined_TeklilerSozluk.append(sozluk)
#.    p("Arama>>TabloyaSozluk: VERI.Joined_TeklilerSozluk ",VERI.Joined_TeklilerSozluk)
    
def fonksiyon_secimi():
    from InquirerPy import inquirer
    
    EMPTY_LISTS.verticalsReadyForJoin.clear()
    EMPTY_LISTS.TekKriterinBulunanlari=[]
    EMPTY_LISTS.TotalBulunanlar=[]
    EMPTY_LISTS.altListe_birKriter = [[],[],[],[],[],[],[],[]]
    
    secimler = inquirer.checkbox(
        message="Hangi fonksiyon(lar) çalıştırılsın?",
        instruction="(Boşluk ile seç, Enter ile devam et)",
        choices=[
            {"name": "🧠 Tümünü Seç", "value": "all", "enabled": False},  # özel kontrol için
            {"name": "🔹 Ayrık Kriter", "value": "tekli", "enabled": True},
            {"name": "🔸 Birlesik Kriter", "value": "birlesik", "enabled": False},
            {"name": "📊 Tablo Sonuç", "value": "tablo", "enabled": False, "disabled": "Pasif"},
            {"name": "📋 Panel Sonuç", "value": "panel", "enabled": True},
        ],
        transformer=lambda result: ", ".join(result) if result else "Hiçbir şey seçilmedi.",
    ).execute()

    # "Tümünü Seç" seçildiyse tüm aktif seçenekleri uygula
    if "all" in secimler:
        secimler = ["tekli", "birlesik","tablo", "panel"]  # "tablo" devre dışı olduğu için eklenmedi

    if not secimler:
        print("⚠️ Hiçbir fonksiyon seçilmedi!")
        return 

    if "birlesik" in secimler:
        KriterleriBirlesikBul(EMPTY_LISTS.KellesiGidenler_Listesi, EMPTY_LISTS.Jsonda_Mevcut_Veriler)

    if "tekli" in secimler:
        KriterleriAyriBul(EMPTY_LISTS.KellesiGidenler_Listesi, EMPTY_LISTS.Jsonda_Mevcut_Veriler)

    if "panel" in secimler:
        joinification(EMPTY_LISTS.verticalsReadyForJoin)
        panelisation(EMPTY_LISTS.Joined_altAnaListeTekler)
        
    if "tablo" in secimler:
        joinification(EMPTY_LISTS.verticalsReadyForJoin)
        TabloyaSozlukYap(EMPTY_LISTS.Joined_altAnaListeTekler)
        TABLOLAR.genel_TABLO(EMPTY_LISTS.Joined_TeklilerSozluk )  
   
"""           
        for sozluk in EmptyLists.joinedListSozlukCoklu:
            for k, v in sozluk.items():
                if v.strip() == "":
                    sozluk[k] = "+++++++++??"
                
     #^CTRL    c.print("arama>arama> joinedListSozlukCoklu >>",EmptyLists.joinedListSozlukCoklu)
     
    return aramaParametresi

 """    

def Cleaning():
    EMPTY_LISTS.altListe_birKriter = reset_altListe_birKriter()
    EMPTY_LISTS.altListe_birKriter.clear() 
    EMPTY_LISTS.verticalsReadyForJoin=       []
    EMPTY_LISTS.altListe_Butun=          [[],[],[],[],[],[],[],[]]
    EMPTY_LISTS.Joined_altAnaListeTum=   [[],[],[],[],[],[],[],[]]
    
    EMPTY_LISTS.Joined_altAnaListeTekler.clear() 
    EMPTY_LISTS.Joined_altAnaListeTekler.clear() 
    
    EMPTY_LISTS.TekKriterinBulunanlari.clear()  #!j - Her sorguda önce temizle 
   
    EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
    
def JSONdan_Import():
    JSON_.JSONdanImport()  

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
    EMPTY_LISTS.KellesiGidenler_Listesi=[]
    EMPTY_LISTS.KellesiGidenler_Listesi = re.split(r'[,\s]+', kriterStringi) 
    #! Klavyeden girilenler temizlenip liste yapıldı. Boşluklar veya virgüller atıldı. 



     
def KriterleriBul(parsedKriterStringi_Listesi:list, neredeAranacak:list=EMPTY_LISTS.Jsonda_Mevcut_Veriler):   
    kriterListesi=[]
    birOncekiToplam:int=0
    p("\n\n✈️📌 Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",len(EMPTY_LISTS.verticalsReadyForJoin)) 
    p("✈️📌📌 Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",EMPTY_LISTS.verticalsReadyForJoin) 
    
    #EMPTY_LISTS.altAnaListeBirCokKriterYanyana = [[[] for _ in range(len(EMPTY_LISTS.altAnaListeBirCokKriterYanyana))] for _ in range(len(parsedKriterStringi_Listesi))] #_ Boş 2 boyutlu liste oluşturuldu. (altAnaListeTekler[0] X parsedKriterStringi_Listesi)
    
    p("\n✈️  ✈️  Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",len(EMPTY_LISTS.verticalsReadyForJoin[0]),"X",len(parsedKriterStringi_Listesi)) 
    
    KriterleriAyriBul(parsedKriterStringi_Listesi, neredeAranacak)  #_  
    
    p("\n✈️✈️ Arama>>kriterBul >> parsedKriterStringi_Listesi uzunluğu: >>", len(parsedKriterStringi_Listesi))
    p("✈️✈️ Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler uzunluğu: >>", len(EMPTY_LISTS.verticalsReadyForJoin[0]))
    p("⤵️arama>>kriterleriBul     EMPTY_LISTS.Bulunanlar>>",EMPTY_LISTS.TekKriterinBulunanlari)
    p("⤵️⤵️arama>>kriterleriBul     EMPTY_LISTS.BulunanAdSoyadIDler>>",)
    p("\n✈️✈️✈️    Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>", EMPTY_LISTS.verticalsReadyForJoin)
    
    p("\n");c.rule(" SONUÇLAR ",style="red") ;
                    