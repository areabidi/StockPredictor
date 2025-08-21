import requests
from flask import Flask, render_template, request
import yfinance as yf

from main import run_analysis

from datetime import datetime, timedelta
import pandas as pd

app = Flask(__name__)

def is_valid_ticker(ticker):
    try: 
        stock = yf.Ticker(ticker)
        info = stock.info
        return 'regularMarketPrice' in info and info['regularMarketPrice'] is not None
    except Exception:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    ticker = request.form.get('ticker', '').upper()
    if not is_valid_ticker(ticker):
        error = f" '{ticker}' is not a valid stock ticker."
        return render_template('index.html', error = error)
    

    result_data = run_analysis(ticker)



    return render_template('result.html', ticker=ticker,  result = result_data)




if __name__ == '__main__':
    app.run(debug=True)
