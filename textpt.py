from rich.console import Console
from rich.text import Text

console = Console()
text = Text("Hello, World!")
text.stylize("bold magenta", 0, 6)
console.print(text)




text = Text()
text.append("Hello", style="bold magenta")
text.append(" World!")
console.print(text)





text = Text.from_ansi("\033[1;35mHello\033[0m, World!")
console.print(text.spans)




from rich import print
from rich.panel import Panel
from rich.text import Text
panel = Panel(Text("Hello", justify="right"))
print(panel)




from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

class EmailHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    base_style = "example."
    highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]


theme = Theme({"example.email": "bold yellow"})
console = Console(highlighter=EmailHighlighter(), theme=theme)
console.print("Send funds to money@example.org")




from random import randint

from rich import print
from rich.highlighter import Highlighter


class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({randint(16, 255)})", index, index + 1)


rainbow = RainbowHighlighter()
print(rainbow("I must not fear. Fear is the mind-killer."))




from rich.pretty import pprint
pprint(locals())




from rich import print
from rich.pretty import Pretty
from rich.panel import Panel

pretty = Pretty(locals())
panel = Panel(pretty)
print(panel)




class Bird:
    def __init__(self, name, eats=None, fly=True, extinct=False):
        self.name = name
        self.eats = list(eats) if eats else []
        self.fly = fly
        self.extinct = extinct

    def __repr__(self):
        return f"Bird({self.name!r}, eats={self.eats!r}, fly={self.fly!r}, extinct={self.extinct!r})"

BIRDS = {
    "gull": Bird("gull", eats=["fish", "chips", "ice cream", "sausage rolls"]),
    "penguin": Bird("penguin", eats=["fish"], fly=False),
    "dodo": Bird("dodo", eats=["fruit"], fly=False, extinct=True)
}
print(BIRDS)




def __rich_repr__(self):
    yield self.name
    yield "eats", self.eats
    yield "fly", self.fly, True
    yield "extinct", self.extinct, False
    
    
    
    
import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")




import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

log = logging.getLogger("rich")
try:
    print(1 / 0)
except Exception:
    log.exception("unable print!")
    
    
    
    
import click
import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])]
)




from rich.prompt import Prompt
name = Prompt.ask("Enter your name")




import os
import sys
from rich import print
from rich.columns import Columns

if len(sys.argv) < 2:
    print("Usage: python columns.py DIRECTORY")
else:
    directory = os.listdir(sys.argv[1])
    columns = Columns(directory, equal=True, expand=True)
    print(columns)
    
    
    
    
    

"""
This example shows how to display content in columns.

The data is pulled from https://randomuser.me
"""

import json
from urllib.request import urlopen

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


def get_content(user):
    """Extract text from user dict."""
    country = user["location"]["country"]
    name = f"{user['name']['first']} {user['name']['last']}"
    return f"[b]{name}[/b]\n[yellow]{country}"


console = Console()


users = json.loads(urlopen("https://randomuser.me/api/?results=30").read())["results"]
console.print(users, overflow="ignore", crop=False)
user_renderables = [Panel(get_content(user), expand=True) for user in users]
console.print(Columns(user_renderables))




MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)




from rich import print
from rich.padding import Padding
test = Padding("Hello", (2, 4))
print(test)




import time

from rich.progress import Progress

with Progress() as progress:

    task1 = progress.add_task("[red]Downloading...", total=1000)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)
        
        
        
        
        
from rich.console import Console
from rich.syntax import Syntax

console = Console()
with open("syntax.py", "rt") as code_file:
    syntax = Syntax(code_file.read(), "python")
console.print(syntax) 



from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies",show_lines=True,show_footer=True, )

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta",vertical="middle")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)





from rich import print
from rich.table import Table

grid = Table.grid(expand=True)
grid.add_column()
grid.add_column(justify="right")
grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")

print(grid)






"""Lite simulation of the top linux command."""
import datetime
import random
import time
from dataclasses import dataclass

from rich import box
from rich.console import Console
from rich.live import Live
from rich.table import Table
from typing import Literal


@dataclass
class Process:
    pid: int
    command: str
    cpu_percent: float
    memory: int
    start_time: datetime.datetime
    thread_count: int
    state: Literal["running", "sleeping"]

    @property
    def memory_str(self) -> str:
        if self.memory > 1e6:
            return f"{int(self.memory/1e6)}M"
        if self.memory > 1e3:
            return f"{int(self.memory/1e3)}K"
        return str(self.memory)

    @property
    def time_str(self) -> str:
        return str(datetime.datetime.now() - self.start_time)


def generate_process(pid: int) -> Process:
    return Process(
        pid=pid,
        command=f"Process {pid}",
        cpu_percent=random.random() * 20,
        memory=random.randint(10, 200) ** 3,
        start_time=datetime.datetime.now()
        - datetime.timedelta(seconds=random.randint(0, 500) ** 2),
        thread_count=random.randint(1, 32),
        state="running" if random.randint(0, 10) < 8 else "sleeping",
    )


