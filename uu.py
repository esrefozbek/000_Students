# Önce gerekli kütüphaneleri yükleyin:
# pip install textual rich pillow

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static
from rich.panel import Panel
from rich.text import Text
from PIL import Image

class TerminalApp(App):
    CSS = """
    Screen {
        background: black;
    }
    #terminal {
        background: url("background.jpg");  # Arka plan resmi
        background-size: cover;
        padding: 1;
        border: round yellow;
    }
    """

    def compose(self) -> ComposeResult:
        # Terminal paneli
        yield Container(
            Static(
                Panel(
                    Text("Python Terminal Simülasyonu\nRich + Textual ile", justify="center", style="bold white"),
                    title="Terminal",
                    border_style="bright_blue"
                ),
                id="terminal"
            )
        )

    async def on_key(self, event):
        # Esc tuşuna basınca uygulamayı kapat
        if event.key == "escape":
            await self.action_quit()

if __name__ == "__main__":
    TerminalApp().run()
