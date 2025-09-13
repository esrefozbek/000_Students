#breakpoint()
import VERI.emptyLists as Veri_Yolu,Widgetler.SayacAnimasyon.sayacKronometre as Say_Kro
import json
import os
from rich.panel import Panel
from rich.layout import Layout
from rich import print
from rich.console import Console; c = Console()
import AsistanFonksiyonlar.txt_Jobs as TxtYolu
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as makeDict
import Widgetler.SayacAnimasyon.spinner as SpinnerYolu




#& JSON DOSYASINDAN LİSTEYİ ÇEKME  
            
def JSONdanYükleme_():
           #^ console.print("\n[bold yellow]jsondan_yükleme():[/bold yellow]🐓🐓🐓  VERİ.TupleliListe_:", veri.TupleliListe_,style="")
            
            jsonDosya_adi = ("VERI/students.json")

            if not os.path.exists(jsonDosya_adi):
                print(f"⚠️ '{jsonDosya_adi}' dosyası bulunamadı. Henüz veri kaydedilmemiş olabilir.")
                return
           
            with open(jsonDosya_adi, "r", encoding="utf-8") as file:
                Geçici_Liste = json.load(file)
            
            if Veri_Yolu.TupleliListe_:
               Veri_Yolu.TupleliListe_.clear() 
            # Tuple listeyi oluştur
            Veri_Yolu.TupleliListe_ = [
            (ogr["id"], ogr["ad"], ogr["soyad"],ogr["öğrenciNumarası"], ogr["dogum_yili"], ogr["sinif"], ogr["kayıtTarihi"])
                for ogr in Geçici_Liste  ]
    
            if not Veri_Yolu.TupleliListe_:
                c.print("[bold yellow]jsondan_yükleme(): [/bold yellow] if TupleliListe_ şuan boş",style="")
                c.print(Veri_Yolu.TupleliListe_,"...")
            
            

#& JSON DOSYASINA ÖĞRENCİ EKLEME  
# 2️⃣ JSON'a kayıt fonksiyonu

def JSONaKayıt(jsonDosya_adi: str, TupleSozlukYapildi: list):
    #FIXME -  global getLastID

    try:
        with open(jsonDosya_adi, "r", encoding="utf-8") as f:
            mevcut_veriler = json.load(f)
            getLastID = mevcut_veriler[-1]["id"] if mevcut_veriler else 0   #NOTE -  

    except (FileNotFoundError, json.JSONDecodeError):
        c.print("JSON dosyası mevcut değil")
        mevcut_veriler = []
        getLastID = 0

        if not os.path.exists("VERI/Text.txt"):
            c.print("[yellow]VERI/Text.txt dosyası bulunamadı. Oluşturuluyor...[/yellow]")
            TxtYolu.txtOlustur("VERI/Text.txt")

        c.print("Yeni bir JSON dosyası oluşturuluyor...", style="bold red")
        with open(jsonDosya_adi, "w", encoding="utf-8") as f:
            json.dump(mevcut_veriler, f, indent=4)

    # Mevcut ID ile text dosyasındaki ID'yi karşılaştır
    textID = TxtYolu.txtID_Oku("VERI/Text.txt")
    
    if textID!=(getLastID+len(Veri_Yolu.YeniEklenenlerinTupleListesi_)):
        c.print("\n","⚠️","[red]ID çatışması tespit edildi. Biraz belkleyin düzeltiyorum.[/]")
        c.print("=================================================================")
        c.print("[red]@textID[/] >>",textID)
        c.print("getLastID@JSONFile >>", getLastID,  "|| from Text.txt ID :", textID  - len(Veri_Yolu.YeniEklenenlerinTupleListesi_))
        c.print("[yellow]len(SozluklerListesi_)[] >>",len(Veri_Yolu.SozluklerListesi_))
        c.print("[yellow]len(TupleListe)[/] >>",len(Veri_Yolu.YeniEklenenlerinTupleListesi_))
        c.print("[yellow]IDsi hatalı Tupleler[/] >>",Veri_Yolu.YeniEklenenlerinTupleListesi_,style="yellow")
        c.print("IDsi hatalı Sözlükler >>",TupleSozlukYapildi,style="yellow")
        SpinnerYolu.spinner2(5)      
        for i in Veri_Yolu.SozluklerListesi_:
            getLastID+=1
            #c.print("for içinde getLastID :", getLastID)
            i["id"]=getLastID 
            TxtYolu.txtUzerineYaz("VERI/Text.txt", getLastID)
        c.print("SÖZLÜK IDsi düzeltildi",TupleSozlukYapildi,style="yellow")
        c.print("=================================================================\n")
            
              

    else:  #getLastID == (textID  - len(Veri_Yolu.SozluklerListesi_)):
        """ c.print("=================================================================")
        c.print("[italic yellow]****ÇAKIŞMA YOK****[/]")
        c.print("TxtYolu.txtUzerineYaz", getLastID,"& textID >>",textID )
        c.print("****çakışma var*** \n@textID >>",textID)
        c.print("getLastID@JSONFile >>",getLastID)
        c.print("len(SozluklerListesi_) >>",len(Veri_Yolu.SozluklerListesi_))
        c.print("len(YeniEklenenlerinTupleListesi_) >>",len(Veri_Yolu.YeniEklenenlerinTupleListesi_))
        c.print("getLastID@JSONFile >>", getLastID, "|||| from Text.txt ID :", textID  - len(Veri_Yolu.YeniEklenenlerinTupleListesi_))
        c.print("Veri_Yolu.YeniEklenenlerinTupleListesi>>\n",Veri_Yolu.YeniEklenenlerinTupleListesi_)
        c.print("=================================================================") """

        
                
    mevcut_veriler.extend(TupleSozlukYapildi)
    getLastID = mevcut_veriler[-1]["id"]
    with open(jsonDosya_adi, "w", encoding="utf-8") as f:
        json.dump(mevcut_veriler, f, indent=4, ensure_ascii=False)
    c.print(f"{len(TupleSozlukYapildi)} öğrencinin bilgileri [red]JSON[/]'a kaydedildi.\n")
    Veri_Yolu.YeniEklenenlerinTupleListesi_.clear()
    SpinnerYolu.spinner3(3)      
    return getLastID