def create_process_table(height: int) -> Table:
    processes = sorted(
        [generate_process(pid) for pid in range(height)],
        key=lambda p: p.cpu_percent,
        reverse=True,
    )
    table = Table(
        "PID", "Command", "CPU %", "Memory", "Time", "Thread #", "State", box=box.SIMPLE
    )

    for process in processes:
        table.add_row(
            str(process.pid),
            process.command,
            f"{process.cpu_percent:.1f}",
            process.memory_str,
            process.time_str,
            str(process.thread_count),
            process.state,
        )

    return table


console = Console()

with Live(console=console, screen=True, auto_refresh=False) as live:
    while True:
        live.update(create_process_table(console.size.height - 4), refresh=True)
        time.sleep(1)
        
        
        
        
        
        
        
        
        
        
"""Same as the table_movie.py but uses Live to update"""
import time
from contextlib import contextmanager

from rich import box
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text

TABLE_DATA = [
    [
        "May 25, 1977",
        "Star Wars Ep. [b]IV[/]: [i]A New Hope",
        "$11,000,000",
        "$1,554,475",
        "$775,398,007",
    ],
    [
        "May 21, 1980",
        "Star Wars Ep. [b]V[/]: [i]The Empire Strikes Back",
        "$23,000,000",
        "$4,910,483",
        "$547,969,004",
    ],
    [
        "May 25, 1983",
        "Star Wars Ep. [b]VI[/b]: [i]Return of the Jedi",
        "$32,500,000",
        "$23,019,618",
        "$475,106,177",
    ],
    [
        "May 19, 1999",
        "Star Wars Ep. [b]I[/b]: [i]The phantom Menace",
        "$115,000,000",
        "$64,810,870",
        "$1,027,044,677",
    ],
    [
        "May 16, 2002",
        "Star Wars Ep. [b]II[/b]: [i]Attack of the Clones",
        "$115,000,000",
        "$80,027,814",
        "$656,695,615",
    ],
    [
        "May 19, 2005",
        "Star Wars Ep. [b]III[/b]: [i]Revenge of the Sith",
        "$115,500,000",
        "$380,270,577",
        "$848,998,877",
    ],
]

console = Console()

BEAT_TIME = 0.04


@contextmanager
def beat(length: int = 1) -> None:
    yield
    time.sleep(length * BEAT_TIME)


table = Table(show_footer=False)
table_centered = Align.center(table)

console.clear()

with Live(table_centered, console=console, screen=False, refresh_per_second=20):
    with beat(10):
        table.add_column("Release Date", no_wrap=True)

    with beat(10):
        table.add_column("Title", Text.from_markup("[b]Total", justify="right"))

    with beat(10):
        table.add_column("Budget", "[u]$412,000,000", no_wrap=True)

    with beat(10):
        table.add_column("Opening Weekend", "[u]$577,703,455", no_wrap=True)

    with beat(10):
        table.add_column("Box Office", "[u]$4,331,212,357", no_wrap=True)

    with beat(10):
        table.title = "Star Wars Box Office"

    with beat(10):
        table.title = (
            "[not italic]:popcorn:[/] Star Wars Box Office [not italic]:popcorn:[/]"
        )

    with beat(10):
        table.caption = "Made with Rich"

    with beat(10):
        table.caption = "Made with [b]Rich[/b]"

    with beat(10):
        table.caption = "Made with [b magenta not dim]Rich[/]"

    for row in TABLE_DATA:
        with beat(10):
            table.add_row(*row)

    with beat(10):
        table.show_footer = True

    table_width = console.measure(table).maximum

    with beat(10):
        table.columns[2].justify = "right"

    with beat(10):
        table.columns[3].justify = "right"

    with beat(10):
        table.columns[4].justify = "right"

    with beat(10):
        table.columns[2].header_style = "bold red"

    with beat(10):
        table.columns[3].header_style = "bold green"

    with beat(10):
        table.columns[4].header_style = "bold blue"

    with beat(10):
        table.columns[2].style = "red"

    with beat(10):
        table.columns[3].style = "green"

    with beat(10):
        table.columns[4].style = "blue"

    with beat(10):
        table.columns[0].style = "cyan"
        table.columns[0].header_style = "bold cyan"

    with beat(10):
        table.columns[1].style = "magenta"
        table.columns[1].header_style = "bold magenta"

    with beat(10):
        table.columns[2].footer_style = "bright_red"

    with beat(10):
        table.columns[3].footer_style = "bright_green"

    with beat(10):
        table.columns[4].footer_style = "bright_blue"

    with beat(10):
        table.row_styles = ["none", "dim"]

    with beat(10):
        table.border_style = "bright_yellow"

    for box_style in [
        box.SQUARE,
        box.MINIMAL,
        box.SIMPLE,
        box.SIMPLE_HEAD,
    ]:
        with beat(10):
            table.box = box_style

    with beat(10):
        table.pad_edge = False

    original_width = console.measure(table).maximum

    for width in range(original_width, console.width, 2):
        with beat(1):
            table.width = width

    for width in range(console.width, original_width, -2):
        with beat(1):
            table.width = width

    for width in range(original_width, 90, -2):
        with beat(1):
            table.width = width

    for width in range(90, original_width + 1, 2):
        with beat(1):
            table.width = width

    with beat(2):
        table.width = None        