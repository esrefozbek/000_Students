 #_ Evet Hayır onayı nerede ????                                                      
#~  3 Silmeye girince bilgilendirme kısmında son eklenen Id numaraları gelsin !!!!!!!!
#~  silme fonksiyonneleştirlmeli Okunurluğu artırılmalı.                              
 #€  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
 #?  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
 #_  asdasdasdasdasda23423424242342                             
 #£  C:\Users\Markus\AppData\Roaming\Code\User\settings.json    
 #~   C:\Users\Markus\AppData\Roaming\Code\User\settings.json   
 #** asddasdsadasadasdad2342342342342342                        
 #/ dsafsddfsfdsfsfdsdfsfsfdsfsfdsdfsfsfsdfsdfsfsfds            
 #= asdsadasdasdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa          

# breakpoint()
from rich.panel import Panel
from rich import print
from rich.layout import Layout

import sys,os
from rich.live import Live
from rich.box import Box
from rich import box
from rich.table import Table
from rich.console import Console; c = Console()
import readchar
import time
import VERI.emptyLists as EMPTY_LISTS

import AnaFonksiyonlar.yeniOgrenci_KAYIT as YeniOgr_KAYIT
import AnaFonksiyonlar.ogrenci_LiSTEleme as Ogr_List
import AnaFonksiyonlar.JSON_jobs as ANAMODUL
import AnaFonksiyonlar.ogrenci_SiLME as Ogr_SiL

import Widgetler.SayacAnimasyon.sayacKronometre as Say_Kro

import MenuTablo.canlıTablo as Canlı_Tablo
import MenuTablo.teknikMenü as Tek_Menü
import MenuTablo.menu as Menu
import MenuTablo.tablolarPY as TABLOLAR

from AsistanFonksiyonlar.klavyeDinleme import ENTER
import AsistanFonksiyonlar.dilimleme as Dilimleme
import AsistanFonksiyonlar.sırfSORGU as sırfSORGU
import AsistanFonksiyonlar.arama as Arama
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as AsistanModul
import AsistanFonksiyonlar.klavyeDinleme as KLAVYE_DINLE
#import Widgetler.SayacAnimasyon.spinner as spinnerPY

#^########################################menu.ekranTemizle()

def anamenü_bekletme(scnd):
    with Live(refresh_per_second=2) as live:
        for i in range(scnd, 0, -1):
            live.update(f"[cyan]⏳ Anamenü açılıyor...yaşaşınnnn {i}[/]")
            time.sleep(4)

def startPoint():
        EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
        EMPTY_LISTS.FARK_SozlukListesi.clear()

