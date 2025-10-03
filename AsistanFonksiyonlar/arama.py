import  re    #. importlar
import copy
import string
import VERI.mesajlar as MESAJLAR
import VERI.emptyLists as E_LISTS 
import MenuTablo.tablolarPY as TABLOLAR
import AnaFonksiyonlar.JSON_jobs as JSON_
import AsistanFonksiyonlar.klavyeDinleme as KLAVYE_DINLE
import Widgetler.randomRenk as RR
from rich import print as p # ya da c.print kullanıyorsan onu bırak
from rich import box
from rich.text import Text
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align
from rich.console import Console,Group; c=Console()

def reset_altListe_birKriter():
    return [[] for _ in range(8)]

def CleanThem():
    E_LISTS.altListe_birKriter = reset_altListe_birKriter()
    E_LISTS.altListe_birKriter.clear() 
    E_LISTS.verticalsReadyForJoin=       []
    E_LISTS.altListe_Butun=          [[],[],[],[],[],[],[],[]]
    E_LISTS.Joined_altAnaListeTum=   [[],[],[],[],[],[],[],[]]
    
    E_LISTS.Joined_altAnaListeTekler.clear() 
    E_LISTS.Joined_altAnaListeTekler.clear() 
    
    E_LISTS.TekKriterinBulunanlari.clear()  #!j - Her sorguda önce temizle 
    
    E_LISTS.Jsonda_Mevcut_Veriler.clear()
    E_LISTS.TKB_Miktarlar.clear()


def bul_AnaFonksiyon(GirisMesaji:int):
    CleanThem()
    JSONdan_Import()                        #  her seferinde baştan yükleniyor İyi mi Kötü mü ???
    MESAJLAR.Mesajlar(GirisMesaji)
    klavye=InputwithESCAPE()
    if klavye is None:
        return None
    else:
        Parsing(klavye)  
        fonksiyon_secimi()
    return klavye         
          
 
def KriterleriAyriBul(kriterler:list, sozlukListesi:list=E_LISTS.Jsonda_Mevcut_Veriler):
    E_LISTS.TKB_Miktarlar=[]
    for birKriter in kriterler: 
        birKriter= birKriter.lower()
        # 🔻🔻🔻 TekKriterinBulunanlari'nı temizle 🔻🔻🔻
        E_LISTS.TekKriterinBulunanlari.clear()
        CORE_Bul(birKriter,sozlukListesi)
        E_LISTS.TotalBulunanlar.extend(E_LISTS.TekKriterinBulunanlari)  #~Bu işe yaramaz bir veri, sanırım.
        DikeyeGecis_TekKriter(E_LISTS.TekKriterinBulunanlari)
        DikeyeKriteriEkle(birKriter)
        E_LISTS.verticalsReadyForJoin.append(E_LISTS.altListe_birKriter)
        E_LISTS.altListe_birKriter = reset_altListe_birKriter()
       


def KriterleriBirlesikBul(Kriterler,liste):
    takas:list=[]
    E_LISTS.TKB_Miktarlar=[]
    for i, kriter in enumerate(Kriterler):
        if i!=0:
            E_LISTS.TekKriterinBulunanlari=[]
            liste=takas
        CORE_Bul(kriter,liste)
        takas=E_LISTS.TekKriterinBulunanlari
    #    c.print("Arama>>BirlesikKriterBul:: TekKriterinBulunanlari",EMPTY_LISTS.TekKriterinBulunanlari)
    E_LISTS.TotalBulunanlar.extend(E_LISTS.TekKriterinBulunanlari)  #~Bu işe yaramaz bir veri, sanırım. Buraya ne olur ne olmaz bulunsun diye ekledim.
    
    
    
    
    E_LISTS.TotalBulunanlar = list({tuple(sorted(d.items())): d for d in E_LISTS.TotalBulunanlar}.values())
    #c.print("Arama>>BirlesikKriterBul:: TotalBulunanlar",EMPTY_LISTS.TotalBulunanlar)    
    DikeyeGecis_TekKriter(E_LISTS.TekKriterinBulunanlari)
    DikeyeKriteriEkle(Kriterler)
    E_LISTS.verticalsReadyForJoin=[E_LISTS.altListe_birKriter] #. diğer yapı 3 katman   [[[]]]   şekklinde olduğu için  ve sonraki adımlara uyumluluk için 3 katman yaptım. 
    if E_LISTS.TKB_Miktarlar: E_LISTS.TKB_Miktarlar=[E_LISTS.TKB_Miktarlar[-1]]




