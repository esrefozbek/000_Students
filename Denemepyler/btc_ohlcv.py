#!/usr/bin/python

import asyncio
import ccxt.async_support as ccxt

from rich import box
from rich.console import Console
from rich.table import Table
from datetime import datetime


async def tickers():

    binance = ccxt.binance()
    data = await binance.fetch_ohlcv('BTC/USDT', '1d', limit=20)
    await binance.close()

    now = f'{datetime.today()}'
    table = Table(title='Binance - BTC/USDT', box=box.ASCII,
                  caption=now, caption_justify='left')

    table.add_column('Date', justify='center', style='steel_blue')
    table.add_column('Open')
    table.add_column('High')
    table.add_column('Low')
    table.add_column('Close')
    table.add_column('Volume', justify='right', style='cadet_blue')

    for e in data:
        d = datetime.utcfromtimestamp(e[0]/1000.0)
        table.add_row(f'{d:%m/%d/%Y}', f'{e[1]:.2f}', f'{e[2]:.2f}',
                      f'{e[3]:.2f}', f'{e[4]:.2f}', f'{e[5]:.5f}')

    console = Console()
    console.print(table)

asyncio.run(tickers())
