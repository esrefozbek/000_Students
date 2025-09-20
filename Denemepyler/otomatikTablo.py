from rich.table import Table
from rich.console import Console

# Console nesnesi
console = Console()

# Tek satırlık veri (bir sözlük)
ogrenci = {
    "Id": 1,
    "Ad": "Zeynep",
    "Soyad": "Karakurt",
    "Numara": "1654",
    "Doğum Tarihi": "12/03/2010",
    "Sınıf": "6A",
    "Kayıt Tarihi": "02/09/2025"
}

# Tablo oluştur
table = Table(title="Öğrenci Bilgisi")

# Sütunları ekle (sözlük anahtarları)
for key in ogrenci.keys():
    table.add_column(key, style="cyan", no_wrap=True)

# Veriyi satır olarak ekle
table.add_row(*ogrenci.values())

# Tabloyu yazdır
console.print(table)
