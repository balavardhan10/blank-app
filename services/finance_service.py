# services/finance_service.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class FinancialMetrics:
    revenue: Optional[float] = None
    revenue_growth: Optional[float] = None

    pat: Optional[float] = None
    profit_growth: Optional[float] = None

    eps: Optional[float] = None

    ebitda: Optional[float] = None
    ebitda_margin: Optional[float] = None

    roe: Optional[float] = None
    roce: Optional[float] = None

    debt_equity: Optional[float] = None

    operating_cashflow: Optional[float] = None
    free_cashflow: Optional[float] = None

    pe: Optional[float] = None
    pb: Optional[float] = None


class FinanceService:

    @staticmethod
    def extract(info: dict) -> FinancialMetrics:
        """
        Converts raw Yahoo Finance dictionary
        into structured financial metrics.
        """

        return FinancialMetrics(

            revenue=info.get("totalRevenue"),

            revenue_growth=info.get("revenueGrowth"),

            pat=info.get("netIncomeToCommon"),

            profit_growth=info.get("earningsGrowth"),

            eps=info.get("trailingEps"),

            ebitda=info.get("ebitda"),

            ebitda_margin=info.get("ebitdaMargins"),

            roe=info.get("returnOnEquity"),

            roce=None,      # Yahoo doesn't provide this

            debt_equity=info.get("debtToEquity"),

            operating_cashflow=info.get("operatingCashflow"),

            free_cashflow=info.get("freeCashflow"),

            pe=info.get("trailingPE"),

            pb=info.get("priceToBook")

        )
