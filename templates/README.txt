Stock Sentiment Analysis Web Application
========================================

Overview
--------
This is a Flask web application that analyzes the sentiment of recent news articles related to a given stock ticker symbol. Using the VADER Sentiment Analyzer, it processes the titles of news articles published in the last 3 days, calculating an average sentiment score to help users quickly gauge the market sentiment around a stock.

How It Works
------------
1. The user inputs a stock ticker symbol (e.g., AAPL for Apple) on the homepage.
2. The application verifies if the ticker is valid using Yahoo Finance data.
3. It fetches news articles about that ticker from the last 3 days using the NewsAPI.
4. It analyzes the sentiment of the article titles using VADER.
5. The average sentiment score and the number of analyzed articles are displayed in a formatted table on a results page.

File Breakdown
--------------
1. app.py
   - The main Flask application file.
   - Handles routing:
     - '/' route renders the homepage where users input stock ticker symbols.
     - '/result' route processes the submitted ticker, validates it, calls the sentiment analysis function, and renders the results page.
   - Imports and calls the run_analysis function from main.py.
   - Passes data (ticker symbol, sentiment results) to the HTML templates.

2. main.py
   - Contains the core logic of the sentiment analysis.
   - Defines the run_analysis(ticker) function which:
     - Fetches news articles related to the ticker for the past 3 days using NewsAPI.
     - Uses VADER sentiment analyzer to calculate sentiment scores for each article title.
     - Calculates the average sentiment score.
     - Returns the result as a pandas DataFrame with columns: Ticker, Articles, AvgSentiment.

3. templates/index.html
   - The homepage HTML template.
   - Provides a simple form where users enter a stock ticker symbol.
   - Displays error messages if the ticker is invalid.

4. templates/result.html
   - The results page HTML template.
   - Displays the ticker analyzed, the number of articles processed, and the average sentiment score in a clean table.
   - Shows a note indicating that the sentiment analysis is based on the last 3 days' news.

Requirements
------------
- Python 3.x
- Flask
- pandas
- requests
- vaderSentiment
- yfinance

You can install the required packages via:

pip install flask pandas requests vaderSentiment yfinance

How to Run
----------
1. Make sure you have your NEWS_API_KEY set correctly in main.py.
2. Run the Flask app:

python app.py

3. Open your browser and go to http://127.0.0.1:5000/.
4. Enter a stock ticker symbol and submit.
5. View the sentiment analysis results.

Notes
-----
- The sentiment analysis uses the VADER model, which is optimized for social media and news text.
- The average sentiment score ranges from -1 (very negative) to +1 (very positive).
- Only news articles in English from the last 3 days are considered.

