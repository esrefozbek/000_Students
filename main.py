
#breakpoint()

import sys,os
from rich.live import Live
from rich.box import Box
from rich.console import Console; c = Console()
import readchar
import time
from AsistanFonksiyonlar.klavyeDinleme import ENTER
import MenuTablo.canlıTablo as Canlı_Tablo
import AsistanFonksiyonlar.dilimleme as Dilimleme
import VERI.emptyLists as VERIModul
import AnaFonksiyonlar.yeniOgrenci_KAYIT as YeniOgr_KAYIT
import AnaFonksiyonlar.ogrenci_LiSTEleme as Ogr_List
import AnaFonksiyonlar.JSON_jobs as AnaModul
import MenuTablo.menu as Menu
import AnaFonksiyonlar.ogrenci_SiLME as Ogr_SiL
import AsistanFonksiyonlar.sırfSORGU as sırfSORGU
import Widgetler.SayacAnimasyon.sayacKronometre as Say_Kro
import Widgetler.SayacAnimasyon.geriSayar as Geri_Sayar
import MenuTablo.teknikMenü as Tek_Menü
import AsistanFonksiyonlar.arama as Arama
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as AsistanModul
import AsistanFonksiyonlar.klavyeDinleme as klavDinle
#import Widgetler.SayacAnimasyon.spinner as spinnerPY

#breakpoint()
#^########################################menu.ekranTemizle()

def anamenü_bekletme(scnd):
    with Live(refresh_per_second=2) as live:
        for i in range(scnd, 0, -1):
            live.update(f"[cyan]⏳ Anamenü açılıyor... {i}[/]")
            time.sleep(1)

def startPoint():
        VERIModul.SilinenlerinTupleliListesi_.clear()
        VERIModul.YeniEklenenlerinSozluklerListesi_.clear()
       
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
                        c.print( "❗❗❗❗❗❗❗[bold bright white] Düzgün bir sayı gir ENTER ile devam et[/]❗❗❗❗❗❗", style="blink", end="")
                        input()
                        continue
                   
                        
                    
                    
                    if CHOOSEN == 1:#NOTE - YENİ KAYIT
                       #^ breakpoint()
                        YeniOgr_KAYIT.yeniOgrenciKayidi()



                    elif CHOOSEN==2:#NOTE - BUL
                        if not VERIModul.SilinenlerinTupleliListesi_:
                            AnaModul.JSONdanYükleme_()
                            while True:
                                a=Arama.aramaParametresi()
                                if a is not None:
                                    a=a.strip().lower()
                                    if a == "":
                                        c.print("Hiçbir değer girmeden [italic white]Enter[/] tuşuna bastın Beni boşuna oyalama dostum",style="yellow")
                                    else:    
                                        Arama.arama(a)
                                else :
                                    break
                      
                        VERIModul.SilinenlerinTupleliListesi_.clear()
                        Geri_Sayar.GeriSayar(2,"Ana menüye dönülecek (2 saniye)...")
                        #pomodoro.pomodoro_dongusu()
                       

                    elif CHOOSEN ==3: #NOTE -  SİL
                        # if not VERİ.TupleliListe_:
                        # else:
                        
                        Ogr_SiL.ogrenciSil()
                        klavDinle.Enter_ile_devam_et()

                    elif CHOOSEN==4:  #NOTE -  ÇIKIŞ
                        print("Çıkılıyor. Görüşmek üzere!")
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
                        VERIModul.SilinenlerinTupleliListesi_.clear()
                        VERIModul.YeniEklenenlerinSozluklerListesi_.clear()
                        continue
   
                       
                    elif CHOOSEN==6: #NOTE - editleme
                        Canlı_Tablo.main()
                        Say_Kro.geri_say(3)
                        
                    elif CHOOSEN == 7: #NOTE -  DİLİMLEME         #Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
                      
                        VERIModul.value=20
                        değer=VERIModul.value
                        Menu.ekranTemizle()
                        AnaModul.JSONdanYükleme_()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if VERIModul.SilinenlerinTupleliListesi_:
                            Ogr_List.altAltaOgrenciListesi(değer)
                            VERIModul.SilinenlerinTupleliListesi_.clear()
                        else:
                            c.print("📭 Liste boş. Önce öğrenci gir.",style="white")
                        Say_Kro.progress_sayac()

                    elif CHOOSEN==77:#NOTE -  DİLİMLEME
                
                        VERIModul.value=500
                        değer=VERIModul.value
                        Menu.ekranTemizle()
                        AnaModul.JSONdanYükleme_()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if VERIModul.SilinenlerinTupleliListesi_:
                            Ogr_List.altAltaOgrenciListesi(değer)
                           #^######                                  Canlı_Tablo.main()    
                            VERIModul.SilinenlerinTupleliListesi_.clear()
                        else:
                            c.print("📭 Liste boş. Önce öğrenci gir.", style="blink")
                      #FIXME -   menü.rastgele_box_stili
                            ENTER()
                        #FIXME - startPoint()
                    
                       
                    elif CHOOSEN==44:
                       anamenü_bekletme(2)
                       break

                       
                       
                       
