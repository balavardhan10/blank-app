import streamlit as st
import plotly.express as px

from data_fetcher import get_stock_data
from score_engine import calculate_score
from score_engine import recommendation



st.set_page_config(
    page_title="StockIQ AI",
    layout="wide"
)

st.title("📈 StockIQ AI")

st.write("AI Powered Indian Stock Analyzer")

symbol = st.text_input(
    "Enter NSE Symbol",
    "INFY"
)

if st.button("Analyze"):

    with st.spinner("Fetching Stock Data..."):

        data = get_stock_data(symbol)

        score, reasons = calculate_score(data)

        verdict = recommendation(score)

    st.header("Company Details")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Company", data["Company"])
        st.metric("Sector", data["Sector"])
        st.metric("Current Price", data["Current Price"])

    with col2:
        st.metric("Market Cap", data["Market Cap"])
        st.metric("PE", data["PE"])
        st.metric("PB", data["PB"])

    st.divider()

    st.header("AI Score")

    st.metric("Overall Score", f"{score}/100")

    st.success(verdict)

    st.divider()

    st.header("Reasons")

    for reason in reasons:
        st.write("✅", reason)

    st.divider()

    st.header("Raw Data")

    st.json(data)
    fig = px.line(

    stock.history,

    x=stock.history.index,

    y="Close",

    title="1 Year Stock Price"

)

st.plotly_chart(fig, use_container_width=True)
stock.history["RSI"] = Technicals.rsi(stock.history)

st.line_chart(stock.history["RSI"])
