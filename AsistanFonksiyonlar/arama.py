import  re    #. importlar
import copy
import string
import VERI.mesajlar as MESAJLAR
import VERI.emptyLists as EMPTY 
import MenuTablo.tablolarPY as TABLO
import AnaFonksiyonlar.JSON_jobs as JSON_
import AsistanFonksiyonlar.klavyeDinleme as KLAVYE_DINLE
import Widgetler.randomRenk as RENK
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
    EMPTY.altListe_birKriter = reset_altListe_birKriter()
    EMPTY.altListe_birKriter.clear() 
    EMPTY.verticalsReadyForJoin=       []
    EMPTY.altListe_Butun=          [[],[],[],[],[],[],[],[]]
    EMPTY.Joined_altAnaListeTum=   [[],[],[],[],[],[],[],[]]
    
    EMPTY.Joined_altAnaListeTekler.clear() 
    EMPTY.Joined_altAnaListeTekler.clear() 
    
    EMPTY.TekKriterinBulunanlari.clear()  #!j - Her sorguda önce temizle 
    
    EMPTY.Jsonda_Mevcut_Veriler.clear()
    EMPTY.TKB_Miktarlar.clear()


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
          
 
def KriterleriAyriBul(kriterler:list, sozlukListesi:list=EMPTY.Jsonda_Mevcut_Veriler):
    EMPTY.TKB_Miktarlar=[]
    for birKriter in kriterler: 
        birKriter= birKriter.lower()
        # 🔻🔻🔻 TekKriterinBulunanlari'nı temizle 🔻🔻🔻
        EMPTY.TekKriterinBulunanlari.clear()
        CORE_Bul(birKriter,sozlukListesi)
        EMPTY.TotalBulunanlar.extend(EMPTY.TekKriterinBulunanlari)  #~Bu işe yaramaz bir veri, sanırım.
        DikeyeGecis_TekKriter(EMPTY.TekKriterinBulunanlari)
        DikeyeKriteriEkle(birKriter)
        EMPTY.verticalsReadyForJoin.append(EMPTY.altListe_birKriter)
        EMPTY.altListe_birKriter = reset_altListe_birKriter()
       


def KriterleriBirlesikBul(Kriterler,liste):
    takas:list=[]
    EMPTY.TKB_Miktarlar=[]
    for i, kriter in enumerate(Kriterler):
        if i!=0:
            EMPTY.TekKriterinBulunanlari=[]
            liste=takas
        CORE_Bul(kriter,liste)
        takas=EMPTY.TekKriterinBulunanlari
    #    c.print("Arama>>BirlesikKriterBul:: TekKriterinBulunanlari",EMPTY_LISTS.TekKriterinBulunanlari)
    EMPTY.TotalBulunanlar.extend(EMPTY.TekKriterinBulunanlari)  #~Bu işe yaramaz bir veri, sanırım. Buraya ne olur ne olmaz bulunsun diye ekledim.
    
    
    
    
    EMPTY.TotalBulunanlar = list({tuple(sorted(d.items())): d for d in EMPTY.TotalBulunanlar}.values())
    #c.print("Arama>>BirlesikKriterBul:: TotalBulunanlar",EMPTY_LISTS.TotalBulunanlar)    
    DikeyeGecis_TekKriter(EMPTY.TekKriterinBulunanlari)
    DikeyeKriteriEkle(Kriterler)
    EMPTY.verticalsReadyForJoin=[EMPTY.altListe_birKriter] #. diğer yapı 3 katman   [[[]]]   şekklinde olduğu için  ve sonraki adımlara uyumluluk için 3 katman yaptım. 
    if EMPTY.TKB_Miktarlar: EMPTY.TKB_Miktarlar=[EMPTY.TKB_Miktarlar[-1]]




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
            EMPTY.TekKriterinBulunanlari.append(ogrenci)
#.Yatay
               
        else: 
            continue
    EMPTY.TKB_Miktarlar.append(len(EMPTY.TekKriterinBulunanlari)) 
    
  #  c.print("CORE>>  TekKriterinBulunanlari_Miktarlar >>", E_LISTS.TKB_Miktarlar, end="")
    #c.print("\n")
    return 

