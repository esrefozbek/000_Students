import VERI.emptyLists as EMPTY_LISTS
from rich.panel import Panel
from rich.console import Console;c = Console()
from rich import print as p

aramaSayısı=0
def Mesajlar(sayı:int=0):
    global aramaSayısı
        
    if sayı==0: pass
    if sayı==1:
        if aramaSayısı<1:  #=   BUL    
            c.print(Panel.fit(f"""📌
[cornsilk1 on navy_blue] Aradığın talebelerin numarasını, adını ya da soyadını gir  [/]
[italic tan on grey23]  {" "*24}Menüye dönmek için [bold orange_red1]Esc[/] tuşuna bas.[/]""", style="deep_sky_blue1"),end="")
            p("[gold1]@[/][turquoise2]Bul[/] [bold red3] Esc[/][grey30] or[/][bold sea_green2] first Search[/] ➡️ ", end="", flush=True)            
        else: 
            if EMPTY_LISTS.bul:
                p("[gold1]@[/][turquoise2]Bul[/] [bold red3] Esc[/][grey30] or[/][bold sea_green2] new Search[/] ➡️ ", end="", flush=True)
            
        
    if sayı==2:    #=   SİLME    
        if aramaSayısı<1:
            p(Panel.fit(f"📌 [bright_white on red] Silinecek talebelerin numarasını, adını ya da soyadını gir [/] \n[italic tan]   Menüye dönmek için [bold orange_red1]Esc[/] tuşuna bas.[/]", style="red"),end="")
        else:
            p("silmek mi istiyorsun  O halde ad soyad id numara vb. gir ➡️ ")
            
            
    if sayı==22:
            c.print("@ Sil :Silinmesini istediğiniz ID NUMARALARI ➡️ ",end="")
            if EMPTY_LISTS.sil:
                print("[bold red3] Esc[/][grey30] or[/][bold sea_green2] Id[/] [yellow1] [/] ", end="", flush=True)
         
         
         
    if sayı==3:
        if aramaSayısı<11:
           c.print("\n[yellow]Öğrencinin;[/]\n[green]\tADI[/][grey30] || [red1]Esc[/][/grey30]",end=" ➡️ ")
           """ else:
            if EMPTY_LISTS.sil:
                print("@      Sil?? : [bold red3] Esc[/][grey30] or[/][bold sea_green2] new[/] [yellow1]➡️ [/] ", end="", flush=True)   
         """
            
    if sayı==4:
        metin1=f"""[yellow]Silinecek öğrencilerin numaralarını girin. Sayıları boşluk veya virgül ile ayırabilirsiniz.[/]        
    [bold magenta]Geçerli aralık:[/] 0 - {len(EMPTY_LISTS.Bulunanlar) - 1} 
    """  
    
 
    if sayı==6:
        metin1=f"""[yellow]Silinecek öğrencilerin Id numaralarını girin. '\\s' veya ',' ile ayırabilirsiniz.[/]        
        [bold magenta]Geçerli aralık:[/] 0 - {len(EMPTY_LISTS.Bulunanlar) - 1} 
        """  
        
    if sayı==7:    
        metin2=f""" [bold white][italic yellow] Lütfen bu sefer dikkatli ol, Tanrı aşkına![/italic yellow] 🙏  Geçerli aralık:[bold yellow] 0 - {len(EMPTY_LISTS.Bulunanlar) - 1} [/] [/] """
   
   
   
   
   
   
   
   
   
   
   
   
   
    aramaSayısı+=1