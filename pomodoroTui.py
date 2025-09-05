# pomodoro_tui.py

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.reactive import reactive
from textual.containers import Container
import asyncio

class PomodoroApp(App):

    CSS_PATH = None  # Gerekirse stil tanımı

    kalan_saniye = reactive(25)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("🍅 Pomodoro Zamanlayıcısı", id="baslik"),
            Static(id="sayac"),
        )
        yield Footer()

    async def on_mount(self):
        await self.geri_say(25)

    async def geri_say(self, dakika: int):
        self.kalan_saniye = dakika * 60
        sayac = self.query_one("#sayac", Static)

        while self.kalan_saniye > 0:
            dakika, saniye = divmod(self.kalan_saniye, 60)
            sayac.update(f"[b cyan]Kalan süre:[/b cyan] {dakika:02d}:{saniye:02d}")
            await asyncio.sleep(1)
            self.kalan_saniye -= 1

        sayac.update("[b green]⏰ Süre doldu! Molaya çık.[/b green]")

if __name__ == "__main__":
    app = PomodoroApp()
    app.run(inline=True)
