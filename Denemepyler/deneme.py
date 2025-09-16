print("bir", "iki", "üç", "dört", "on dört", sep="mumdur", end=None )

import os
print(os.getcwd())


import sys
sys.stdout.writelines("Eşref ")

f = open("kişisel_bilgiler.txt", "w")

print("ne545asdasdasdasd464rede", file=f, flush=True)
f.close()
 
 
print(*"dallama",sep="-")


print("saddsa"\
    "1231231231"    )

sayı1=1
sayı2=2

sayı1,sayı2=sayı2,sayı1

print("sayı1>>",sayı1,"sayı2>>",sayı2)

print("="*60)
import keyword
#^print(keyword.kwlist)
import rich
rich.print("Hello, [bold magenta]World[/bold magenta]!")


başlık="Eşref ÖZBEK"
print(başlık, "\n", "-"*len(başlık), sep="")

print("\a"*10)
print(help())
import this
print(this.s)
personelINFO=open("kişisel_bilgiler.txt", "w")

