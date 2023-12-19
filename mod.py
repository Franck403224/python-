# -*- coding: utf-8 -*-


def portfolio_return():
    # Importing required libraries
    import numpy as np
    import pandas as pd
    import yfinance as yf
    from datetime import datetime, timedelta

    # Setting date parameters
    today_date = datetime.now()
    start_date = (today_date - timedelta(days=3650)).date()

    # Determining the size of the portfolio
    number_stocks = int(input("How many stocks are in the portfolio? "))
    j = 1

    # Collecting ticker symbols of the companies
    companies = []
    while j <= number_stocks:
        company = str(input(f"Ticker for company {j}: "))
        companies.append(company)
        j += 1

    # Defining portfolio weights
    print("Portfolio Weights")
    weights = []
    i = 0
    total_weight = 0
    while total_weight != 100:
        weights.clear()
        total_weight = 0
        while i < number_stocks:
            weight = int(input(f"Weight for {companies[i]}: "))
            weights.append(weight)
            total_weight += weight
            i += 1
        if total_weight != 100:
            print("Invalid weights. The total should be 100.")
            i = 0

    # Converting weights to percentage
    weights = [w / 100 for w in weights]

    # Creating a table of historical values
    tickers = yf.Tickers(companies)
    data_table = tickers.download(start=start_date, end=today_date, interval='1d')['Close']

    # Creating the portfolio DataFrame
    portfolio = pd.DataFrame(columns=['Year'] + companies + ['Annual Return %'])

    # Calculating daily returns
    daily_returns = data_table.pct_change().dropna()
    if len(daily_returns) > 2500:
        daily_returns = daily_returns.tail(2500)

    # Calculating annual returns
    annual_returns = daily_returns + 1
    annual_averages = []
    for i in range(10):
        yearly_data = annual_returns.head(250)
        average_year = yearly_data.prod()
        annual_averages.append(average_year)
        annual_returns = annual_returns.iloc[250:]

    portfolio['Year'] = list(range(1, 11))
    portfolio[companies] = annual_averages

    # Calculating weighted average annual return
    portfolio['Annual Return %'] = (portfolio[companies].mul(weights).sum(axis=1) * 100) - 100
    total_performance = (portfolio['Annual Return %'] / 100 + 1).prod()
    return f"{portfolio}\nThe total return of the portfolio is: {total_performance * 100:.2f}%"
