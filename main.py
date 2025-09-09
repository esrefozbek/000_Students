import sys,os
import canlıTablo 
from klavyeDinleme import ENTER
from rich.live import Live
import dilimleme, veri, yeniOgrenci_KAYIT, ogrenci_LiSTEleme, JSON, menu, tupleyi_Sozluklestirme, ogrenci_SiLME,  klavyeDinleme, readchar, sırfSORGU, time,sayacKronometre,pomodoro,teknikMenü,arama

from rich.console import Console; c = Console()

"""! Bu programda ilk olarak JSON dosyasından verileri alıyoruz, yoksa boş falan diyerek uyarı veriyoruz.
Yeni öğrenci Kayıt işlemleri ilk olarak  'ogrenciListesi=[ ];' ne tuple şeklinde kayıt girilerek bqşlıyor, listeye tupleler şeklinde öğrencileri ekliyoruz.   """

menu.ekranTemizle()
def startPoint():
        veri.TupleliListe_.clear()
        veri.SozlukluListe_.clear()
        menu.rastgele_box_stili
        
        
#!SECTION ANAMENÜ
        while True:  #Menüden seçim
            
                    menu.menu_goster()
                    #REVIEW - JSON._JSONdanYükleme_()
                    try:
                        c.print("🟢 [bold white]SANA ZAHMET BİR SEÇİM YAP:[/bold white]", style="blink",end=" ")
                        CHOOSEN = int(input())
                    except ValueError:
                        c.print( "⚠️  Lütfen sadece sayı girin.",style="" )
                        input("ENTER ile devam et...")
                        continue
                    
                    if CHOOSEN not in (1,2,3,4,5,6,7,77,33):
                        c.print( "❗❗❗❗❗❗❗ Düzgün bir sayı gir ❗❗❗❗❗❗", style="blink")
                        input("ENTER ile devam et...")
                        continue
                   
                        
                    
                    
                    if CHOOSEN == 1:#NOTE - YENİ KAYIT
                        yeniOgrenci_KAYIT.yeniOgrenciKayidi()



                    elif CHOOSEN==2:#NOTE - BUL
                        if not veri.TupleliListe_:
                            JSON.JSONdanYükleme_()
                            while True:
                                a=arama.aramaParametresi()
                                if a is not None:
                                    a=a.strip().lower()
                                    if a is "":
                                        c.print("Hiçbir değer girmeden [italic white]Enter[/] tuşuna bastınız",style="yellow")
                                    else:    
                                        arama.arama(a)
                                else :
                                    break
                      
                        veri.TupleliListe_.clear()
                        pomodoro.geri_say_bar(3,"Ana menüye dönülecek (5 saniye)...")
                        #pomodoro.pomodoro_dongusu()
                       

                    elif CHOOSEN ==3: #NOTE -  SİL
                        # if not VERİ.TupleliListe_:
                        # else:
                        JSON.JSONdanYükleme_()   
                        print( "❗ Liste boş, silinecek öğrenci yok.")
                        ogrenci_SiLME.ogrenciSil()
                        klavyeDinleme.Enter_ile_devam_et()

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
                           
                           os.system("exit")
                           sys.exit()
                           os.system("taskkill /F /PID " + str(os.getpid()))
                        
                    elif CHOOSEN==5: #NOTE - Ekranı resEtleme
                        sayacKronometre.geri_say(5)
                       
                    elif CHOOSEN==6: #NOTE - editleme
                        canlıTablo.main()
                        sayacKronometre.geri_say(6)
                        
                    elif CHOOSEN == 7: #NOTE -  DİLİMLEME         #Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
                      
                        veri.value=10
                        değer=veri.value
                        menu.ekranTemizle()
                        JSON.JSONdanYükleme_()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if veri.TupleliListe_:
                            ogrenci_LiSTEleme.altAltaOgrenciListesi(değer)
                            veri.TupleliListe_.clear()
                        else:
                            c.print("📭 Liste boş. Önce öğrenci gir.",style="white")
                        sayacKronometre.progress_sayac()

                    elif CHOOSEN==77:#NOTE -  DİLİMLEME
                
                        veri.value=50
                        değer=veri.value
                        menu.ekranTemizle()
                        JSON.JSONdanYükleme_()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if veri.TupleliListe_:
                            ogrenci_LiSTEleme.altAltaOgrenciListesi(değer)
                            canlıTablo.main()    
                            veri.TupleliListe_.clear()
                        else:
                            c.print("📭 Liste boş. Önce öğrenci gir.", style="blink")
                      #FIXME -   menü.rastgele_box_stili
                            ENTER()
                        #FIXME - startPoint()
                    
                       
                    elif CHOOSEN==33:
                       break
                    with Live(refresh_per_second=2) as live:
                        for _ in range(3):
                            time.sleep(1)
                            live.update(f"menü açılıyor... {_}")           
                    
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
                        ogrenci_LiSTEleme.yeniEklenenOgrencilerListesiDökümü() 
                        ENTER()

                    elif CHOOSEN==2:
                        ogrenci_LiSTEleme.silinmişKayıtlılarListesiDökümü() 
                        ENTER()

                        
                    elif CHOOSEN==3:
                        JSON.JSONdanYükleme_()
                        sayacKronometre.geri_say(6)
                       
                        
                        
                    elif CHOOSEN==4: 
                        c.print("\n[bold]VERİ.TupleliListe_:[/bold]",veri.TupleliListe_)
                        ENTER()
           
                    elif CHOOSEN==5:
                        tupleyi_Sozluklestirme.TupleyiSözlükYap(liste=veri.TupleliListe_)
                        #NOTE - Hangi tuple var, ilk kayıttaki mi , jsondan gelip remove edilmiş olan mı, 
                        klavyeDinleme.Enter_ile_devam_et()

                    elif CHOOSEN==6:
                        menüTipi="sözlüklüListe"
                        listeTipi="sözlüklüListe"
                        if veri.SozlukluListe_:
                            c.print("\nVERİ.SözlüklüListe_:",style="green")
                            for i in veri.SozlukluListe_:
                                    c.print(i)
                                    
                        else:
                            print( "Henüz Öğrenci Kaydı girilmedi. ")
                        klavyeDinleme.Enter_ile_devam_et()
                        

                    elif CHOOSEN==7:
                        menüTipi="tupleliListe"
                        listeTipi="tupleliListe"
                        veri.TupleliListe_.sort()
                            
                        c.print(f"\n[ {len(veri.TupleliListe_)} TALEBE bulundu ]",style=" white")
                        c.print("[magenta]VERİ.TupleliListe_:[/magenta]",veri.TupleliListe_)
                        if veri.SozlukluListe_:
                           # for sözlük in sözlüklüListe:
                                c.print("\n",veri.SozlukluListe_,"\n",style="bold")
                        else:
                            print( "SözlüklüListe_de Öğrenci Kaydı yok. ")
                        klavyeDinleme.Enter_ile_devam_et()

                    elif CHOOSEN==8:
                        sayacKronometre.geri_say(5)
                        
                    
                    elif CHOOSEN==9:
                        veri.TupleliListe_.clear()
                        if veri.TupleliListe_:
                            print("Tupleli liste dolu")
                            ENTER()
                        else:
                            print("Tupleli liste  BOŞŞŞ şuanda.")
                        ENTER()
                    
                    elif CHOOSEN==10:
                        veri.SozlukluListe_.clear()

                        # ekran temizlenir anaMenüye gidilir Lakin silinen eklenen listeleri doludur.
                        
                    elif CHOOSEN==11:
                        dilimleme.dilimleme(5,veri.TupleliListe_)                        
                    #ANCHOR - console.input("\n🔁 Devam etmek için ENTER'a basın..." )
                    
                    elif CHOOSEN==12:
                        sırfSORGU._SırfSorgu_()
                                       
                        
                    elif CHOOSEN==13:  #NOTE - renk paleti  
                        c.print("[bold underline]256 Renk Paleti[/]\n")
                        for i in range(0, 256, 16):
                            line = " ".join(f"[on color({j})]{j:3}[/]" for j in range(i, i + 16))
                            c.print(line)
                        klavyeDinleme.Enter_ile_devam_et()
                    
                    elif CHOOSEN==44:
                        startPoint()
                        
                        
  


if __name__ == "__main__":
    startPoint()