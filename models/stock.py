from dataclasses import dataclass


@dataclass
class StockData:

    symbol: str
    company: str

    sector: str

    current_price: float

    market_cap: float

    pe: float

    pb: float

    roe: float

    debt_equity: float

    revenue_growth: float

    profit_margin: float

    history=None
