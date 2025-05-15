import requests 
import pandas as pd
from Transform import df_clean
import Api_calls
import config
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm



sia = SentimentIntensityAnalyzer()

Sims4_df = df_clean

# getting the sentiments based on each comment 
sentiments = []
for index, row in Sims4_df.iterrows():

    sentiment_score = sia.polarity_scores(row['selftext'])
    compound = sentiment_score['compound']

    if compound >= 0.05:
        sentiment = 'Positive'
    elif compound <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'


    sentiments.append({
    'Sentiment_Score': sentiment_score,
    'Sentiment_Label': sentiment
    })

# order 


# save to cache, return dataframe and save it to a csv file
sentiment_df = pd.DataFrame(sentiments)
s_file = sentiment_df.to_csv('Sims_sentiment.csv', index=False)

# Concat the sims_new file and the sims sentiment.csv file
concating = pd.concat(map(pd.read_csv, ['Sims4_new.csv', 'Sims_sentiment.csv']), axis=1)
concating.to_csv('merged_sentiment.csv', index=False)


# import streamlit as st 
#st.dataframe(filter_sentiment_df)
# st.write(filter_sentiment_df)