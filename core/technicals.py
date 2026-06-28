import pandas as pd


class Technicals:

    @staticmethod
    def sma(df, days):

        return df["Close"].rolling(days).mean()

    @staticmethod
    def ema(df, days):

        return df["Close"].ewm(span=days).mean()

    @staticmethod
    def rsi(df, period=14):

        delta = df["Close"].diff()

        gain = delta.clip(lower=0)

        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(period).mean()

        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        return 100 - (100 / (1 + rs))