def DikeyeGecis_TekKriter(TekKriterinBulunanlari:list):
    for ogr in TekKriterinBulunanlari:
        for j,val in enumerate(ogr.values()):
            EMPTY.altListe_birKriter[j+1].append(str(val))
            EMPTY.altListe_Butun[j+1].append(str(val))
    

def DikeyeKriteriEkle(birKriter):
    EMPTY.altListe_birKriter[0] = [birKriter] if isinstance(birKriter, str) else birKriter   #. kriter alt dikey listeye eklendi.
  

def joinification(liste:list):
            EMPTY.Joined_altAnaListeTekler= [["" for _ in range(len(liste[0]))] for _ in range(len(liste))]   
            for i,grup in enumerate(liste):
                for j,sutun  in enumerate(grup):      
                    EMPTY.Joined_altAnaListeTekler[i][j]="\n".join(sutun)


def panelisation(joinedLists):
            c.rule("PANEL SONUÇLARI",style="orange_red1",align="right")
    #        p("\n")
            icerikler = []
            renk=["bright_white","orange1","medium_purple1","light_goldenrod2","dark_olive_green2","khaki1","light_salmon1","grey70"]
            basliklar=["🔎","Id","Ad","Soyad","No","Doğ. Tar.","Şube","Kayıt"]
            genislikler=[17,11,15,16,12,15,10,14]
            
            if EMPTY.Joined_altAnaListeTekler: pass

            for j, joinedList in enumerate(joinedLists):
                paneller=[]
                sagPanel=[]
                solPanel=[]
                birRenkList=[]
                
                if joinedList[1]!="":
                    # uzunluk=iter(EMPTY_LISTS.TKB_Miktarlar)
                    # next(uzunluk)
    #                c.print("\n")
                    for i,longString in enumerate(joinedList):
                        if i==0:
                            
                            if EMPTY.TKB_Miktarlar:       #c.print("uzunluk✔️",E_LISTS.TKB_Miktarlar[j])
                                pass
                            
                            ust_panel = Panel(
                                Text(longString,
                                    style=f"{RENK.randomRENK()}",
                                    justify="center"),
                                title=basliklar[i],
                                title_align="center",
                                border_style=f"{RENK.randomRENK()}",
                                box=box.ROUNDED,)
                            
                            alt_panel = Panel(
                                Text(str(EMPTY.TKB_Miktarlar[j]),
                                    style=f"{RENK.randomRENK()}",
                                    justify="center"),
                                title="Adet",
                                title_align="center",
                                border_style=f"{RENK.randomRENK()}",
                                box=box.ROUNDED,)

                            # İki paneli grupla
                            sagPanel = Panel.fit(
                                Group(ust_panel, alt_panel),  # içeriğe panelleri alt alta koyduk
                                title="GÖT", 
                                subtitle="",
                                border_style=f"{RENK.randomRENK()}",
                                width=14,
                                height=9 if EMPTY.TKB_Miktarlar[j]<6  else  EMPTY.TKB_Miktarlar[j]+4,
                                style=f"on {RENK.randomRENK()}",
                                box=box.ROUNDED)
                            sagPanel=Align.right(sagPanel)
                            
                        else:  #.    SAĞ PANEL
                            birRenk=RENK.randomRENK()
                            birRenkList.append(birRenk)
                            
    #                        c.print(f"  [{birRenk}]{birRenk}  [/]",)
                          #  birRenk=str(birRenk)
                            pan=(Panel(Text(longString, style=f"{RENK.randomRENK()}",justify="center"), title=f"[{RENK.randomRENK()}]{basliklar[i]}[/]", border_style=RENK.randomRENK(), width=genislikler[i],box=box.SQUARE  ))
                            solPanel.append(pan)  
                    c.print("\nbirRenkList >> ",birRenkList,end="")
                            
                    
                    solPanel=Panel.fit(
                                       Columns(solPanel,expand=False,title=""),
                                       title="",
                                       subtitle_align="left",
                                       border_style=f"{RENK.randomRENK()}",
                                       width=104, height=9 if EMPTY.TKB_Miktarlar[j]<5 else None,
                                       
                                       box=box.SQUARE)
                    
                    paneller=[sagPanel,solPanel]
                    
                    kolonlar=Columns(paneller,
                                     expand=False,
                                     column_first=False,
                                     align="left")
                    kolonPaneli=Panel(kolonlar,
                                      title="",
                                      title_align="right",
                                      border_style=f"{RENK.randomRENK()}",
                                      box=box.SQUARE,
                                      style="none",
                                      width=125,
                                      ) # buradaki panel gizli. simple box ile çerçeveledim.
                    kolonPaneli=Align.center(kolonPaneli)
                    
                    outer_panel=Panel(kolonPaneli,
                                      subtitle="outer panel",
                                      subtitle_align="right",
                                      border_style=f"{RENK.randomRENK()}",
                                      box=box.HORIZONTALS,
                                      #style=f"on {RR.randomRENK()}",
                                      width=130)
                    
                    outer_panel=Align.left(outer_panel)
                    
                    
                    #""  c.print(*[renk_kutusu(color) for color in birRenkList], end="") 
                    # c.print("\n")
                    # c.print(Group(*[renk_kutusu(color) for color in birRenkList]))
                   # c.print("\n")
                    # c.print(Panel(Columns([renk_kutusu(renk) for renk in birRenkList])), ) 
                    c.print(renk_teksti(birRenkList))
                   # c.print("\n")
                    c.print(Columns([renk_kutusu(renk) for renk in birRenkList]))  
                    c.print("\n")
                    #c.print(renk_kolonu(birRenkList))     #. HATALI !!!!!  kolon molon değil bu.
                    c.print(outer_panel)
            c.print("\n")


