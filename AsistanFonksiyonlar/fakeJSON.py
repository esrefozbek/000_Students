from faker import Faker
import random
import json
from datetime import datetime
from rich.console import Console; c = Console()




def fakeOgrenciOlustur():
    # Türkçe sahte veriler için faker yapılandırması



    # Farklı diller için faker nesneleri
    faker_tr = Faker("tr_TR")
    faker_en_gb = Faker("en_GB")
    faker_de = Faker("de_DE")
    faker_in = Faker("en_IN")  # Hint İngilizcesi
    faker_us = Faker("en_US")
    faker_is=Faker("is_IS")
    faker_ru=Faker("ru_RU")
    faker_fr=Faker("fr_FR")
    faker_it=Faker("it_IT") 
    
    

    # Farklı faker’ları listeye koy
    fakers = [
        faker_tr,
        faker_en_gb,
        faker_de,
        faker_in,
        faker_us,
        faker_is,
        faker_ru,
        faker_fr,
        faker_it
    ]

    c.print(" Kaç öğrenci oluşturayım >> ", end="")
    sayi=int(input())
    
    # Öğrenci sayısı
    num_students = sayi

    # Sınıf seviyeleri ve şubeleri
    grades = list(range(5, 8))  # 4. sınıftan 8. sınıfa
    sections = list("ABCDEFGH")

    # Doğum tarihi aralığı (8-13 yaş)
    start_date = datetime.now().replace(year=datetime.now().year - 13)
    end_date = datetime.now().replace(year=datetime.now().year - 8)

    # Öğrenci verileri
    students = []

    for i in range(1, num_students + 1):
        fake = random.choice(fakers) 
        dogum_tarihi = fake.date_between(start_date=start_date, end_date=end_date)
        sinif = f"{random.choice(grades)}{random.choice(sections)}"
        kayit_tarihi = fake.date_between(start_date=datetime(2018, 7, 1), end_date=datetime(2026, 9, 20))

        students.append({
            "Id": i,
            "ad": fake.first_name(),
            "soyad": fake.last_name(),
            "ogrenciNumarasi": str(1000 + i),
            "dogumTarihi": dogum_tarihi.strftime("%d/%m/%Y"),
            "sinifi": sinif,
            "kayitTarihi": kayit_tarihi.strftime("%d/%m/%Y")
        })

    # Veriyi JSON dosyasına kaydet
    with open("VERI/students.json", "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

    c.print(f" ✔️  {num_students} [bold red]öğrenci verisi başarıyla [yellow]'VERI/students.json'[/] dosyasına kaydedildi.[/]")
