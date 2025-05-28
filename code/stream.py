
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# # 
# def sentiments(df):
#     if df['Sentiment_Label'] == 'Positive':
#         df = df[df['Sentiment_Label']].str.contain('Positive')
#         return df

#     if df['Sentiment_Label'] == 'Negative':
#         df = df[df['Sentiment_Label']].str.contain('Negative')
#         return df
    
#     if df['Sentiment_Label'] == 'Nuetral':
#         df = df[df['Sentiment_Label']].str.contain('Nuetral')
#         return df


# def query():
#     if 

# st.title("Analyzing the Sims4 Subreddit Comments")


# sentiments = ['Negative', 'Positive', 'Nuetral']

dataset = pd.read_csv('excel_files/merged_sentiment.csv')

#------------------------------------

# I need to goes through each value in a sentiment score using a for loop
# The for loop will go through the dictionary containing each value

sen_scores = dataset.loc[dataset['Sentiment_Scores']]

for key, val in sen_scores.items():
    if key == 'Pos':
        pass
    if key == 'neu':
        pass
    if key == 'neg':
        pass








#_______________________

# select_sentiment = st.selectbox('Select Sentiment', sentiments)

# I need to have seperate data that only show pos/ neg/ nue (selectbox)
# Search database based on query keywords like I love, I hate, I like (multiselect)








#_______________________


# I need average pos / neg/ nue (pandas mean, 3 boxes)

dataset['Positive Average'] = dataset.loc[dataset['Sentiment_Label'] == 'Positive'].mean()


dataset['Negative Average'] = dataset.loc[dataset['Sentiment_Label'] == 'Negative'].mean()


dataset['Nuetral Average'] = dataset.loc[dataset['Sentiment_Label'] == 'Nuetral'].mean()

# Seaborn Graphs

# Linecharts - that uses frequency points where x = year and y = count of sentiments (time-series plot)



# Piechart - that will show the percentage of each pos/ neg/ nue




# Barcharts - three plots for pos/ neg/ nue

figure, series1 = plt.subplots()
bar = sns.barplot(data= dataset, x= "sentence_sentiment", y='max_confidence_score', hue= "sentence_sentiment", estimator="sum").set_title("Sentiment Analysis of Sims 4 Subreddit")



# Wordcloud - Inport images that can be used to showcase the wordcloud