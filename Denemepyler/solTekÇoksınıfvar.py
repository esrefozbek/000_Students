from rich.console import Console
from rich.table import Table

def gruplu_tablo(sol_sutun_etiketi: str, diger_sutunlar: list[str], gruplar: dict[str, dict[str, list[str]]]):
    """
    Birden fazla grubu tek tabloda gösterir. Sol sütun grup adı olur.

    Args:
        sol_sutun_etiketi: Grup başlığı (örneğin "Sınıf")
        diger_sutunlar: Sağ sütun başlıkları (örneğin ["Ad", "Numara"])
        gruplar: {
            "5A": {"Ad": [...], "Numara": [...]},
            "5B": {"Ad": [...], "Numara": [...]}
        }
    """
    console = Console()
    table = Table(show_header=True, header_style="bold green")

    table.add_column(sol_sutun_etiketi, justify="center")
    for sutun in diger_sutunlar:
        table.add_column(sutun, justify="left")

    for grup_adi, veri in gruplar.items():
        satirlar = [ "\n".join(veri.get(sutun, [])) for sutun in diger_sutunlar ]
        table.add_row(grup_adi, *satirlar)

    console.print(table)



veriler = {
    "5A": {
        "Ad": ["Zeynep", "Ali"],
        "Numara": ["101", "102"]
    },
    "5B": {
        "Ad": ["Elif", "Mehmet", "Ayşe"],
        "Numara": ["201", "202", "203"]
    },
    "6A": {
        "Ad": ["Burak"],
        "Numara": ["301"]
    }
}

gruplu_tablo("Sınıf", ["Ad", "Numara"], veriler)
