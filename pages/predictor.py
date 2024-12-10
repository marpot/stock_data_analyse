import yfinance as yf
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
import streamlit as st

def get_yahoo_finance_data(symbol, start_date="2020-01-01", end_date="2023-01-01"):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        
        if data.empty:
            print("Brak danych dla podanego symbolu w wybranym zakresie dat.")
            return pd.DataFrame()  # Zwróć pustą ramkę danych, jeśli nie ma danych
        
        return data
    except Exception as e:
        print(f"Błąd podczas pobierania danych: {e}")
        return pd.DataFrame()  # Zwróć pustą ramkę danych w przypadku błędu

def prepare_data(data):
    data = data[['Close']] # Używamy tylko kolumny "Close" (cena zamknięcia)
    data['Target'] = data['Close'].shift(-1) # Przesunięcie danych, aby przewidywać przyszłą cenę
    data = data.dropna()  # Usuwamy wiersze z brakującymi danymi
    X = data[['Close']].values  # Funkcja niezależna
    y = data['Target'].values  # Zmienna zależna (to, co chcemy przewidzieć)
    return X, y

def create_neural_network():
    model = Sequential([
        Dense(64, input_dim=1, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Trening modelu sieci neuronowej
def train_neural_network(X, y):
    model = create_neural_network()
    model.fit(X, y, epochs=10, batch_size=32, verbose=1)
    return model

# Przewidywanie przyszłej ceny
def predict_future_price(model, last_price):
    predicted_price = model.predict(np.array([[last_price]]))  # Predykcja przyszłej ceny
    return predicted_price[0][0]

# Aplikacja Streamlit
def run_predictor():
    st.title("Przewidywanie ceny akcji z siecią neuronową")

    # Wybór symbolu akcji
    symbol = st.text_input("Wpisz symbol akcji (np. AAPL, TSLA):", "AAPL")

    # Dynamiczny wybór daty początkowej i końcowej
    start_date = st.date_input("Data początkowa:", value=pd.to_datetime("2020-01-01"))
    end_date = st.date_input("Data końcowa:", value=pd.to_datetime("2023-01-01"))

    # Pobieranie danych
    if st.button("Pobierz dane"):
        # Zmienione argumenty: start_date i end_date (małe litery)
        data = get_yahoo_finance_data(symbol, start_date=start_date, end_date=end_date)
        
        if not data.empty:
            st.write("Dane historyczne:")
            st.dataframe(data)

            # Przygotowanie danych
            X, y = prepare_data(data)
            
            # Trening modelu
            model = train_neural_network(X, y)

            # Przewidywanie przyszłej ceny
            last_price = data['Close'].iloc[-1]  # Ostatnia dostępna cena zamknięcia
            predicted_price = predict_future_price(model, last_price)

            st.write(f"Przewidywana cena akcji {symbol} na następny dzień: {predicted_price:.2f}")

            # Wykres cen zamknięcia
            st.write("Wykres cen zamknięcia:")
            fig, ax = plt.subplots()
            ax.plot(data.index, data['Close'], label='Cena zamknięcia')
            ax.set_xlabel("Data")
            ax.set_ylabel("Cena")
            ax.legend()
            st.pyplot(fig)
        else:
            st.write("Brak danych dla wybranego symbolu.")

# Uruchomienie aplikacji
if __name__ == "__main__":
    run_predictor()

