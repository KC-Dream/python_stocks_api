
import requests
import secret
import format

#Stock Data

stock_url = "enter_url_here"

def get_data(user_input):
    print("getting data...")

    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": user_input,
        "apikey": secret.api_key
    }

    try:
        response = requests.get(stock_url, params=stock_params)
        data = response.json()["Time Series (Daily)"]
        stock_name = response.json()['Meta Data']['2. Symbol']

        data_list = [value for (key, value) in data.items()]
        most_recent_data = data_list[0]
        #format.format_data(stock_name, most_recent_data)
        return format.format_data(stock_name, most_recent_data)

    except:
        print("Something went wrong. Please enter a valid Stock Symbol.")
    else:
        print("Sucess! You entered a valid Symbol.")

