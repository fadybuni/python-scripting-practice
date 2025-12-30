import requests

API_KEY = "E2H8AU4PT920PWBT"
welcome = input("Welcome to the stock fetcher app. Press any key to start (q to quit): ")

while welcome != "q":
    ticker = input("Please enter the ticker for the stock you would like to get the price of: ").strip().upper()
    if ticker == "Q":
        exit
    url = "https://www.alphavantage.co/query"


    params = {
        "function" : "GLOBAL_QUOTE",
        "symbol":ticker,
        "apikey":API_KEY
    }

    response = requests.get(url,params=params,timeout=10)
    response.raise_for_status()

    data = response.json()
    quote = data.get("Global Quote")
    if not quote:
        print("Not a valid ticker")
        exit()
    price = quote.get("05. price")
    change = quote.get("10. change percent")
    print(f"The price for the ticker {ticker} is ${price}. \nThe price has moved {change} since yesterday.")
