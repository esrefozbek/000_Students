#breakpoint()
import os
from rich.console import Console; c = Console()


def txtOlustur(txt_dosya_yolu):
    os.makedirs(os.path.dirname(txt_dosya_yolu), exist_ok=True)
    with open(txt_dosya_yolu, "w", encoding="utf-8") as dosya:
        dosya.write("ID: 0\n")
    print("Dosya oluşturuldu ve ID: 0 yazıldı.")
    mevcut_id=0
    return mevcut_id

def txtID_Oku(dosya_yolu):
    with open(dosya_yolu, "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()
        return int(satirlar[0].split(":")[1].strip())

def txtUpdate(txt_dosya_yolu, yeni_id):
    with open(txt_dosya_yolu, "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()
    if satirlar:
        satirlar[0] = f"ID: {yeni_id}\n"
    else:
        satirlar = [f"ID: {yeni_id}\n"]
    return satirlar

def txtUzerineYaz(txt_dosya_yolu, yeni_id):
    satirlar = txtUpdate(txt_dosya_yolu, yeni_id)
    with open(txt_dosya_yolu, "w", encoding="utf-8") as dosya:
        dosya.writelines(satirlar)
   # c.print("\t[yellow]ID txt dosyasında güncellendi[/][green] >>[/]", satirlar[0],end=""        )



def ID_olustur_ve_oku():
    txt_dosya_yolu = "VERI/Text.txt"
    
    if not os.path.exists(txt_dosya_yolu):
        mevcut_id = txtOlustur(txt_dosya_yolu)
    else: 
        mevcut_id = txtID_Oku(txt_dosya_yolu)

    yeni_id = mevcut_id + 1
    txtUzerineYaz(txt_dosya_yolu, yeni_id)
    c.print(f"Yeni ID kaydedildi: {yeni_id}")
    
    return yeni_id

if __name__ == "__main__":
    ID_olustur_ve_oku()
