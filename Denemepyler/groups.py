from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text

console = Console()

panel1 = Panel(Text("Birinci Panel"))
panel2 = Panel(Text("İkinci Panel"))

group = Group(panel1, panel2)

console.print(group)  # ✅ İkisini arka arkaya yazdırır


mesaj1="eşrref"
mesaj2="merhaba oolum"
sayi1=232423

group2=Group(mesaj1,mesaj2)
console.print(group2)






    
    
    
    # file: textual_dashboard.py

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static
from rich.table import Table
from rich.panel import Panel


class DashboardApp(App):
    """Textual tabanlı örnek dashboard uygulaması."""

    def compose(self) -> ComposeResult:
        # 1. Görev tablosu (Rich ile)
        task_table = Table(title="Görevler")
        task_table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        task_table.add_column("Açıklama", style="magenta")
        task_table.add_column("Durum", justify="center", style="green")

        task_table.add_row("1", "API bağlantısı", "✅ Tamamlandı")
        task_table.add_row("2", "Veri çekiliyor", "⏳ Bekleniyor")
        task_table.add_row("3", "Rapor oluşturuluyor", "❌ Hatalı")

        # Table'ı bir panel içine al
        task_panel = Panel(task_table, title="Görev Tablosu", border_style="blue")

        # 2. Log paneli (Rich Panel içinde metin)
        log_panel = Panel(
            "[bold yellow]İşlem 1 tamamlandı\nİşlem 2 devam ediyor...[/bold yellow]",
            title="Log Paneli",
            border_style="green"
        )

        # Layout: yatay 2 parçaya böl
        yield Horizontal(
            Static(task_panel, expand=True),
            Static(log_panel, expand=True)
        )


if __name__ == "__main__":
    DashboardApp().run()
