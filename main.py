import canlıTablo 
from klavyeDinleme import ENTER
from rich.live import Live
import dilimleme, VERİ, yeniÖğrenci_KAYIT, ogrenci_LiSTEleme, JSON, menü, tupleyi_Sözlükleştirme, ogrenci_SiLME, ogrenci_BUL, klavyeDinleme, readchar, sırfSORGU, time,sayaçKronometre,pomodoro,teknikMenü

from rich.console import Console; console = Console()

"""! Bu programda ilk olarak JSON dosyasından verileri alıyoruz, yoksa boş falan diyerek uyarı veriyoruz.
Yeni öğrenci Kayıt işlemleri ilk olarak  'ogrenciListesi=[ ];' ne tuple şeklinde kayıt girilerek bqşlıyor, listeye tupleler şeklinde öğrencileri ekliyoruz.   """

menü.ekranTemizle()
def startPoint():
        VERİ.TupleliListe_.clear()
        VERİ.SözlüklüListe_.clear()
        menü.rastgele_box_stili
        
        

        while True:  #Menüden seçim
            
                    menü.menu_goster()
                    #REVIEW - JSON._JSONdanYükleme_()
                    try:
                        console.print("🟢 [bold white]SANA ZAHMET BİR SEÇİM YAP:[/bold white]", style="blink",end=" ")
                        CHOOSEN = int(input())
                    except ValueError:
                        console.print( "⚠️  Lütfen sadece sayı girin.",style="" )
                        input("ENTER ile devam et...")
                        continue
                    
                    if CHOOSEN not in (1,2,3,4,5,6,7,77,33):
                        console.print( "❗❗❗❗❗❗❗ Düzgün bir sayı gir ❗❗❗❗❗❗", style="blink")
                        input("ENTER ile devam et...")
                        continue
                   
                        
                    
                    
                    if CHOOSEN == 1:
                        yeniÖğrenci_KAYIT.yeniÖğrenciKayıdı()

                    elif CHOOSEN==2:
                        if not VERİ.TupleliListe_:
                            JSON.JSONdanYükleme_()
                            ogrenci_BUL.ogrenciBul()
                        #FIXME - klavyeDinleme.enter_ile_devam_et()
                        VERİ.TupleliListe_.clear()
                        pomodoro.geri_say_bar(4,"pomodoro")
                       
                        

                    elif CHOOSEN ==3:
                        # if not VERİ.TupleliListe_:
                        # else:
                        JSON.JSONdanYükleme_()   
                        print( "❗ Liste boş, silinecek öğrenci yok.")
                        ogrenci_SiLME.ogrenciSil()
                        klavyeDinleme.Enter_ile_devam_et()

                    elif CHOOSEN==4:
                        print("Çıkılıyor. Görüşmek üzere!")
                        #JSON.JSONaKayıt("öğrenciler.json",VERİ.SözlüklüListe_)
                        #VERİ.SözlüklüListe_.clear()
                        console.print("\n[bold ] bak cidden çıkıyorum [bold yellow]emin misin[/bold yellow]\n[bold] [bold white]Vazgeçmek istersen [bold green ]Esc[/bold green]'ye bas [/bold white]\n [bold orange] İlla çıkman gerekiyorsa [bold green ]ENTER[/bold green]'a bas [/bold orange]")
                                            
                        key = readchar.readkey()
                        if key == readchar.key.ESC:
                            startPoint()

                        elif key == '\r':  # ENTER
                            break
                        
                        
                    elif CHOOSEN==5: #NOTE - Ekranı restleme
                        sayaçKronometre.geri_say(5)
                       
                    elif CHOOSEN==6: #NOTE - editleme0
                        canlıTablo.main()
                        sayaçKronometre.geri_say(6)
                        
                    elif CHOOSEN == 7:         #Burada tüm liste ekranı aşıyor,   Tüm listeyi  20 satır yap,  oklarla 21... satırlara gidebil Ama tablonun içinde yaşa bu durumu. 
                      
                        VERİ.value=10
                        değer=VERİ.value
                        menü.ekranTemizle()
                        JSON.JSONdanYükleme_()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if VERİ.TupleliListe_:
                            ogrenci_LiSTEleme.altAltaOgrenciListesi(değer)
                            VERİ.TupleliListe_.clear()
                        else:
                            console.print("📭 Liste boş. Önce öğrenci gir.",style="white")
                        sayaçKronometre.progress_sayac()

                    elif CHOOSEN==77:
                
                        VERİ.value=50
                        değer=VERİ.value
                        menü.ekranTemizle()
                        JSON.JSONdanYükleme_()
                        #FIXME - JSON.JSONaKayıt("öğrenciler.json")
                        if VERİ.TupleliListe_:
                            ogrenci_LiSTEleme.altAltaOgrenciListesi(değer)
                            canlıTablo.main()    
                            VERİ.TupleliListe_.clear()
                        else:
                            console.print("📭 Liste boş. Önce öğrenci gir.", style="blink")
                      #FIXME -   menü.rastgele_box_stili
                            ENTER()
                        #FIXME - startPoint()
                    
                       
                    elif CHOOSEN==33:
                       break
        with Live(refresh_per_second=2) as live:
            for _ in range(3):
                time.sleep(1)
                live.update(f"menü açılıyor... {_}")           
                    
              
        while True:                
                    teknikMenü.teknikMenü()
                    try:
                        console.print("🟢 [bold white]SANA ZAHMET BİR SEÇİM YAP:[/bold white]", style="blink",end=" ")
                        CHOOSEN = int(input())
                    except ValueError:
                        console.print( "⚠️  Lütfen sadece sayı girin.",style="" )
                        input("ENTER ile devam et...")
                        continue
                    

                    if CHOOSEN not in (1,2,3,4,5,6,7,8,9,10,11,12, 13,44):
                        console.print( "❗❗❗❗❗❗❗ Düzgün bir sayı gir ❗❗❗❗❗❗", style="blink")
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
                        sayaçKronometre.geri_say(6)
                       
                        
                        
                    elif CHOOSEN==4: 
                        console.print("\n[bold]VERİ.TupleliListe_:[/bold]",VERİ.TupleliListe_)
                        ENTER()
           
                    elif CHOOSEN==5:
                        tupleyi_Sözlükleştirme.TupleyiSözlükYap(liste=VERİ.TupleliListe_)
                        #NOTE - Hangi tuple var, ilk kayıttaki mi , jsondan gelip remove edilmiş olan mı, 
                        klavyeDinleme.Enter_ile_devam_et()

                    elif CHOOSEN==6:
                        menüTipi="sözlüklüListe"
                        listeTipi="sözlüklüListe"
                        if VERİ.SözlüklüListe_:
                            console.print("\nVERİ.SözlüklüListe_:",style="green")
                            for i in VERİ.SözlüklüListe_:
                                    console.print(i)
                                    
                        else:
                            print( "Henüz Öğrenci Kaydı girilmedi. ")
                        klavyeDinleme.Enter_ile_devam_et()
                        

                    elif CHOOSEN==7:
                        menüTipi="tupleliListe"
                        listeTipi="tupleliListe"
                        VERİ.TupleliListe_.sort()
                            
                        console.print(f"\n[ {len(VERİ.TupleliListe_)} TALEBE bulundu ]",style=" white")
                        console.print("[magenta]VERİ.TupleliListe_:[/magenta]",VERİ.TupleliListe_)
                        if VERİ.SözlüklüListe_:
                           # for sözlük in sözlüklüListe:
                                console.print("\n",VERİ.SözlüklüListe_,"\n",style="bold")
                        else:
                            print( "SözlüklüListe_de Öğrenci Kaydı yok. ")
                        klavyeDinleme.Enter_ile_devam_et()

                    elif CHOOSEN==8:
                        sayaçKronometre.geri_say(5)
                        
                    
                    elif CHOOSEN==9:
                        VERİ.TupleliListe_.clear()
                        if VERİ.TupleliListe_:
                            print("Tupleli liste dolu")
                            ENTER()
                        else:
                            print("Tupleli liste  BOŞŞŞ şuanda.")
                        ENTER()
                    
                    elif CHOOSEN==10:
                        VERİ.SözlüklüListe_.clear()

                        # ekran temizlenir anaMenüye gidilir Lakin silinen eklenen listeleri doludur.
                        
                    elif CHOOSEN==11:
                        dilimleme.dilimleme(5,VERİ.TupleliListe_)                        
                    #ANCHOR - console.input("\n🔁 Devam etmek için ENTER'a basın..." )
                    
                    elif CHOOSEN==12:
                        sırfSORGU._SırfSorgu_()
                                       
                        
                    elif CHOOSEN==13:  #NOTE - renk paleti  
                        console.print("[bold underline]256 Renk Paleti[/]\n")
                        for i in range(0, 256, 16):
                            line = " ".join(f"[on color({j})]{j:3}[/]" for j in range(i, i + 16))
                            console.print(line)
                        klavyeDinleme.Enter_ile_devam_et()
                    
                    elif CHOOSEN==44:
                        startPoint()
                        
                        
  


if __name__ == "__main__":
    startPoint()

    
    
    
    
    
    