def CORE_Bul(birKriter, liste: list):
    if not birKriter:  # None veya "" ise hiç uğraşma
        return
    
    birKriter = str(birKriter).lower().strip()  # arananı normalize et
    
    for ogrenci in liste:
        # Her alanı güvenli şekilde alıyoruz (None -> "")
        ogr_id     = str(ogrenci.get("Id") or "")
        ad         = (ogrenci.get("ad") or "").lower()
        soyad      = (ogrenci.get("soyad") or "").lower()
        numara     = str(ogrenci.get("ogrenciNumarasi") or "")
        dogum      = str(ogrenci.get("dogumTarihi") or "")
        sinif      = (ogrenci.get("sinifi") or "").lower()
        kayit      = str(ogrenci.get("kayitTarihi") or "")

        # Karşılaştırmalar
        if (
            birKriter == ogr_id or
            birKriter in ad or
            birKriter in soyad or
            birKriter == numara or
            birKriter == dogum or
            (len(birKriter) == 4 and birKriter in dogum) or
            birKriter == sinif or
            (len(birKriter) == 4 and birKriter == kayit)
        ):
            E_LISTS.TekKriterinBulunanlari.append(ogrenci)
#.Yatay
               
        else: 
            continue
    E_LISTS.TKB_Miktarlar.append(len(E_LISTS.TekKriterinBulunanlari)) 
    
  #  c.print("CORE>>  TekKriterinBulunanlari_Miktarlar >>", E_LISTS.TKB_Miktarlar, end="")
    #c.print("\n")
    return 

def DikeyeGecis_TekKriter(TekKriterinBulunanlari:list):
    for ogr in TekKriterinBulunanlari:
        for j,val in enumerate(ogr.values()):
            E_LISTS.altListe_birKriter[j+1].append(str(val))
            E_LISTS.altListe_Butun[j+1].append(str(val))
    

def DikeyeKriteriEkle(birKriter):
    E_LISTS.altListe_birKriter[0] = [birKriter] if isinstance(birKriter, str) else birKriter   #. kriter alt dikey listeye eklendi.
  

def joinification(liste:list):
            E_LISTS.Joined_altAnaListeTekler= [["" for _ in range(len(liste[0]))] for _ in range(len(liste))]   
            for i,grup in enumerate(liste):
                for j,sutun  in enumerate(grup):      
                    E_LISTS.Joined_altAnaListeTekler[i][j]="\n".join(sutun)



