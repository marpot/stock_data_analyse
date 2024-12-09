```markdown
# Stock Data Analysis Application

A Streamlit-based application for market data analysis, including stock and cryptocurrency prices, and forecasting future stock prices using a neural network. Users can access historical data, analyze charts, and get stock price predictions based on a trained model.

## Features

- **Stock Analysis**: Enter a stock symbol (e.g., AAPL, TSLA) to fetch data from Yahoo Finance, including the closing price chart.
- **Cryptocurrency Analysis**: Similar analysis for cryptocurrencies (e.g., BTC-USD, ETH-USD) with Yahoo Finance data and an interactive chart.
- **Stock Price Prediction**: Use a neural network (TensorFlow) to predict future stock prices based on historical data.

## Project Structure

- **`app.py`**: The main Streamlit app with a menu to switch between different pages.
- **`send_requests.py`**: Functions for fetching market data from external APIs (e.g., Polygon).
- **`pages/actions.py`**: The stock analysis page that fetches data from Yahoo Finance and displays it in a chart.
- **`pages/cryptocurrencies.py`**: The cryptocurrency analysis page with similar functionality as the stock analysis page.
- **`predictor.py`**: A module for predicting stock prices using a TensorFlow neural network, including data fetching, model training, and future price prediction.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/marpot/stock_data_analyse.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Requirements

- Python 3.6+
- Streamlit
- Plotly
- TensorFlow
- Yahoo Finance API (for stock and cryptocurrency analysis)

## Technologies Used

- **Streamlit**: A framework for building web applications in Python.
- **Plotly**: A library for creating interactive charts.
- **Yahoo Finance API**: Source of market data.
- **TensorFlow**: A library for building and training neural network models.

## Examples

1. **Stock Analysis**: After entering a stock symbol (e.g., AAPL), the app will display historical data and an interactive closing price chart.
2. **Cryptocurrency Analysis**: After entering a cryptocurrency symbol (e.g., BTC-USD), the app will show the data and chart.
3. **Stock Price Prediction**: The app uses a trained neural network model to predict the next day's stock price based on historical data.

## Future Features

- Ability to analyze other financial markets.
- Expansion of the prediction model to include additional factors.
- Support for more data sources.

## License

This project is available under the MIT License.
```