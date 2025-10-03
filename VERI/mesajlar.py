import VERI.emptyLists as E_LISTS
from rich.panel import Panel
from rich.console import Console;c = Console()
from rich import print as p
import Widgetler.randomRenk as RR

def Mesajlar(sayı:int=0):
    E_LISTS.aramaSayisi=0
    
    
    if sayı==0: pass  #= mesajsız geçiş.   
    
    
    if sayı==1:   #=   BUL    
        if E_LISTS.aramaSayisi<1:  
            c.print(Panel.fit(f"""✅✅[cornsilk1 on navy_blue] Aradığın talebelerin numarasını, adını ya da soyadını gir [/][italic tan on grey15] Menü için [bold orange_red1]Esc 📌[/] [/]""", style="deep_sky_blue1"),end="")
            p("[red]↳ ↳⚡⚡ Esc[/][grey30] or[/][bold sea_green2] first Search[/] ➡️ ", end="", flush=True)
            E_LISTS.aramaSayisi+=1            
        else: 
            if E_LISTS.bul:
                Mesajlar(sayı=11)
    
    
    if sayı==11:
         p("🤝🤝[gold1]@[/][turquoise2]Bul[/] [bold red3] Esc[/][grey30] or[/][bold sea_green2] new Search[/] ➡️ ", end="\n", flush=True)
    
            
        
    if sayı==2:    #=   SİLME    
        if E_LISTS.aramaSayisi<1:
            p(Panel.fit("⏳⏳ 📌 [tan on dark_red] Silinecek talebelerin numarasını, adını ya da soyadını gir [/][italic tan] Menü için [bold orange_red1]Esc[/][/]", style="red"),end="")
            p("🤝🤝[red] Esc[/][grey30] or[/][bold sea_green2] first Search[/] 🚢🚢💙➡️ ", end="", flush=True)
            E_LISTS.aramaSayisi+=1
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
    [bold magenta]Geçerli aralık:[/] 0 - {len(E_LISTS.TekKriterinBulunanlari) - 1} 
    """  
    
 
    if sayı==6:
        metin1=f"""[yellow]Silinecek öğrencilerin Id numaralarını girin. '\\s' veya ',' ile ayırabilirsiniz.[/]        
        [bold magenta]Geçerli aralık:[/] 0 - {len(E_LISTS.TekKriterinBulunanlari) - 1} 
        """  
        
    if sayı==7:    
        metin2=f""" [bold white][italic yellow] Lütfen bu sefer dikkatli ol, Tanrı aşkına![/italic yellow] 🙏  Geçerli aralık:[bold yellow] 0 - {len(E_LISTS.TekKriterinBulunanlari) - 1} [/] [/] """
        
  
 
    if sayı== 8 : # =   YENİKAYIT    
        E_LISTS.renk=RR.randomRENK()
        if E_LISTS.aramaSayisi<1:
            
            c.print(Panel.fit("🔔🔔[bold][yellow2]📝 Yeni Öğrenci Girişi [/][/][italic grey30]  Anamenü'ye [bold orange_red1]Esc[/] ile dönebilirsin.[/]📌", border_style="green_yellow"), end="")
            
            c.print(f"➕➕✨🌿 [bright_white]Öğrencinin;[/]\n[{E_LISTS.renk}]\t↳ ↳ ADI             >[/{E_LISTS.renk}] ",end="")
                      
            E_LISTS.aramaSayisi+=1
        else:
             c.print(f"✨🌿🔔🔔[bright_white]Öğrencinin;[/]\n[{E_LISTS.renk}]\t ↳ ↳ ADI             >[/{E_LISTS.renk}] ",end="")
    
    
     
        if sayı==10: #/       parsedKriterStringi_Listesi             
           p(Panel.fit(str(E_LISTS.KellesiGidenler_Listesi), title=" KellesiGidenler_Listesi ",     style="white"))   
   
   
   
   
   
   
   
   
   
   
   
   
    