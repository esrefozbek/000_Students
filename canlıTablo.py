from rich.table import Table
from rich.live import Live
from time import sleep
import VERİ  # içinde TupleliListe_ olan modül


def tablo_olustur(liste: list) -> Table:
    table = Table(title="📋 Öğrenci Tablosu")

    table.add_column("Sıra No", justify="center", style="bold yellow")
    table.add_column("ID", justify="center", style="white")
    table.add_column("Ad", justify="right", style="white")
    table.add_column("Soyad", justify="left", style="white")
    table.add_column("Numarası", justify="left", style="white")
    table.add_column("Doğum Tarihi", justify="center", style="yellow")
    table.add_column("Sınıf", justify="center", style="green")
    table.add_column("Kayıt Tarihi", justify="center", style="white", overflow="crop")

    for sıra, ogrenci in enumerate(liste):
        table.add_row(
            str(sıra + 1),
            str(ogrenci[0]),
            ogrenci[1],
            ogrenci[2],
            ogrenci[3],
            ogrenci[4],
            ogrenci[5],
            ogrenci[6]
        )

    return table


def main():
    liste = VERİ.TupleliListe_

    with Live(tablo_olustur(liste), refresh_per_second=4) as live:
        for _ in range(14):  # 50 kez güncellensin
            sleep(0.5)

            # 🔄 Listeyi sola kaydır
            liste = liste[1:] + [liste[0]]

            # 🔁 Live tabloyu güncelle
            live.update(tablo_olustur(liste))


if __name__ == "__main__":
    main()
