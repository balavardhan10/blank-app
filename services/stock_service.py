import yfinance as yf

from models.stock import StockData


class StockService:

    def fetch(self, symbol):

        if not symbol.endswith(".NS"):
            symbol += ".NS"

        stock = yf.Ticker(symbol)

        info = stock.info

        history = stock.history(period="1y")

        return StockData(

            symbol=symbol,

            company=info.get("longName"),

            sector=info.get("sector"),

            current_price=info.get("currentPrice"),

            market_cap=info.get("marketCap"),

            pe=info.get("trailingPE"),

            pb=info.get("priceToBook"),

            roe=info.get("returnOnEquity"),

            debt_equity=info.get("debtToEquity"),

            revenue_growth=info.get("revenueGrowth"),

            profit_margin=info.get("profitMargins"),

            history=history
        )
