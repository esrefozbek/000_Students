
#^     breakpoint()

import sys,os
import MenuTablo.canlıTablo as CanlıTablo 
from AsistanFonksiyonlar.klavyeDinleme import ENTER
from rich.live import Live
from rich.box import Box
import AsistanFonksiyonlar.dilimleme as Dilimleme, VERI.veri as Veri, AnaFonksiyonlar.yeniOgrenci_KAYIT as yeniOgrenci_KAYIT, AnaFonksiyonlar.ogrenci_LiSTEleme as oglis, AnaFonksiyonlar.JSON as Json, MenuTablo.menu as Menu, AnaFonksiyonlar.ogrenci_SiLME as ogrenci_SiLME,   readchar, AsistanFonksiyonlar.sırfSORGU as sırfSORGU, time,Widgetler.SayacAnimasyon.sayacKronometre as Sayac_Kronometre,Widgetler.SayacAnimasyon.geriSayar as Geri_Sayar,MenuTablo.teknikMenü as teknikMenü,AsistanFonksiyonlar.arama as Arama
from rich.console import Console; c = Console()
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as tupSoz
import AsistanFonksiyonlar.klavyeDinleme as klavDinle


#^########################################menu.ekranTemizle()

def anamenü_bekletme(scnd):
    with Live(refresh_per_second=2) as live:
        for i in range(scnd, 0, -1):
            live.update(f"[cyan]⏳ Anamenü açılıyor... {i}[/]")
            time.sleep(1)

