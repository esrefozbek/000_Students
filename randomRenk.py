import time
import random
from rich.live import Live
from rich.box import Box

from rich.console import Console

console = Console()
import time,sys
from rich import print
import re,random



with open("renk.txt", "r", encoding="utf-8") as dosya:
    renkler = []

    for line in dosya:
        eslesme = re.search(r'"(.*?)"', line)
        if eslesme:
            renkler.append(eslesme.group(1))


renkler = tuple(renkler)

print(renkler)

def Renkler():
    return renkler


def randomize(birTuple):
    oltada=random.choice(birTuple)
    return oltada


for i in range(1):
    renk = randomize(Renkler())
    metin = f"[{renk}]Bu kayıtta bir öğrenci bulunamadı.[/]"
    print(metin)
    time.sleep(0.1)
    
print("\n\n")


for i in range(1):
        for renk in renkler:
           # if renkler.index(renk)>230:
                metin = f"[{renk}]Bu kayıtta bir öğrenci bulunamadı.[/]"
                print(metin)
                time.sleep(0.01)
                                                
print("\n\n")








metin_taban = "Bu kayıtta bir öğrenci bulunamadı."
with Live("", refresh_per_second=2, console=console) as live:
    for _ in range(1):
        renk = randomize(Renkler())
        metin = f"[{renk}]{metin_taban}[/]"
        live.update(metin)
        time.sleep(0.1)

print("\n\n")




metin_taban = "Bu kayıtta bir öğrenci bulunamadı."
with Live("", refresh_per_second=2, console=console) as live:
    for renk in renkler:
            metin = f"[{renk}]Bu kayıtta bir öğrenci bulunamadı.[/]"
            live.update(metin)
            time.sleep(0.05)






def ogrenciYok():    
    metin_taban = "Bu kayıtta bir öğrenci bulunamadı."
    with Live("", refresh_per_second=2, console=console) as live:
        for renk in renkler:
                metin = f"[{renk}]Bu kayıtta bir öğrenci bulunamadı.[/]"
                time.sleep(0.01)
                live.update(metin)
                time.sleep(0.1)


