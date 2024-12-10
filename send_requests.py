# send_requests.py
import requests
import pandas as pd

def get_polygon_data(api_key, symbol, start_date, end_date, timespan='day', limit=100):
    # URL z dynamicznymi datami
    url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/{timespan}/{start_date}/{end_date}'

    params = {
        'apiKey': api_key,
        'limit': limit
    }

    response = requests.get(url, params=params)

    # Sprawdzenie statusu odpowiedzi
    if response.status_code == 200:
        try:
            data = response.json()
            if 'results' in data:
                return pd.DataFrame(data['results'])
            else:
                print("Brak danych 'results' w odpowiedzi.")
                return None
        except requests.exceptions.JSONDecodeError:
            print(f"Error: Odpowiedź nie jest w formacie JSON. Zawartość odpowiedzi: {response.text}")
            return None
    else:
        print(f"Error: Odpowiedź z API ma status {response.status_code}. Zawartość odpowiedzi: {response.text}")
        return None
