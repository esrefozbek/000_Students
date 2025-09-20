#!/usr/bin/python

from rich.console import Console
from rich.syntax import Syntax

stx = Syntax.from_path("filter.fsx", theme="nord-darker", line_numbers=True)

console = Console()
console.print(stx)