def panelisation(joinedLists):
            p("\n")
            icerikler = []
            renk=["bright_white","orange1","medium_purple1","light_goldenrod2","dark_olive_green2","khaki1","light_salmon1","grey70"]
            basliklar=["Kriter","Id","Ad","Soyad","No","Doğ. Tar.","Şube","Kayıt"]
            genislikler=[16,11,15,16,12,15,10,14]
            
            if E_LISTS.Joined_altAnaListeTekler: pass

            for j, joinedList in enumerate(joinedLists):
                paneller=[]
                sagPanel=[]
                solPanel=[]
                birRenkList=[]
                
                if joinedList[1]!="":
                    # uzunluk=iter(EMPTY_LISTS.TKB_Miktarlar)
                    # next(uzunluk)
                    for i,longString in enumerate(joinedList):
                        if i==0:
                            
                            if E_LISTS.TKB_Miktarlar:       #c.print("uzunluk✔️",E_LISTS.TKB_Miktarlar[j])
                                pass
                            
                            ust_panel = Panel(Text(longString, style="green",justify="center" ), title=basliklar[i], title_align="center",border_style=renk[i], box=box.SQUARE,)
                            alt_panel = Panel(Text(str(E_LISTS.TKB_Miktarlar[j]), style="yellow",justify="center", ), title="Adet",title_align="center", border_style=renk[i],  box=box.SQUARE,)

                            # İki paneli grupla
                            solPanel = Panel.fit(
                                Group(ust_panel, alt_panel),  # içeriğe panelleri alt alta koyduk
                               # title="Panel 0", 
                               #subtitle="Eşref",
                                border_style="bright_yellow",
                                width=16,
                                height=9 if E_LISTS.TKB_Miktarlar[j]<6  else  E_LISTS.TKB_Miktarlar[j]+4         ,
                                box=box.SIMPLE,   
                                  
                            )
                        else:
                            birRenk=RR.randomRENK()
                            birRenkList.append(birRenk)
                            
                            c.print(f"[{birRenk}]-{birRenk}--  [/]",end="")
                            birRenk=str(birRenk)
                            pan=(Panel(Text(longString, style=f"{birRenk}",justify="center"), title=basliklar[i], border_style=birRenk, width=genislikler[i],box=box.SQUARE  ))
                            sagPanel.append(pan)  
                            
                    
                    sagPanel=Panel(Columns(sagPanel,expand=False,title=""),title="",
                            subtitle_align="left",   border_style="white", width=104, height=9 if E_LISTS.TKB_Miktarlar[j]<5 else None,box=box.SIMPLE)
                    sagPanel=Align.left(sagPanel)
                    
                    paneller=[sagPanel,solPanel ]
                    paneller=Columns(paneller,expand=False,column_first=False,title="",align="left",)
                    panel=Panel(paneller,title="", title_align="right", border_style="bright_yellow",box=box.HORIZONTALS,width=125)
                    p("\n")
                    p(panel)
                    
                    # Başarı mesajı
    
"""                             
                    icerikler.append(panel)
                    
#           luzumsuzCevre=Panel(Group(*icerikler),title="Dış Panel100",border_style="orange1")
            luzumsuzCevre=(Group(*icerikler))
#            p(Panel(luzumsuzCevre,title="Dış Panel 1", width=124 ,style=" ", box=box.SQUARE,border_style="deep_pink2" ),end="\n")
            p(luzumsuzCevre,end="\n")
            c.rule("Panel sonuçlar yukarıda verildi", style="magenta", align="right")
            
              
               """
              
              
def TabloyaSozlukYap(liste):
    basliklar = ["kriter", "Id", "ad", "soyad", "ogrenciNumarasi", "dogumTarihi", "sinifi", "kayitTarihi"]
    E_LISTS.Joined_TeklilerSozluk = []
    for item in liste:
        sozluk = {}
        for j in range(len(item)):
            sozluk[basliklar[j]] = item[j]  #_ key:value yapıdı. 
        E_LISTS.Joined_TeklilerSozluk.append(sozluk)
#.    p("Arama>>TabloyaSozluk: VERI.Joined_TeklilerSozluk ",VERI.Joined_TeklilerSozluk)
    
