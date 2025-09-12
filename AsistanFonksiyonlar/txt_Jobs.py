import os
import AnaFonksiyonlar.JSON_jobs as Json





#yeni_id = input("Yeni ID'yi girin: ")

def txteYeniID_Gir(yeni_id):
    txt_dosya_yolu = "VERI/Text.txt"
    txtUzerineYaz(txt_dosya_yolu,yeni_id) 
    


def txtYoksaOlustur(txt_dosya_yolu):  #^  ilk oluşturmada ID ye 0 değeri verdim.
                        
            # 1. Dosya yoksa oluştur ve ID: 0 yaz
            if not os.path.exists(txt_dosya_yolu):
                # Klasör yoksa oluştur
                os.makedirs(os.path.dirname(txt_dosya_yolu), exist_ok=True)
                
                with open(txt_dosya_yolu, "w", encoding="utf-8") as dosya:
                    dosya.write("ID: 0\n")
                print("Dosya oluşturuldu ve ID: 0 yazıldı.")

            # 2. Dosya varsa, normal süreç devam etsin (örneğin ilk satırı güncelle)
            else:
                pass 
                

def txtID_Oku(dosya_yolu):
            # Dosyayı oku
            with open(dosya_yolu, "r", encoding="utf-8") as dosya:
                
                satirlar = dosya.readlines()
                return int(satirlar[0].split(":")[1].strip())

def txtUpdate(txt_dosya_yolu,yeni_id):
            # Dosyayı oku
            with open(txt_dosya_yolu, "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()
            # İlk satırı güncelle
            if satirlar:
                satirlar[0] = f"ID: {yeni_id}\n"
                return satirlar
            else:
                satirlar = [f"ID: {yeni_id}\n"]
                return satirlar


def txtUzerineYaz(txt_dosya_yolu,yeni_id):
     # Geri yaz
        satirlar=txtUpdate(txt_dosya_yolu,yeni_id)
        with open(txt_dosya_yolu, "w", encoding="utf-8") as dosya:
                dosya.writelines(satirlar)
        print("ID,txt_jobs'da  güncellendi.")
        print("ID,txt_jobs'da  güncellendi.SATIR[0]>>", satirlar[0])


if __name__=="__main__":
    txteYeniID_Gir(Json.getLastID)