import VERI.emptyLists as Veri_Yolu,Widgetler.SayacAnimasyon.sayacKronometre as Say_Kro
import json
import os
from rich.panel import Panel
from rich.layout import Layout
from rich import print
from rich.console import Console; c = Console()
import AsistanFonksiyonlar.txt_Jobs as TxtYolu


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

def JSONaKayıt(jsonDosya_adi: str, liste: list):
    global getLastID

    try:
        with open(jsonDosya_adi, "r", encoding="utf-8") as f:
            mevcut_veriler = json.load(f)
            getLastID = mevcut_veriler[-1]["id"] if mevcut_veriler else 0

    except (FileNotFoundError, json.JSONDecodeError):
        c.print("JSON dosyası mevcut değil")
        mevcut_veriler = []
        getLastID = 0

        if not os.path.exists("VERI/Text.txt"):
            c.print("[yellow]VERI/Text.txt dosyası bulunamadı. Oluşturuluyor...[/yellow]")
            TxtYolu.txtYoksaOlustur("VERI/Text.txt")

        c.print("Yeni bir JSON dosyası oluşturuluyor...", style="bold red")
        with open(jsonDosya_adi, "w", encoding="utf-8") as f:
            json.dump(mevcut_veriler, f, indent=4)

    # Mevcut ID ile text dosyasındaki ID'yi karşılaştır
    textID = TxtYolu.txtID_Oku("VERI/Text.txt")
    c.print("getLastID:", getLastID, "| Text.txt ID - 1:", textID - 1)

    if getLastID != (textID - 1):
        Veri_Yolu.YeniEklenenlerinTupleListesi_.clear()
        Veri_Yolu.TupleliListe_.clear()
        Veri_Yolu.SozluklerListesi_.clear()

        TxtYolu.txtUzerineYaz("VERI/Text.txt", getLastID)
        c.print("[bold red]⚠️ ID çakışması tespit edildi. Lütfen öğrenci kaydını tekrar yapınız.[/bold red]")
        input("[Enter] tuşuna basarak devam ediniz...")
        return getLastID

    else:
        mevcut_veriler.extend(liste)
        getLastID = mevcut_veriler[-1]["id"]

        with open(jsonDosya_adi, "w", encoding="utf-8") as f:
            json.dump(mevcut_veriler, f, indent=4, ensure_ascii=False)

        c.print(f"💾 [bold green]JSONaKayıt_[/]: '{jsonDosya_adi}' dosyasına {len(liste)} öğrenci eklendi.")
        return getLastID
