# Stock Data Analysis Application

A Streamlit-based application for analyzing market data, including stock and cryptocurrency prices, as well as forecasting future stock prices using a neural network. Users can access historical data, visualize charts, and predict stock prices using a pre-trained model.



## 🌟 Features

- **📈 Stock Analysis**: 
  - Fetch data for any stock symbol (e.g., AAPL, TSLA) from Yahoo Finance.
  - View interactive closing price charts.
  
- **💰 Cryptocurrency Analysis**:
  - Analyze cryptocurrencies (e.g., BTC-USD, ETH-USD).
  - Interactive chart visualization for crypto prices.
  
- **🤖 Stock Price Prediction**:
  - Utilize a TensorFlow-based neural network for forecasting future stock prices based on historical data.

---

## 🗂 Project Structure

- **`app.py`**: The main Streamlit app file that includes navigation between pages.
- **`send_requests.py`**: Contains functions to fetch market data from external APIs (e.g., Polygon.io).
- **`pages/actions.py`**: Implements stock analysis functionalities and displays data in a chart.
- **`pages/cryptocurrencies.py`**: Provides cryptocurrency analysis using Yahoo Finance data.
- **`predictor.py`**: Handles price prediction using TensorFlow, including data preprocessing and model training.

---

## 🚀 Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/marpot/stock_data_analyse.git
   ```

2. Navigate to the project directory:
   ```bash
   cd stock_data_analyse
   ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## 📋 Requirements

- Python 3.6+
- Streamlit
- Plotly
- TensorFlow
- Yahoo Finance API (for stock and cryptocurrency data)

---

## 💻 Technologies Used

- **Streamlit**: Framework for creating interactive web apps in Python.
- **Plotly**: Library for creating high-quality, interactive data visualizations.
- **Yahoo Finance API**: Data source for stock and cryptocurrency prices.
- **TensorFlow**: Used for implementing and training the neural network.

---

## 📊 Examples

1. **Stock Analysis**:
   - Enter a stock symbol (e.g., `AAPL`) to visualize historical closing prices in an interactive chart.
2. **Cryptocurrency Analysis**:
   - Enter a cryptocurrency symbol (e.g., `BTC-USD`) to display its historical prices and interactive charts.
3. **Stock Price Prediction**:
   - Get the next day's stock price prediction using a pre-trained neural network.

---

## 🌟 Future Features

- Support for additional financial markets and asset types.
- Improved prediction models considering external factors (e.g., news sentiment, economic indicators).
- Integration with more comprehensive data sources.

---

## 🛠 Troubleshooting

### Common Issues
- **Missing Dependencies**: Ensure all packages are installed correctly using `pip install -r requirements.txt`.
- **Streamlit Not Found**: Verify that the correct Python environment is active.

### Suggestions
- Use a virtual environment to avoid conflicts with system-wide dependencies.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🧑‍💻 Author

Developed by **Marcin Potoczny**.  
Feel free to explore and contribute! 🚀
