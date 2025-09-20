from faker import Faker
import random
import json
from datetime import datetime

# Türkçe sahte veriler için faker yapılandırması
fake = Faker('tr_TR')

# Öğrenci sayısı
num_students = 71

# Sınıf seviyeleri ve şubeleri
grades = list(range(4, 9))  # 4. sınıftan 8. sınıfa
sections = list("ABCDEFGH")

# Doğum tarihi aralığı (8-13 yaş)
start_date = datetime.now().replace(year=datetime.now().year - 13)
end_date = datetime.now().replace(year=datetime.now().year - 8)

# Öğrenci verileri
students = []

for i in range(1, num_students + 1):
    dogum_tarihi = fake.date_between(start_date=start_date, end_date=end_date)
    sinif = f"{random.choice(grades)}{random.choice(sections)}"
    kayit_tarihi = fake.date_between(start_date=datetime(2025, 9, 1), end_date=datetime(2025, 9, 20))

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

print("✔️ 71 öğrenci verisi başarıyla 'ogrenciler.json' dosyasına kaydedildi.")
