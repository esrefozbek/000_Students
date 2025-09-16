import json
from rich.console import Console; c = Console()
from rich.prompt import Prompt
from rich.panel import Panel





# name = Prompt.ask("Enter your name", default="Paul Atreides")

with open("VERI/students copy.json", "r") as jsonFile:
    mevcut_veriler = json.load(jsonFile)
    c.print("mevcut_veriler   tipi: ", type(mevcut_veriler))
    # mevcut_veriler=dict(mevcut_veriler)




sözlük =mevcut_veriler[0]

def şekilliSözlük(oneDict):    
    c.print("[bold yellow]{[/]")
    for i in range(len(oneDict)):
                keylistesiTuple=tuple(oneDict.keys())
                c.print(f" '{keylistesiTuple[i]}': {oneDict[keylistesiTuple[i]]}         ")
    c.print("[bold yellow]}[/]")
    
sonuc=şekilliSözlük(sözlük)   
    
c.print(sonuc  ) 
  
  
    
    
