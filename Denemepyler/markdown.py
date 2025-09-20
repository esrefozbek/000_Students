
#!/usr/bin/python

from rich.console import Console
from rich.markdown import Markdown

with open('pattern_match.md', 'r') as f:

    data = f.read()

    console = Console()
    md = Markdown(data)
    console.print(md)
