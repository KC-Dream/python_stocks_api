
def format_data(stock_name, most_recent_data):
    print("formatting data...")

    opening_price = most_recent_data['1. open']
    closing_price = most_recent_data['4. close']

    low_price = most_recent_data['3. low']
    high_price = most_recent_data['2. high']

    volume = most_recent_data['5. volume']

    print(f'''
    Stock: {stock_name}\n
    Opening Price: {opening_price}\n
    Closing Price: {closing_price}\n
    Low Price: {low_price}\n
    High Price: {high_price}\n
    Volume: {volume}\n
    ''')

    stock_dictionary = [
        {
            'stock_name': stock_name,
            'opening_price': opening_price,
            'closing_price': closing_price,
            'low_price': low_price,
            'high_price': high_price,
            'volume': volume
        }
    ]

    return stock_dictionary

