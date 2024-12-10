import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.title("Analiza kryptowalut")

symbol = st.text_input("Wpisz symbol kryptowaluty (np. BTC-USD, ETH-USD):", "BTC-USD")

if symbol:
    # Pobieranie danych kryptowaluty z Yahoo Finance
    crypto_data = yf.Ticker(symbol)
    data = crypto_data.history(period="1y")  # Dane z ostatniego roku

    if not data.empty:
        st.write("Tabela z danymi kryptowaluty:")
        st.dataframe(data)

        # Tworzenie interaktywnego wykresu za pomocą Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name="Cena zamknięcia"))
        fig.update_layout(
            title=f"Cena zamknięcia kryptowaluty {symbol}",
            xaxis_title="Data",
            yaxis_title="Cena zamknięcia (USD)",
            template="plotly_white"  # Ustawienie jasnego stylu wykresu
        )

        # Wyświetlenie interaktywnego wykresu w Streamlit
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Brak danych do wyświetlenia.")