# Tek bir renk kutusu
def renk_kutusu(Renk: str):
    pan = Panel.fit(
        f"[{RENK.randomRENK()}]{Renk}[/]",               # iç yazı
       # title=f"[{RR.randomRENK()}]{Renk}[/]",          # panel başlığı
       style=f" on {Renk}",           # arka plan rengi
       border_style=f"{RENK.randomRENK()}",                  # border rengi artık değişken
        box=box.SIMPLE,)
    return pan

# Renkleri dikey kolon şeklinde panel                   !!!!!! HATALI !!!!!!
def renk_kolonu(renkListesi: list[str]):
    kolonlar = [Text(f"{renk}\n", style=renk) for renk in renkListesi]
    panelim = Panel.fit(
        Columns(kolonlar, align="left"),
        title="[bold yellow]Renkler[/]",
        border_style="cyan")
    return panelim

# Renkleri alt alta yazı şeklinde panel
def renk_teksti(colorsList: list[str]):
    
    txt = Text()
    for i, color in enumerate(colorsList):
        txt.append(f"{color}\n" if i<len(colorsList)-1 else f"{color}", style=color)

    panelim = Panel.fit(
        txt,
     #   title="[bold yellow]Renkler[/]",
        border_style=f"{RENK.randomRENK()}" )
    return panelim

        
def TabloyaSozlukYap(liste):
    basliklar = ["kriter", "Id", "ad", "soyad", "ogrenciNumarasi", "dogumTarihi", "sinifi", "kayitTarihi"]
    EMPTY.Joined_TeklilerSozluk = []
    for item in liste:
        sozluk = {}
        for j in range(len(item)):
            sozluk[basliklar[j]] = item[j]  #_ key:value yapıdı. 
        EMPTY.Joined_TeklilerSozluk.append(sozluk)
#.    p("Arama>>TabloyaSozluk: VERI.Joined_TeklilerSozluk ",VERI.Joined_TeklilerSozluk)
    
