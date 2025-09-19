from rich.console import Console
from rich.table import Table

def tek_sutunlu_grup_tablo(sol_sutun_etiketi: str, diger_sutunlar: list[str], veri: dict[str, list[str]], sol_sutun_degeri: str):
    """
    Bir sol sütun tek bir veri içerir, sağ sütunlar çok satırlı veri içerir.

    Args:
        sol_sutun_etiketi: Tablo başlığı (örneğin "Sınıf")
        diger_sutunlar: Sağ sütun başlıkları listesi (örneğin ["Ad", "Numara"])
        veri: Sağ sütunların verileri dict olarak {"Ad": [...], "Numara": [...]}
        sol_sutun_degeri: Sol sütunda gösterilecek sabit değer (örneğin "5A")

    Örnek:
        tek_sutunlu_grup_tablo(
            "Sınıf",
            ["Ad", "Numara"],
            {"Ad": ["Ali", "Veli"], "Numara": ["123", "456"]},
            "5A"
        )
    """
    console = Console()
    table = Table(show_header=True, header_style="bold green")

    table.add_column(sol_sutun_etiketi, justify="center")
    for sutun in diger_sutunlar:
        table.add_column(sutun, justify="left")

    # Her sütun için alt alta yazılacak içerikler '\n' ile birleştirilir
    satirlar = [ "\n".join(veri[sutun]) for sutun in diger_sutunlar ]

    table.add_row(sol_sutun_degeri, *satirlar)
    console.print(table)



tek_sutunlu_grup_tablo(
    "Sınıf",
    ["Ad", "Numara"],
    {
        "Ad": ["Zeynep", "Ali", "Elif", "Mehmet"],
        "Numara": ["123", "124", "125", "126"]
    },
    "5A"
)
