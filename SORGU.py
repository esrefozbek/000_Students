import tablolarPY,VERİ
from rich.console import Console; console=Console()

menüTipi="Sorgu Menüsü"
listeTipi="Sorgu Listesi"


SorgudaBulunanlarListesi_=[]

def _Sorgu_(buÖğrenciyiBul):
    found = False
    if SorgudaBulunanlarListesi_:
        SorgudaBulunanlarListesi_.clear()  #TODO - Her sorguda önce temizle 
        
    if buÖğrenciyiBul:     
        if buÖğrenciyiBul.isdigit():
            for ogrenci in VERİ.TupleliListe_:
                if buÖğrenciyiBul == str(ogrenci[0]):
                    found = True
                    SorgudaBulunanlarListesi_.append(ogrenci)
                    if len(SorgudaBulunanlarListesi_) == 1:
                        console.print(f"\n🔍 Bulunan Öğrenciler Listesi ", style="bold white on blue",end="")
                    
            console.print(f"[ {len(SorgudaBulunanlarListesi_)} TALEBE bulundu ]", style=" bold yellow")
            # main.ekranTemizle()
            # main.menu_goster()
            if len(SorgudaBulunanlarListesi_)==0:
                pass
            else:
                tablolarPY.TABLO_6lı(SorgudaBulunanlarListesi_,menüTipi, listeTipi)
           
           
            if not found:
                console.print(" [white on red]Bu numaraya sahip bir öğrenci yok. Düzgün bir sayı gir[/white on red]", style=""  )
        else:
            if SorgudaBulunanlarListesi_:
                SorgudaBulunanlarListesi_.clear()  #TODO - Her sorguda önce temizle
                
            for ogrenci in VERİ.TupleliListe_:
                if buÖğrenciyiBul in ogrenci[1] or buÖğrenciyiBul in ogrenci[2]:
                    SorgudaBulunanlarListesi_.append(ogrenci)
                    if len(SorgudaBulunanlarListesi_) == 1:
                        
                        console.print(f"\n🔍 Bulunan Öğrenciler Listesi ", style="bold black on white",end="")
            console.print(f"[ {len(SorgudaBulunanlarListesi_)} TALEBE bulundu ]", style=" bold yellow")
            # main.ekranTemizle()
            # main.menu_goster()
            
            if len(SorgudaBulunanlarListesi_)==0:
                pass
            else:
                tablolarPY.TABLO_6lı(SorgudaBulunanlarListesi_,menüTipi, listeTipi)
                
            if not SorgudaBulunanlarListesi_:
                console.print("[blue on bright_green]  Bu isimde bir öğrenci bulunamadı.[/blue on bright_green]", style="orange1")
           