def fonksiyon_secimi():
    from InquirerPy import inquirer
    
    EMPTY.verticalsReadyForJoin.clear()
    EMPTY.TekKriterinBulunanlari=[]
    EMPTY.TotalBulunanlar=[]
    EMPTY.altListe_birKriter = [[],[],[],[],[],[],[],[]]
    c.print("\n")
    secimler = inquirer.checkbox(
        message="Hangi fonksiyon(lar) çalıştırılsın?",
        instruction="(Space ile seç, Enter ile devam et)",
        choices=[
            {"name": "✈️ Panel Sonuç", "value": "panel", "enabled": True},
            {"name": "📊 Tablo Sonuç", "value": "tablo", "enabled": True , "disabled": "Pasif"},
            {"name": "💛 Ayrık Kriter", "value": "tekli", "enabled": True},
            {"name": "🌟 Birlesik Kriter", "value": "birlesik", "enabled": False},
        ],
        transformer=lambda result: ", ".join(result) if result else "Hiçbir şey seçilmedi.",
    ).execute()
  
    if not secimler:
        print("⚠️ Hiçbir fonksiyon seçilmedi!")
        return 

    if "birlesik" in secimler:
        KriterleriBirlesikBul(EMPTY.KellesiGidenlerin_Listesi, EMPTY.Jsonda_Mevcut_Veriler)

    if "tekli" in secimler:
        KriterleriAyriBul(EMPTY.KellesiGidenlerin_Listesi, EMPTY.Jsonda_Mevcut_Veriler)

    if "panel" in secimler:
        joinification(EMPTY.verticalsReadyForJoin)
        panelisation(EMPTY.Joined_altAnaListeTekler)
        
    if "tablo" in secimler:
        joinification(EMPTY.verticalsReadyForJoin)
        TabloyaSozlukYap(EMPTY.Joined_altAnaListeTekler)
        TABLO.sagSolTablo(TABLO.genel_TABLO(EMPTY.Joined_TeklilerSozluk),EMPTY.Joined_TeklilerSozluk )
       
    
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
            MESAJLAR.Mesajlar(11)
            continue

        else:    
            kriter=str(kriterStringi).strip().lower()         
            return kriterStringi

def Parsing(kriterStringi):
    kriterStringi=kriterStringi or ""
    EMPTY.KellesiGidenlerin_Listesi=[]
    EMPTY.KellesiGidenlerin_Listesi = re.split(r'[,\s]+', kriterStringi) 
    #! Klavyeden girilenler temizlenip liste yapıldı. Boşluklar veya virgüller atıldı. 

     
def KriterleriBul(parsedKriterStringi_Listesi:list, neredeAranacak:list=EMPTY.Jsonda_Mevcut_Veriler):   
    kriterListesi=[]
    birOncekiToplam:int=0
    p("\n\n✈️📌 Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",len(EMPTY.verticalsReadyForJoin)) 
    p("✈️📌📌 Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",EMPTY.verticalsReadyForJoin) 
    
    #EMPTY_LISTS.altAnaListeBirCokKriterYanyana = [[[] for _ in range(len(EMPTY_LISTS.altAnaListeBirCokKriterYanyana))] for _ in range(len(parsedKriterStringi_Listesi))] #_ Boş 2 boyutlu liste oluşturuldu. (altAnaListeTekler[0] X parsedKriterStringi_Listesi)
    
    p("\n✈️  ✈️  Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>",len(EMPTY.verticalsReadyForJoin[0]),"X",len(parsedKriterStringi_Listesi)) 
    
    KriterleriAyriBul(parsedKriterStringi_Listesi, neredeAranacak)  #_  
    
    p("\n✈️✈️ Arama>>kriterBul >> parsedKriterStringi_Listesi uzunluğu: >>", len(parsedKriterStringi_Listesi))
    p("✈️✈️ Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler uzunluğu: >>", len(EMPTY.verticalsReadyForJoin[0]))
    p("⤵️arama>>kriterleriBul     EMPTY_LISTS.Bulunanlar>>",EMPTY.TekKriterinBulunanlari)
    p("⤵️⤵️arama>>kriterleriBul     EMPTY_LISTS.BulunanAdSoyadIDler>>",)
    p("\n✈️✈️✈️    Arama>>kriterBul >> EMPTY_LISTS.altAnaListeTekler  >>", EMPTY.verticalsReadyForJoin)
    
    p("\n");c.rule(" SONUÇLAR ",style="red") ;
                    