def fonksiyon_secimi():
    from InquirerPy import inquirer
    
    E_LISTS.verticalsReadyForJoin.clear()
    E_LISTS.TekKriterinBulunanlari=[]
    E_LISTS.TotalBulunanlar=[]
    E_LISTS.altListe_birKriter = [[],[],[],[],[],[],[],[]]
    c.print("\n")
    secimler = inquirer.checkbox(
        message="Hangi fonksiyon(lar) çalıştırılsın?",
        instruction="(Space ile seç, Enter ile devam et)",
        choices=[
            {"name": "💛 Ayrık Kriter", "value": "tekli", "enabled": False},
            {"name": "🌟 Birlesik Kriter", "value": "birlesik", "enabled": False},
            {"name": "📊 Tablo Sonuç", "value": "tablo", "enabled": True , "disabled": "Pasif"},
            {"name": "✈️ Panel Sonuç", "value": "panel", "enabled": True},
        ],
        transformer=lambda result: ", ".join(result) if result else "Hiçbir şey seçilmedi.",
    ).execute()
  #  c.print("\n")
  
    if not secimler:
        print("⚠️ Hiçbir fonksiyon seçilmedi!")
        return 

    if "birlesik" in secimler:
        KriterleriBirlesikBul(E_LISTS.KellesiGidenler_Listesi, E_LISTS.Jsonda_Mevcut_Veriler)

    if "tekli" in secimler:
        KriterleriAyriBul(E_LISTS.KellesiGidenler_Listesi, E_LISTS.Jsonda_Mevcut_Veriler)

    if "panel" in secimler:
        joinification(E_LISTS.verticalsReadyForJoin)
        panelisation(E_LISTS.Joined_altAnaListeTekler)
        
    if "tablo" in secimler:
        joinification(E_LISTS.verticalsReadyForJoin)
        TabloyaSozlukYap(E_LISTS.Joined_altAnaListeTekler)
        TABLOLAR.genel_TABLO_kriterli(E_LISTS.Joined_TeklilerSozluk )
    
     
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
            c.print("\n<< \" \" Hiçbir değer girmeden [red on green] Enter [/] tuşuna bastın Beni boşuna oyalama dostum, gazabım kötüdür",style="bright_yellow")
            continue

        else:    
            kriter=str(kriterStringi).strip().lower()         
            return kriterStringi

def Parsing(kriterStringi):
    kriterStringi=kriterStringi or ""
    E_LISTS.KellesiGidenler_Listesi=[]
    E_LISTS.KellesiGidenler_Listesi = re.split(r'[,\s]+', kriterStringi) 
    #! Klavyeden girilenler temizlenip liste yapıldı. Boşluklar veya virgüller atıldı. 

     
def KriterleriBul(parsedKriterStringi_Listesi:list, neredeAranacak:list=E_LISTS.Jsonda_Mevcut_Veriler):   
    kriterListesi=[]
    birOncekiToplam:int=0
    p("\n\n✈️📌 Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",len(E_LISTS.verticalsReadyForJoin)) 
    p("✈️📌📌 Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",E_LISTS.verticalsReadyForJoin) 
    
    #EMPTY_LISTS.altAnaListeBirCokKriterYanyana = [[[] for _ in range(len(EMPTY_LISTS.altAnaListeBirCokKriterYanyana))] for _ in range(len(parsedKriterStringi_Listesi))] #_ Boş 2 boyutlu liste oluşturuldu. (altAnaListeTekler[0] X parsedKriterStringi_Listesi)
    
    p("\n✈️  ✈️  Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",len(E_LISTS.verticalsReadyForJoin[0]),"X",len(parsedKriterStringi_Listesi)) 
    
    KriterleriAyriBul(parsedKriterStringi_Listesi, neredeAranacak)  #_  
    
    p("\n✈️✈️ Arama>>kriterBul >> parsedKriterStringi_Listesi uzunluğu: >>", len(parsedKriterStringi_Listesi))
    p("✈️✈️ Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler uzunluğu: >>", len(E_LISTS.verticalsReadyForJoin[0]))
    p("⤵️arama>>kriterleriBul     EMPTY_LISTS.Bulunanlar>>",E_LISTS.TekKriterinBulunanlari)
    p("⤵️⤵️arama>>kriterleriBul     EMPTY_LISTS.BulunanAdSoyadIDler>>",)
    p("\n✈️✈️✈️    Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>", E_LISTS.verticalsReadyForJoin)
    
    p("\n");c.rule(" SONUÇLAR ",style="red") ;
                    