def startPoint():
        Veri.TupleliListe_.clear()
        Veri.SozlukluListe_.clear()
       
                                                                #!SECTION ANAMENÜ
        while True:  #Menüden seçim
            
                    Menu.menu_goster()
                    #REVIEW - JSON._JSONdanYükleme_()
                    try:
                        c.print("🟢 [bold white]SANA ZAHMET BİR SEÇİM YAP:[/bold white]", style="blink",end=" ")
                        CHOOSEN = int(input())
                    except ValueError:
                        c.print( "⚠️  Lütfen sadece sayı girin.ENTER ile devam et",style="" )
                        input()
                        continue
                    
                    if CHOOSEN not in (1,2,3,4,5,6,7,77,33):
                        c.print( "❗❗❗❗❗❗❗[bold bright white] Düzgün bir sayı gir ENTER ile devam et[/]❗❗❗❗❗❗", style="blink")
                        input()
                        continue
                   
                        
                    
                    
                    if CHOOSEN == 1:#NOTE - YENİ KAYIT
                        yeniOgrenci_KAYIT.yeniOgrenciKayidi()



                    elif CHOOSEN==2:#NOTE - BUL
                        if not Veri.TupleliListe_:
                            Json.JSONdanYükleme_()
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
                      
                        Veri.TupleliListe_.clear()
                        Geri_Sayar.GeriSayar(2,"Ana menüye dönülecek (2 saniye)...")
                        #pomodoro.pomodoro_dongusu()
                       

                    elif CHOOSEN ==3: #NOTE -  SİL
                        # if not VERİ.TupleliListe_:
                        # else:
                        Json.JSONdanYükleme_()   
                        print( "❗ Liste boş, silinecek öğrenci yok.")
                        ogrenci_SiLME.ogrenciSil()
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
                        anamenü_bekletme(1)
                        Veri.TupleliListe_.clear()
                        Veri.SozlukluListe_.clear()
                        continue
                    
                        
   
   
   
                       
                    elif CHOOSEN==6: #NOTE - editleme
                        CanlıTablo.main()
                        Sayac_Kronometre.geri_say(3)
                        
                    elif CHOOSEN == 7: #NOTE -  DİLİMLEME         #Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
                      
                        Veri.value=20
                        değer=Veri.value
                        Menu.ekranTemizle()
                        Json.JSONdanYükleme_()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if Veri.TupleliListe_:
                            oglis.altAltaOgrenciListesi(değer)
                            Veri.TupleliListe_.clear()
                        else:
                            c.print("📭 Liste boş. Önce öğrenci gir.",style="white")
                        Sayac_Kronometre.progress_sayac()

                    elif CHOOSEN==77:#NOTE -  DİLİMLEME
                
                        Veri.value=30
                        değer=Veri.value
                        Menu.ekranTemizle()
                        Json.JSONdanYükleme_()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if Veri.TupleliListe_:
                            oglis.altAltaOgrenciListesi(değer)
                            CanlıTablo.main()    
                            Veri.TupleliListe_.clear()
                        else:
                            c.print("📭 Liste boş. Önce öğrenci gir.", style="blink")
                      #FIXME -   menü.rastgele_box_stili
                            ENTER()
                        #FIXME - startPoint()
                    
                       
                    elif CHOOSEN==33:
                       anamenü_bekletme(2)
                       break

                       
                       
                       
                                                                           #!SECTION TEKNNİK MENÜ          
        while True:                
                    teknikMenü.teknikMenü()
                    try:
                        c.print("🟢 [bold white]SANA ZAHMET BİR SEÇİM YAP:[/bold white]", style="blink",end=" ")
                        CHOOSEN = int(input())
                    except ValueError:
                        c.print( "⚠️  Lütfen sadece sayı girin.",style="" )
                        input("ENTER ile devam et...")
                        continue
                    

                    if CHOOSEN not in (1,2,3,4,5,6,7,8,9,10,11,12, 13,44):
                        c.print( "❗❗❗❗❗❗❗ Düzgün bir sayı gir ❗❗❗❗❗❗", style="blink")
                        input("ENTER ile devam et...")
                        continue      
                        

                    elif CHOOSEN == 1:
                        oglis.yeniEklenenOgrencilerListesiDökümü() 
                        ENTER()

                    elif CHOOSEN==2:
                        oglis.silinmişKayıtlılarListesiDökümü() 
                        ENTER()

                        
                    elif CHOOSEN==3:
                        Json.JSONdanYükleme_()
                        Sayac_Kronometre.geri_say(3)
                       
                        
                        
                    elif CHOOSEN==4: 
                        c.print("\n[bold]VERİ.TupleliListe_:[/bold]",Veri.TupleliListe_)
                        ENTER()
           
                    elif CHOOSEN==5:
                        tupSoz.TupleyiSözlükYap(liste=Veri.TupleliListe_)
                        #NOTE - Hangi tuple var, ilk kayıttaki mi , jsondan gelip remove edilmiş olan mı, 
                        klavDinle.Enter_ile_devam_et()

                    elif CHOOSEN==6:
                        menüTipi="sözlüklüListe"
                        listeTipi="sözlüklüListe"
                        if Veri.SozlukluListe_:
                            c.print("\nVERİ.SözlüklüListe_:",style="green")
                            for i in Veri.SozlukluListe_:
                                    c.print(i)
                                    
                        else:
                            print( "Henüz Öğrenci Kaydı girilmedi. ")
                        klavDinle.Enter_ile_devam_et()
                        

                    elif CHOOSEN==7:
                        menüTipi="tupleliListe"
                        listeTipi="tupleliListe"
                        Veri.TupleliListe_.sort()
                            
                        c.print(f"\n[ {len(Veri.TupleliListe_)} TALEBE bulundu ]",style=" white")
                        c.print("[magenta]VERİ.TupleliListe_:[/magenta]",Veri.TupleliListe_)
                        if Veri.SozlukluListe_:
                           # for sözlük in sözlüklüListe:
                                c.print("\n",Veri.SozlukluListe_,"\n",style="bold")
                        else:
                            print( "SözlüklüListe_de Öğrenci Kaydı yok. ")
                        klavDinle.Enter_ile_devam_et()

                    elif CHOOSEN==8:
                        Sayac_Kronometre.geri_say(3)
                        
                    
                    elif CHOOSEN==9:
                        Veri.TupleliListe_.clear()
                        if Veri.TupleliListe_:
                            print("Tupleli liste dolu")
                            ENTER()
                        else:
                            print("Tupleli liste  BOŞŞŞ şuanda.")
                        ENTER()
                    
                    elif CHOOSEN==10:
                        Veri.SozlukluListe_.clear()

                        # ekran temizlenir anaMenüye gidilir Lakin silinen eklenen listeleri doludur.
                        
                    elif CHOOSEN==11:
                        Dilimleme.dilimleme(5,Veri.TupleliListe_)                        
                        #ANCHOR - console.input("\n🔁 Devam etmek için ENTER'a basın..." )
                    
                    elif CHOOSEN==12:
                        sırfSORGU._SırfSorgu_()
                                       
                        
                    elif CHOOSEN==13:  #NOTE - renk paleti  
                        c.print("[bold underline]256 Renk Paleti[/]\n")
                        for i in range(0, 256, 16):
                            line = " ".join(f"[on color({j})]{j:3}[/]" for j in range(i, i + 16))
                            c.print(line)
                        klavDinle.Enter_ile_devam_et()
                    
                    elif CHOOSEN==44:
                        startPoint()
                        
                        
  


if __name__ == "__main__":
            startPoint()