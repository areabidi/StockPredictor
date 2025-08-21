import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime, timedelta
import yfinance as yf   

NEWS_API_KEY = "f93848edba8b458b90b4822f579ff8ef" 
# Create an instance of VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def run_analysis(ticker):
    # Define the date range for news fetching (last 3 days)
    today = datetime.now()
    from_date = (today - timedelta(days=3)).strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')

    # Function to fetch news articles for a ticker
    def fetch_news(ticker):
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={ticker}&from={from_date}&to={to_date}"
            f"&sortBy=publishedAt&language=en&apiKey={NEWS_API_KEY}"
        )
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('articles', [])
        else:
            print(f"Error fetching news for {ticker}: {response.status_code}")
            return []

    # Initialize a list to hold the sentiment results
    results = []
    #ticker = 'VOO'

    articles = fetch_news(ticker)
    sentiments = []
    # Analyze sentiment of each article's title
    for article in articles:
        title = article.get('title')
        if title:
            score = analyzer.polarity_scores(title)['compound']
            sentiments.append(score)

    # Calculate average sentiment; avoid division by zero if no sentiments
    avg_sentiment = round(sum(sentiments) / len(sentiments), 4) if sentiments else 0
    # Store the results for the ticker
    return {
    'Ticker': ticker,
    'Articles': len(sentiments),
    'AvgSentiment': avg_sentiment
    }

   


    # # Convert results to a pandas DataFrame and sort by sentiment score descending
    # df = pd.DataFrame(results)
    # # Print the sorted results
    # print(df.to_string(index=False))
    # return results

 


##multiple tickers
# tickers = ['AAPL', 'TSLA', 'MSFT', 'NVDA', 'AMZN']
# for ticker in tickers:
#     articles = fetch_news(ticker)
#     sentiments = []

#     # Analyze sentiment of each article's title
#     for article in articles:
#         title = article.get('title')
#         if title:
#             score = analyzer.polarity_scores(title)['compound']
#             sentiments.append(score)

#     # Calculate average sentiment; avoid division by zero if no sentiments
#     avg_sentiment = round(sum(sentiments) / len(sentiments), 4) if sentiments else 0

    #     # Store the results for the ticker
    #     results.append({
    #         'Ticker': ticker,
    #         'Articles': len(sentiments),
    #         'AvgSentiment': avg_sentiment
    #     })

    # # Convert results to a pandas DataFrame and sort by sentiment score descending
    # df = pd.DataFrame(results)
    # df = df.sort_values(by='AvgSentiment', ascending=False)

    # # Print the sorted results
    # print(df.to_string(index=False))
