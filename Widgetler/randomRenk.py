import json
import time
import random
import re
from rich.live import Live
from rich.console import Console

console = Console()

import re
import json

def renkleriAl(): # renkleri al json'a yaz
    renkler = []
    with open("VERI/renk.txt", "r", encoding="utf-8") as dosya:
        for line in dosya:
            eslesme = re.search(r'"(.*?)"', line)
            if eslesme:
                renkler.append(eslesme.group(1))

    # JSON'a yazma işlemi
    with open("VERI/renkler.json", "w", encoding="utf-8") as json_dosya:
        json.dump({"renkler": renkler}, json_dosya, ensure_ascii=False, indent=4)
    return tuple(renkler)





def renkleriJsondanOku(dosya_adi="VERI/renkler.json"):
    with open(dosya_adi, "r", encoding="utf-8") as json_dosya:
        veri = json.load(json_dosya)
        return tuple(veri["renkler"])



# Rastgele renk seç
def randomize(birTuple):
    return random.choice(birTuple)



# Öğrenci bulunamadı mesajı animasyonu
def ogrenciYok():
    renkler=renkleriJsondanOku(dosya_adi="VERI/renkler.json")
    metin_taban = "Bu kayıtta bir öğrenci bulunamadı."
    with Live("", refresh_per_second=2, console=console) as live:
        for i in range(2):    
            for renk in renkler:
                if "grey" in renk:
                    metin = f"[{renk}]{metin_taban}[/]"
                    time.sleep(0.04)
                    live.update(metin)
               

# # Test amaçlı çalıştırma (doğrudan çalıştırıldığında)
# if __name__ == "__main__":
#     renkler = renkleriAl()
#     metin = f"[{randomize(renkler)}]Bu kayıtta bir öğrenci bulunamadı.[/]"
#     print(metin)
#     time.sleep(0.1)

#     print("\n\n")

#     metin_taban = "Bu kayıtta bir öğrenci bulunamadı."
#     with Live("", refresh_per_second=2, console=console) as live:
#         for _ in range(1):
#             renk = randomize(renkler)
#             metin = f"[{renk}]{metin_taban}[/]"
#             live.update(metin)
#             time.sleep(0.1)

#     print("\n\n")

#     # Tek tek tüm renklerle göster
#     with Live("", refresh_per_second=2, console=console) as live:
#         for renk in renkler:
#             metin = f"[{renk}]Bu kayıtta bir öğrenci bulunamadı.[/]"
#             live.update(metin)
#             time.sleep(0.05)
