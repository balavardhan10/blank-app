# utils/formatter.py


class Formatter:

    @staticmethod
    def currency(value):

        if value is None:
            return "-"

        if value >= 1_00_00_00_00_000:
            return f"₹{value/1_00_00_00_00_000:.2f} L Cr"

        if value >= 1_00_00_00_000:
            return f"₹{value/1_00_00_00_000:.2f} Cr"

        if value >= 1_00_00:
            return f"₹{value/1_00_00:.2f} L"

        return f"₹{value:,.2f}"


    @staticmethod
    def percentage(value):

        if value is None:
            return "-"

        return f"{value*100:.2f}%"


    @staticmethod
    def ratio(value):

        if value is None:
            return "-"

        return round(value,2)


    @staticmethod
    def market_cap(value):

        if value is None:
            return "-"

        crore = value / 10000000

        if crore > 100000:

            return f"{crore/100000:.2f} L Cr"

        return f"{crore:.2f} Cr"
