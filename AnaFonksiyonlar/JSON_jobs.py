#breakpoint()
import VERI.emptyLists as EmptyLists,Widgetler.SayacAnimasyon.sayacKronometre as Say_Kro
import json, os
from rich import print
import Widgetler.SayacAnimasyon.spinner as SpinnerPY
import VERI.emptyLists as AtEmptyLists
import AsistanFonksiyonlar.txt_Jobs as TxtYolu
from rich.console import Console; c = Console()

jsonDosya_adi = ("VERI/students.json")
txt_dosya_yolu = "VERI/Text.txt"
AtEmptyLists.Jsonda_Mevcut_Veriler=[]
mev_DATA=AtEmptyLists.Jsonda_Mevcut_Veriler

#&            JSON DOSYASINDAN LİSTEYİ import etmek                     
            
def JSONdanImport():
        if not os.path.exists(jsonDosya_adi):
            print(f"⚠️ '{jsonDosya_adi}' dosyası bulunamadı. Henüz veri kaydedilmemiş olabilir.")
            return
       
        with open(jsonDosya_adi, "r", encoding="utf-8") as file:
            Geçici_SozlukListesi = json.load(file)
      
        c.print("\njson:import:Geçici_SozlukListesi[-2:]>>",Geçici_SozlukListesi[-2:])       
        EmptyLists.Jsonda_Mevcut_Veriler.clear() 
        
        import copy
        EmptyLists.Jsonda_Mevcut_Veriler =copy.deepcopy(Geçici_SozlukListesi)
      

#&             KayıtOncesiCTRL_theFilesExist_Or                     
def CTRLforFilesExist(jsonDosya_adi: str ):# bunu teknik menüye al  Ayrıca Asisstan fonksiyonnlara taşı.
    global getLastJSON_ID, getTextID 
    try:
        with open(jsonDosya_adi, "r", encoding="utf-8") as f:
            AtEmptyLists.Jsonda_Mevcut_Veriler = json.load(f)
            getLastJSON_ID = AtEmptyLists.Jsonda_Mevcut_Veriler[-1]["Id"] if AtEmptyLists.Jsonda_Mevcut_Veriler else 0   #NOTE -  

            if not os.path.exists(txt_dosya_yolu):
                getTextID = TxtYolu.txtOlustur(txt_dosya_yolu)  #txtOlustur
            else: 
                getTextID = TxtYolu.txtID_Oku(txt_dosya_yolu)   #txtID_Oku 
        c.print("JSON::CTRLforExistance::try:: Jsonda_Mevcut_Veriler [-1] ",AtEmptyLists.Jsonda_Mevcut_Veriler[-1] )                
        return  AtEmptyLists.Jsonda_Mevcut_Veriler, getLastJSON_ID, getTextID
    
    
    except (FileNotFoundError, json.JSONDecodeError):
        AtEmptyLists.Jsonda_Mevcut_Veriler = []
        getLastJSON_ID = 0
        TxtYolu.txtOlustur("VERI/Text.txt")
        getTextID = 0
        c.print("JSON::CTRLforExistance::except:: Jsonda_Mevcut_Veriler [0]",AtEmptyLists.Jsonda_Mevcut_Veriler[0] )                
        return  AtEmptyLists.Jsonda_Mevcut_Veriler, getLastJSON_ID,  getTextID
    

#&                 ID uyum kontrol              
def CTRLforID(JSON_ID, TextID, ilaveSozluk):# bunu teknik menüye al  Ayrıca Asisstan fonksiyonnlara taşı.
   # global getLastJSON_ID, getTextID
    degisimMiktari=len(ilaveSozluk)
   
    if TextID!=(JSON_ID + degisimMiktari):
        c.print("\n⚠️[yellow]ID çatışması tespit edildi. Biraz belkle, düzeltip geliyorum.[/]")
        return tamiratForID(JSON_ID,ilaveSozluk)
    else:
        c.print("")
        return JSON_ID,ilaveSozluk
    
    
#&  TAMİRAT  # bunu teknik menüye al Ayrıca Asistan fonksiyonnlara taşı.   
def tamiratForID(getLastJSON_ID,ilaveSozluk): 
    for i in ilaveSozluk: #yeni eklenen sözlükler TXT ten Id aldıkları için ID leri hatalı olabilir. Json'da kayıtlı ID'ye göre ...
            getLastJSON_ID+=1
            i["Id"]=getLastJSON_ID 
            TxtYolu.txtUzerineYaz("VERI/Text.txt", getLastJSON_ID)
    
    SpinnerPY.spinner(2,3)      # bu tamir süreci  ayrı yapılabilir. 
    return AtEmptyLists.Jsonda_Mevcut_Veriler, ilaveSozluk, getLastJSON_ID, getTextID


#&                   Sözlüğe Ekleme                   
def SozlugeEkleme(JSON_Dosyasi: str, FARK_SozlukListesi: list):
    #degisimMiktari=len(YeniEklenenlerinSozluklerListesi_)
    ReturnedDatas=CTRLforFilesExist(JSON_Dosyasi)  #! ReturnedDatas[0]:AtEmptyLists.Jsonda_Mevcut_Veriler
    c.print("JSON::EKLEME:: Jsonda_Mevcut_Veriler [-2:]>>",ReturnedDatas[0][-2:])
    a= CTRLforID(ReturnedDatas[1],ReturnedDatas[2],FARK_SozlukListesi,)
    ReturnedDatas[0].extend(FARK_SozlukListesi)
    getLastJSON_ID = ReturnedDatas[0][-1]["Id"]
 
    EmptyLists.FARK_TupleListesi.clear()
    SpinnerPY.spinner(2,1)      
   #^ Jsonda_Mevcut_Veriler = []
   
    JsonaDump(ReturnedDatas[0])  
    c.print(f" {len(FARK_SozlukListesi)} öğrencinin bilgileri [green]JSON[/]'a kaydedildi.\n")
    c.print("JSON::EKLEME:: Jsonda_Mevcut_Veriler [-1:]>>",ReturnedDatas[0][-1:])
    return ReturnedDatas[0]



#&                    Jsonda_Mevcut_Verilerden Silme                  
def SozluktenEksiltme(jsonSozluk, silineceklerListesi):
  
    for item in silineceklerListesi:
      jsonSozluk.remove(item)

    getLastJSON_ID =jsonSozluk[-1]["Id"]  #^ mevcut değilse ??
    getTextID = TxtYolu.txtID_Oku(txt_dosya_yolu) #^ mevcut değilse ??

   #^ Jsonda_Mevcut_Veriler = []
    SpinnerPY.spinner(3,2)  
    JsonaDump(jsonSozluk)    
    c.print(f" 200 öğrencinin bilgileri [red]JSON[/]'dan silindi.\n")
    
    return jsonSozluk 
    
    
    
    

#&              Jsonda_Mevcut_Veriler'i JSON'a Dump                     

def JsonaDump(mevcut_Veriler):
    with open(jsonDosya_adi, "w", encoding="utf-8") as f:
        json.dump(mevcut_Veriler, f, indent=4, ensure_ascii=False)
        
        
 