#? SECTION ANAMENÜ
        while True:  #Menüden seçim
            
                    Menu.menu_goster()
                    #REVIEW - JSON._JSONdanYükleme_()
                    try:
                        from rich.prompt import Prompt
                        #name = Prompt.ask("Enter your name") 
                        #name = Prompt.ask("Enter your name", default="Paul Atreides") 
                        
                       # name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")
                        
                        # from rich.prompt import Confirm
                        # is_rich_great = Confirm.ask("Do you like rich?")
                        # assert is_rich_great
                        
                        c.print("[bold white]  SANA ZAHMET BİR [yellow][blink]SEÇİM[/][/] YAP:[/bold white]", style="link https://google.com",end=" ")
                        
                        CHOOSEN = int(input())
                    except ValueError:
                        c.print( "⚠️  Lütfen sadece sayı girin.ENTER ile devam et",style="" )
                        input()
                        continue
                    
                    if CHOOSEN not in (1,2,3,4,5,6,7,77,44):
                        c.print( ":warning: [bold bright white] Düzgün bir sayı gir ENTER ile devam et[/] :warning:", style="blink", end="")
                        input()
                        continue
                   
                    
                    
                    if CHOOSEN == 1:#NOTE - YENİ KAYIT
                        EMPTY_LISTS.ekle=True
                        YeniOgr_KAYIT.yeniOgrenciKayidi()
                        EMPTY_LISTS.ekle=False
                        
                        

                    elif CHOOSEN==2:#NOTE - BUL
                        EMPTY_LISTS.bul=True      
                        while True:
                            sonuc=Arama.bul_AnaFonksiyon(1)  #! Bulunanlar listesine dolum yapılır,
                            if sonuc is None:
                                break
                        EMPTY_LISTS.bul=False      
                        
                            
                            
                        """   if EmptyLists.joinedListSozlukCoklu:
                                TablolarPY.genel_TABLO(EmptyLists.joinedListSozlukCoklu)
                                
                                
                            c.print("main> ",EmptyLists.Joined_altAnaListeTeklilerSozluk)
                            c.rule("Bölüm 1",style="red1",characters="=",align="right") """
                            
                           
                           
                            # # from rich.console import Console
                            # from rich.markdown import Markdown
                            # markdown = Markdown("""
                            # # Heading
                            # ## Subheading
                            # - Bullet point
                            # - Another bullet point
                            # """)

                            # c.print(markdown)
                            
                            
                            # # from rich.syntax import Syntax
                            # # code = '''
                            # # def hello_world():
                            # #     print("Hello, world!")
                            # # '''
                            
                            # # syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
                            # # c.print(syntax)
                                   
                                                     
                            # from rich import print

                            # print([1, 2, 3]) # highlights lists
                            # print({"a": 1}) # highlights dicts
                            # print((1,2,3)) # highlights tuples


                            # # from rich import inspect
                            # # import pandas as pd

                            # # df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})  
                            # # inspect(df)
                            
                            
                            # from rich.tree import Tree

                            # tree = Tree("Directory")
                            # tree.add("Folder 1")
                            # tree.add("Folder 2")
                            # tree.add("Folder 3")

                            # print(tree)
                            
                            
                            
                            # # #!/usr/bin/python

                         
                            # c.rule('Python', style='blue')
                            # c.print('''Python is a general-purpose, dynamic, object-oriented\
                            # programming language. The design purpose of the Python language\
                            # emphasizes programmer productivity and code readability.''')
                            # c.print()

                            # c.rule('F#', style='red')
                            # c.print('''F# is a universal programming language for writing succinct,\
                            # robust and performant code.''')
                            # c.print()

                            # c.rule('Go')
                            # c.print('''Go is an open source programming language that makes it easy to\
                            # build simple, reliable, and efficient software. Go is a statically\
                            # typed, compiled programming language.''')



                            # from rich.text import Text
                            # txt = Text('''Python is a general-purpose, dynamic, object-oriented \
                            # programming language. The design purpose of the Python language \
                            # emphasizes programmer productivity and code readability.''', style='italic')

                         
                            # c.print(txt)
                            
                            # # #!/usr/bin/python

                            # # from rich.console import Console
                            # from rich.columns import Columns
                            # from rich.panel import Panel

                            # # console = Console()

                            # with open('VERI/words.txt', 'r') as f:
                            #     words = f.readlines()

                            #     c.print(Columns([Panel(line, border_style='blue')
                            #                 for line in words], align='center'))

                            
                            
                            
                            
                            # #!/usr/bin/python

                            # from rich import print
                            # from rich.console import group
                            # from rich.panel import Panel

                            # @group()
                            # def get_panels():
                            #     yield Panel.fit("an old falcon", style="on blue")
                            #     yield Panel.fit("a long stormy night", style="on deep_sky_blue4")

                            # print(Panel.fit(get_panels()))

                            # from rich.console import Group

                            # g = Group(
                            #     Panel.fit("an old falcon", style="on blue"),
                            #     Panel.fit("a long stormy night", style="on deep_sky_blue4"),
                            # )

                            # print(Panel.fit(g))

        
        
                    elif CHOOSEN ==3: #NOTE -  SİL
                        # if not VERİ.TupleliListe_:
                        # else:
                        while True:
                            Ogr_SiL.Silme_AnaFonksiyon()
                            EMPTY_LISTS.sil=True
                         
                        EMPTY_LISTS.sil=False
                        ENTER()
        
        

                    elif CHOOSEN==4:  #NOTE -  ÇIKIŞ
                        c.print("Çıkılıyor. Görüşmek üzere!")
                        #JSON.JSONaKayıt("öğrenciler.json",VERİ.SözlüklüListe_)
                        #VERİ.SözlüklüListe_.clear()
                        c.print("""\n[bold ]Bak cidden çıkıyorum [bold yellow]emin misin[/]
[bold white]Vazgeçmek istersen [bold green]Esc[/]'ye bas [/bold white]
[bold orange]İlla çıkman gerekiyorsa [bold green ]ENTER[/]'a bas [/bold orange]""")
                                            
                        key = readchar.readkey()
                        if key == readchar.key.ESC:
                            startPoint()

                        elif key == '\r':  # ENTER
                           sys.exit("çıkıyorum..................................")

                        
                    elif CHOOSEN==5: #NOTE - Ekranı resEtleme
                      #^  sayacKronometre.geri_say(1)
                      #  spinnerPY.dene_spinner() 
                        anamenü_bekletme(3)
                        EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
                        EMPTY_LISTS.FARK_SozlukListesi.clear()
                        continue
   
                       
                    elif CHOOSEN==6: #NOTE - editleme
                        Canlı_Tablo.main()
                        Say_Kro.geri_say(3)
                        
                        
                    elif CHOOSEN == 7: #NOTE -  DİLİMLEME         #Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
                      
                        EMPTY_LISTS.value=25
                        değer=EMPTY_LISTS.value
                        Menu.ekranTemizle()
                        ANAMODUL.JSONdanImport()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if EMPTY_LISTS.Jsonda_Mevcut_Veriler:
                            Ogr_List.altAltaOgrenciListesi(değer)
                            EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
                        else:
                            c.print("📭 Liste boş. Önce öğrenci gir.",style="white")
                        Say_Kro.progress_sayac()

                    elif CHOOSEN==77:#NOTE -  DİLİMLEME
                        EMPTY_LISTS.value=500
                        değer=EMPTY_LISTS.value
                       #! Menu.ekranTemizle()
                        ANAMODUL.JSONdanImport()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if EMPTY_LISTS.Jsonda_Mevcut_Veriler:
                            Ogr_List.altAltaOgrenciListesi(değer)
                           #&   Canlı_Tablo.main()    
                            EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
                        else:
                            c.print("📭 Liste boş. Önce öğrenci gir.", style="blink")
                      #FIXME -   menü.rastgele_box_stili
                            ENTER()
                        #FIXME - startPoint()

                       
                    elif CHOOSEN==44:
                       anamenü_bekletme(2)
                       break

                       
