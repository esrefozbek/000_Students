from rich.console import Console;
from rich.panel import Panel
from rich import print as p
import VERI.emptyLists as EMPTY
import Widgetler.randomRenk as RENK
c=Console()

def Mesajlar(sayı:int=0):
    EMPTY.aramaSayisi=0
    
    
    if sayı==0: pass  #= mesajsız geçiş.   
    
    
    if sayı==1:   #=   BUL    
        if EMPTY.aramaSayisi<1:  
            c.print(Panel.fit(f"""✅✅[cornsilk1 on navy_blue] Aradığın talebelerin numarasını, adını ya da soyadını gir [/][italic tan on grey15] Menü için [bold orange_red1]Esc 📌[/] [/]""", style="deep_sky_blue1"),end="")
            p("[red]↳ ↳⚡⚡ Esc[/][grey30] or[/][bold sea_green2] first Search[/] ➡️ ", end="", flush=True)
            EMPTY.aramaSayisi+=1            
        else: 
            if EMPTY.bul:
                Mesajlar(sayı=11)
    
    
    if sayı==11:
         p("🤝🤝[gold1]@[/][turquoise2]Bul[/] [bold red3] Esc[/][grey30] or[/][bold sea_green2] new Search[/] ➡️ ", end="\n", flush=True)
    
            
        
    if sayı==2:    #=   SİLME    
        if EMPTY.aramaSayisi<1:
            p(Panel.fit("⏳⏳ 📌 [tan on dark_red] Silinecek talebelerin numarasını, adını ya da soyadını gir [/][italic tan] Menü için [bold orange_red1]Esc[/][/]", style="red"),end="")
            p("🤝🤝[red] Esc[/][grey30] or[/][bold sea_green2] first Search[/] 🚢🚢💙➡️ ", end="", flush=True)
            EMPTY.aramaSayisi+=1
        else:
            p("📌 [bright_white on red] Silinecek talebelerin numarasını, adını ya da soyadını gir [/]")
            p("[gold1]@[/][turquoise2]Sil[/] [bold red3] Esc[/][grey30] or[/][bold sea_green2] new Search[/] ➡️ ", end="", flush=True)
            
            
            
    if sayı==22:
            c.print("@ Sil :Silinmesini istediğiniz ID NUMARALARINI girin ya da ESC ile yeni arama ya da Anamenüye çıkış yapın ➡️ ",end="\n")
            
            """  if EMPTY_LISTS.sil:
                print("[bold red3] Esc[/][grey30] or[/][bold sea_green2] Id[/] [yellow1] [/] ", end="", flush=True)
          """
         
         
            
    if sayı==4:
        metin1=f"""[yellow]Silinecek öğrencilerin numaralarını girin. Sayıları boşluk veya virgül ile ayırabilirsiniz.[/]        
    [bold magenta]Geçerli aralık:[/] 0 - {len(EMPTY.TekKriterinBulunanlari) - 1} 
    """  
    
 
    if sayı==6:
        metin1=f"""[yellow]Silinecek öğrencilerin Id numaralarını girin. '\\s' veya ',' ile ayırabilirsiniz.[/]        
        [bold magenta]Geçerli aralık:[/] 0 - {len(EMPTY.TekKriterinBulunanlari) - 1} 
        """  
        
    if sayı==7:    
        metin2=f""" [bold white][italic yellow] Lütfen bu sefer dikkatli ol, Tanrı aşkına![/italic yellow] 🙏  Geçerli aralık:[bold yellow] 0 - {len(EMPTY.TekKriterinBulunanlari) - 1} [/] [/] """
        
  
 
    if sayı== 8 : # =   YENİKAYIT    
        EMPTY.renk=RENK.randomRENK()
        mesaj=f"➕➕✨🌿 [bright_white]Öğrencinin;[/]\n[{EMPTY.renk}]\t↳ ↳ ADI             >[/{EMPTY.renk}] "
        
        if EMPTY.aramaSayisi<1:
            c.print(Panel.fit(f"🔔🔔📝[bold][{RENK.randomRENK()} on {RENK.randomRENK()}] Yeni Öğrenci Girişi [/][/][italic grey30]  Anamenü'ye [bold {RENK.randomRENK()}]Esc[/] ile dönebilirsin.[/]📌", border_style=f"{RENK.randomRENK()}"), end="")
            EMPTY.aramaSayisi+=1
            c.print(mesaj,end="",)    
        else:
            c.print(mesaj,end="",)

    if sayı==9:
        c.print(f"➕➕✨🌿 [bright_white]Öğrencinin;[/]\n[{EMPTY.renk}]\t↳ ↳ SOYADI          >[/{EMPTY.renk}] ",end="")
     
     
     
    if sayı==10: #/       parsedKriterStringi_Listesi             
        p(Panel.fit(str(EMPTY.KellesiGidenlerin_Listesi), title=" KellesiGidenler_Listesi ",     style="white"))   
   
   
   
   
   
   
   
   
   
   
   
   
    