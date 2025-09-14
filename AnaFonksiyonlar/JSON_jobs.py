#breakpoint()
import VERI.emptyLists as VERIModul,Widgetler.SayacAnimasyon.sayacKronometre as Say_Kro
import json
import os
from rich.panel import Panel
from rich.layout import Layout
from rich import print
from rich.console import Console; c = Console()
import AsistanFonksiyonlar.txt_Jobs as TxtYolu
import AsistanFonksiyonlar.tupleyi_Sozluklestirme as makeDict
import Widgetler.SayacAnimasyon.spinner as SpinnerPY




#& JSON DOSYASINDAN LİSTEYİ ÇEKME  
            
def JSONdanYükleme_():
           #^ console.print("\n[bold yellow]jsondan_yükleme():[/bold yellow]🐓🐓🐓  VERİ.TupleliListe_:", veri.TupleliListe_,style="")
            
            jsonDosya_adi = ("VERI/students.json")

            if not os.path.exists(jsonDosya_adi):
                print(f"⚠️ '{jsonDosya_adi}' dosyası bulunamadı. Henüz veri kaydedilmemiş olabilir.")
                return
           
            with open(jsonDosya_adi, "r", encoding="utf-8") as file:
                Geçici_Liste = json.load(file)
            
            if VERIModul.SilinenlerinTupleliListesi_:
               VERIModul.SilinenlerinTupleliListesi_.clear() 
            # Tuple listeyi oluştur
            VERIModul.SilinenlerinTupleliListesi_ = [
            (ogr["id"], ogr["ad"], ogr["soyad"],ogr["öğrenciNumarası"], ogr["dogum_yili"], ogr["sinif"], ogr["kayıtTarihi"])
                for ogr in Geçici_Liste  ]
    
            if not VERIModul.SilinenlerinTupleliListesi_:
                c.print("[bold yellow]jsondan_yükleme(): [/bold yellow] TupleliListe_ şuan boş",style="")
                c.print(VERIModul.SilinenlerinTupleliListesi_,"...")
            
            

#&                              JSON DOSYASINA ÖĞRENCİ EKLEME                                  
# 2️⃣ JSON'a kayıt fonksiyonu

def JSONaKayıtOncesiDosya_VarMi(jsonDosya_adi: str, EklenenVeyaSilinenSayisi: int):
  
    try:
        with open(jsonDosya_adi, "r", encoding="utf-8") as f:
            mevcut_veriler = json.load(f)
            getLastJSON_ID = mevcut_veriler[-1]["id"] if mevcut_veriler else 0   #NOTE -  
            txt_dosya_yolu = "VERI/Text.txt"
            if not os.path.exists(txt_dosya_yolu):
                getTextID = TxtYolu.txtOlustur(txt_dosya_yolu)
            else: 
                getTextID = TxtYolu.txtID_Oku(txt_dosya_yolu)
                getTextID = TxtYolu.txtID_Oku("VERI/Text.txt")

    except (FileNotFoundError, json.JSONDecodeError):
        mevcut_veriler = []
        getLastJSON_ID = 0
        TxtYolu.txtOlustur("VERI/Text.txt")
        getTextID = 0




def JSONaKayıtOncesiID_UyumKontrolu(jsonDosya_adi: str, EklenenVeyaSilinenSayisi: int):
    if getTextID!=(getLastJSON_ID+ EklenenVeyaSilinenSayisi):
        c.print("\n","⚠️","[red]ID çatışması tespit edildi. Biraz belkleyin düzeltiyorum.[/]")
        SpinnerPY.spinner2(3)      
        for i in VERIModul.YeniEklenenlerinSozluklerListesi_:
            getLastJSON_ID+=1
            i["id"]=getLastJSON_ID 
            TxtYolu.txtUzerineYaz("VERI/Text.txt", getLastJSON_ID)
    
    return mevcut_veriler, getLastJSON_ID, getTextID




def JSONaKayıt(jsonDosya_adi: str, mevcut_veriler: list,YeniEklenenlerinSozluklerListesi_: list):
    sayi=len(YeniEklenenlerinSozluklerListesi_)
    veri=JSONaKayıtOncesiDosya_VarMi(jsonDosya_adi, sayi)
    JSONaKayıtOncesiID_UyumKontrolu(jsonDosya_adi, EklenenVeyaSilinenSayisi)
    veri[0].extend(YeniEklenenlerinSozluklerListesi_)
    getLastJSON_ID = veri[0][-1]["id"]
    
    with open(jsonDosya_adi, "w", encoding="utf-8") as f:
        json.dump(veri[0], f, indent=4, ensure_ascii=False)
    c.print(f"{len(YeniEklenenlerinSozluklerListesi_)} öğrencinin bilgileri [red]JSON[/]'a kaydedildi.\n")
    VERIModul.YeniEklenenlerinTupleListesi_.clear()
    SpinnerPY.spinner3(3)      
    return veri[1]


def JSONdanKayitSilme(jsonDosya_adi: str, SilinenlerinSozluklerListesi_: list,mevcut_veriler: list ):
    sayi=len(SilinenlerinSozluklerListesi_)*(-1)
    #FIXME -  veri=JSONaKayıtOncesiID_Kontrol(jsonDosya_adi, sayi)
    mevcut_veriler.remove(SilinenlerinSozluklerListesi_)
    getLastJSON_ID = mevcut_veriler[-1]["id"]
    
    with open(jsonDosya_adi, "w", encoding="utf-8") as f:
        json.dump(mevcut_veriler, f, indent=4, ensure_ascii=False)
    c.print(f"{len(SilinenlerinSozluklerListesi_)} öğrencinin bilgileri [red]JSON[/]'dan silindi.\n")
    VERIModul.SilinenlerinSozluklerListesi_.clear()
    SpinnerPY.spinner3(3)      
    return getLastJSON_ID