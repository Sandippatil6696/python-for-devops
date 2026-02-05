import requests

API_KEY = "8TEQCDA16L2X1IKE"  # step 1 - get an api key 

base_url = "https://www.alphavantage.co/" # Step 2 - find an base url 

symbol = input("enter the symbol you want for stock market api ex ,IBM ,GOGL ,AMZN")

query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

api_url = base_url+query

def get_stock_market_details():
    
    response = requests.get(url=api_url)

    for key,value in response.json().items():
        if key=="Meta Data":
            print(key , value)

get_stock_market_details()