#~                                         SECTION TEKNİK MENÜ                                     
        while True:                
                    Tek_Menü.teknikMenü()
                    try:
                        c.print("🟢 [bold white]SANA ZAHMET BİR SEÇİM YAP:[/bold white]", style="blink",end=" ")
                        selected = int(input())
                    except ValueError:
                        c.print( "⚠️  Lütfen sadece sayı girin.",style="" )
                        input("ENTER ile devam et...")
                        continue
                    

                    if selected not in (0,1,2,3,4,5,6,7,8,9,10,11,12, 13,33):
                        c.print( "❗❗❗❗❗❗❗ Düzgün bir sayı gir ❗❗❗❗❗❗", style="blink")
                        input("ENTER ile devam et...")
                        continue      
                    
                    
                    elif selected == 0:
                        c.print("Veri.SozlukluListe_ >> ",Ogr_List.yeniOgrListesiSözlükDökümü())
                        ENTER()
                        

                    elif selected == 1:
                        c.print("Veri.SozlukluListe_ >> ",Ogr_List.yeniOgrListesiDökümü())
                        ENTER()

                    elif selected == 2:
                        Ogr_List.silinmişKayıtlılarListesiDökümü() 
                        ENTER()

                        
                    elif selected == 3: 
                        ANAMODUL.JSONdanImport()
                        Say_Kro.geri_say(3)
                       
                        
                        
                    elif selected == 4:
                        c.print("\n[bold]VERİ.TupleliListe_:[/bold]",EMPTY_LISTS.Jsonda_Mevcut_Veriler)
                        ENTER()
           
                    elif selected== 5:
                        AsistanModul.TupleyiSözlükListesineEkle(EMPTY_LISTS.Jsonda_Mevcut_Veriler)
                      
                        #NOTE - Hangi tuple var, ilk kayıttaki mi , jsondan gelip remove edilmiş olan mı, 
                        KLAVYE_DINLE.Enter_ile_devam_et()

                    elif selected==6:
                        menuTipi="sözlüklüListe"
                        listeTipi="sözlüklüListe"
                        if EMPTY_LISTS.FARK_SozlukListesi:
                            c.print("\nVERİ.SözlüklüListe_:",style="green")
                            for i in EMPTY_LISTS.FARK_SozlukListesi:
                                    c.print(i)
                                    
                        else:
                            c.print( "Henüz Öğrenci Kaydı girilmedi. ")
                        KLAVYE_DINLE.Enter_ile_devam_et()
                        

                    elif selected==7:
                        menuTipi="tupleliListe"
                        listeTipi="tupleliListe"
                        EMPTY_LISTS.Jsonda_Mevcut_Veriler.sort()
                            
                        c.print(f"\n[ {len(EMPTY_LISTS.Jsonda_Mevcut_Veriler)} TALEBE bulundu ]",style=" white")
                        c.print("[magenta]VERİ.TupleliListe_:[/magenta]",EMPTY_LISTS.Jsonda_Mevcut_Veriler)
                        if EMPTY_LISTS.FARK_SozlukListesi:
                           # for sözlük in sözlüklüListe:
                                c.print("\n",EMPTY_LISTS.FARK_SozlukListesi,"\n",style="bold")
                        else:
                            c.print( "SözlüklüListe_de Öğrenci Kaydı yok. ")
                        KLAVYE_DINLE.Enter_ile_devam_et()

                    elif selected==8:
                        Say_Kro.geri_say(3)
                        
                    
                    elif selected==9:
                        EMPTY_LISTS.Jsonda_Mevcut_Veriler.clear()
                        if EMPTY_LISTS.Jsonda_Mevcut_Veriler:
                            c.print("Tupleli liste dolu")
                            ENTER()
                        else:
                            c.print("Tupleli liste  BOŞŞŞ şuanda.")
                        ENTER()
                    
                    elif selected==10:
                        EMPTY_LISTS.FARK_SozlukListesi.clear()

                        # ekran temizlenir anaMenüye gidilir Lakin silinen eklenen listeleri doludur.
                        
                    elif selected==11:
                        Dilimleme.dilimleme(5,EMPTY_LISTS.Jsonda_Mevcut_Veriler)                        
                        #ANCHOR - console.input("\n🔁 Devam etmek için ENTER'a basın..." )
                    
                    elif selected==12:
                        sırfSORGU._SırfSorgu_()
                                       
                        
                    elif selected==13:  #NOTE - renk paleti
                        c.print("[bold underline]256 Renk Paleti[/]\n")
                        for i in range(0, 256, 16):
                            line = " ".join(f"[on color({j})]{j:3}[/]" for j in range(i, i + 16))
                            c.print(line)
                        KLAVYE_DINLE.Enter_ile_devam_et()
                    
                    elif selected==33:
                        startPoint()

                        
  


if __name__ == "__main__":
            startPoint()