#? SECTION TEKNİK MENÜ 
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
                        AnaModul.JSONdanYükleme_()
                        Say_Kro.geri_say(3)
                       
                        
                        
                    elif selected == 4:
                        c.print("\n[bold]VERİ.TupleliListe_:[/bold]",VERIModul.SilinenlerinTupleliListesi_)
                        ENTER()
           
                    elif selected== 5:
                        AsistanModul.TupleyiSözlükYap(VERIModul.SilinenlerinTupleliListesi_)
                      
                        #NOTE - Hangi tuple var, ilk kayıttaki mi , jsondan gelip remove edilmiş olan mı, 
                        klavDinle.Enter_ile_devam_et()

                    elif selected==6:
                        menüTipi="sözlüklüListe"
                        listeTipi="sözlüklüListe"
                        if VERIModul.YeniEklenenlerinSozluklerListesi_:
                            c.print("\nVERİ.SözlüklüListe_:",style="green")
                            for i in VERIModul.YeniEklenenlerinSozluklerListesi_:
                                    c.print(i)
                                    
                        else:
                            print( "Henüz Öğrenci Kaydı girilmedi. ")
                        klavDinle.Enter_ile_devam_et()
                        

                    elif selected==7:
                        menüTipi="tupleliListe"
                        listeTipi="tupleliListe"
                        VERIModul.SilinenlerinTupleliListesi_.sort()
                            
                        c.print(f"\n[ {len(VERIModul.SilinenlerinTupleliListesi_)} TALEBE bulundu ]",style=" white")
                        c.print("[magenta]VERİ.TupleliListe_:[/magenta]",VERIModul.SilinenlerinTupleliListesi_)
                        if VERIModul.YeniEklenenlerinSozluklerListesi_:
                           # for sözlük in sözlüklüListe:
                                c.print("\n",VERIModul.YeniEklenenlerinSozluklerListesi_,"\n",style="bold")
                        else:
                            print( "SözlüklüListe_de Öğrenci Kaydı yok. ")
                        klavDinle.Enter_ile_devam_et()

                    elif selected==8:
                        Say_Kro.geri_say(3)
                        
                    
                    elif selected==9:
                        VERIModul.SilinenlerinTupleliListesi_.clear()
                        if VERIModul.SilinenlerinTupleliListesi_:
                            print("Tupleli liste dolu")
                            ENTER()
                        else:
                            print("Tupleli liste  BOŞŞŞ şuanda.")
                        ENTER()
                    
                    elif selected==10:
                        VERIModul.YeniEklenenlerinSozluklerListesi_.clear()

                        # ekran temizlenir anaMenüye gidilir Lakin silinen eklenen listeleri doludur.
                        
                    elif selected==11:
                        Dilimleme.dilimleme(5,VERIModul.SilinenlerinTupleliListesi_)                        
                        #ANCHOR - console.input("\n🔁 Devam etmek için ENTER'a basın..." )
                    
                    elif selected==12:
                        sırfSORGU._SırfSorgu_()
                                       
                        
                    elif selected==13:  #NOTE - renk paleti
                        c.print("[bold underline]256 Renk Paleti[/]\n")
                        for i in range(0, 256, 16):
                            line = " ".join(f"[on color({j})]{j:3}[/]" for j in range(i, i + 16))
                            c.print(line)
                        klavDinle.Enter_ile_devam_et()
                    
                    elif selected==33:
                        startPoint()

                        
  


if __name__ == "__main__":
            startPoint()