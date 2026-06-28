class ScoreEngine:

    def calculate(self, stock):

        score = 0

        reasons = []

        if stock.roe:

            if stock.roe > .20:

                score += 20

                reasons.append("Excellent ROE")

        if stock.debt_equity:

            if stock.debt_equity < 50:

                score += 20

                reasons.append("Low Debt")

        if stock.revenue_growth:

            if stock.revenue_growth > .15:

                score += 20

                reasons.append("High Revenue Growth")

        if stock.profit_margin:

            if stock.profit_margin > .15:

                score += 20

                reasons.append("Strong Profit Margin")

        if stock.pe:

            if stock.pe < 25:

                score += 20

                reasons.append("Reasonable Valuation")

        return score, reasons
