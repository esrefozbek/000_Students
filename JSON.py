
import json
from rich.console import Console
import veri,sayacKronometre, os
from rich.panel import Panel
from rich.layout import Layout
from rich import print
console = Console()

#! JSON DOSYASINA ÖĞRENCİ EKLEME


def JSONaKayıt(dosya_adi:str, liste:list ):
        """ try:
            with open(dosya_adi, "r", encoding="utf-8") as f:
                jsonaKayıt_içinGeçiciListe = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            console.print(f"[red]Hata oluştu:[/red] {e}") """
        
        jsonaKayıt_içinGeçiciListe = []
        # Yeni öğrencileri ekle
        jsonaKayıt_içinGeçiciListe.extend(liste) # Dosyaya JSON olarak yaz
        with open(dosya_adi, "w", encoding="utf-8") as f:
                json.dump(jsonaKayıt_içinGeçiciListe, f, indent=4, ensure_ascii=False)
        jsonaKayıt_içinGeçiciListe = []
 
       #REVIEW -  console.print("[bold yellow]_jsona_kayıt_: [/bold yellow] mevcut veriler iLAVELi hali:",    mevcut_veriler)
        console.print(f"💾 _jsona_kayıt_() : '{dosya_adi}' dosyasına {len(veri.SozlukluListe_)} öğrenci eklendi.\n")
        # VERİ.SözlüklüListe_.clear()
        # VERİ.TupleliListe_.clear()
    

#! JSON DOSYASINDAN LİSTEYİ ÇEKME
            
def JSONdanYükleme_():
           #^ console.print("\n[bold yellow]jsondan_yükleme():[/bold yellow]🐓🐓🐓  VERİ.TupleliListe_:", veri.TupleliListe_,style="")
            
            dosya_adi = "students.json"
            if not os.path.exists(dosya_adi):
                print(f"⚠️ '{dosya_adi}' dosyası bulunamadı. Henüz veri kaydedilmemiş olabilir.")
                return
           
            with open("students.json", "r", encoding="utf-8") as file:
                Geçici_Liste = json.load(file)
                
             #^ -    console.print(Panel.fit(f"\n[bold yellow]jsondan_yükleme():[/bold yellow] 🤡🤡🤡 Geçici_Liste=json.load(file) tipi ve [-1:] :{type(Geçici_Liste)},{Geçici_Liste[-1:]}",style=""))
                
                #ANCHOR -  console.print("[bold yellow]jsondan_yükleme(): [/bold yellow] 'ogrenci_listesi = json.load(f)'  tipi:",type(ogrenci_listesi))
                #ANCHOR - console.print("[bold yellow]jsondan_yükleme(): [/bold yellow]  .json'dan gelen sözlüklü liste: _____ogrenci_listesi_____",style="white")
                #ANCHOR - console.print("[yellow]jsondan_yükleme(): [/yellow] ogrenci_listesi değişken olmayan geçici bir listedir.")
                #ANCHOR -  console.print(ogrenci_listesi[1])   #NOTE - örnek olarak koydum
               
            
            if veri.TupleliListe_:
                veri.TupleliListe_.clear() 
            # Tuple listeyi oluştur
            veri.TupleliListe_ = [
            (ogr["id"], ogr["ad"], ogr["soyad"],ogr["öğrenciNumarası"], ogr["dogum_yili"], ogr["sinif"], ogr["kayıtTarihi"])
                for ogr in Geçici_Liste  ]
            
            #! - console.print(Panel.fit(f"[bold yellow]jsondan_yükleme():[/bold yellow]🌼🌼🌼 yukarıdaki sözlük içeren liste tupleye çevrildi ve TupleliListe_ye eklendi : {veri.TupleliListe_[-1:]}", style=""))
            
            
            #! console.print(Panel.fit(f"\n[bold yellow]jsondan_yükleme():[/bold yellow]🦢🦢🦢  JSON'dan gelen sözlükler tupleye çevrildi ve TupleliListe_'ye döşendi.TupleliListe_ dolu şuandaa [-2:] \n { veri.TupleliListe_[-2:]}",style=""))
            
    
            if not veri.TupleliListe_:
                console.print("[bold yellow]jsondan_yükleme(): [/bold yellow] if TupleliListe_ şuan boş",style="")
                console.print(veri.TupleliListe_,"...")
            
            
