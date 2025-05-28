import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import pandas as pd


# I need a plot that will show the difference between positive, neutral, and negative sentiment
# Loading data
sentiment_data = pd.read_csv('excel_files/merged_sentiment.csv')
sentiment_data['count'] = 1

# barplot
figure, series1 = plt.subplots()
bar = sns.barplot(data=sentiment_data, x="sentence_sentiment", y='max_confidence_score', hue= "sentence_sentiment", estimator="sum").set_title("Sentiment Analysis of Sims 4 Subreddit")


#----------------------------------------------
# I need a word cloud that will show the most common words in the selftext

# positive word cloud

pos_words = sentiment_data[sentiment_data['sentence_sentiment'] == 'Positive']
pos_cloud = WordCloud(width=3000, height=1000, background_color='white', stopwords=STOPWORDS).generate(' '.join(pos_words['sentence_text']))
figure2 = plt.figure()
plt.title('Positive Sentiment')
plt.imshow(pos_cloud, interpolation="bilinear")
plt.axis("off")


# negative word cloud

neg_words = sentiment_data[sentiment_data['sentence_sentiment'] == 'Negative']
neg_cloud = WordCloud(width=3000, height=1000, background_color='white', stopwords=STOPWORDS).generate(' '.join(neg_words['sentence_text']))
figure3 = plt.figure()
plt.title('Negative Sentiment')
plt.imshow(neg_cloud, interpolation="bilinear")
plt.axis("off")


# neutral word cloud

neutral_words = sentiment_data[sentiment_data['sentence_sentiment'] == 'Neutral']
neutral_cloud = WordCloud(width=3000, height=1000, background_color='white', stopwords=STOPWORDS).generate(' '.join(neutral_words['sentence_text']))
figure4 = plt.figure()
plt.title('Nuetral Sentiment')
plt.imshow(neutral_cloud, interpolation="bilinear")
plt.axis("off")


#----------------------------------------------

# I want to have a sidebar that shows plots
st.sidebar.title("Plots")
#barplot
with st.sidebar:
    # Display the plot in Streamlit
    st.pyplot(figure)
#wordplots
    st.pyplot(figure2)
    st.pyplot(figure3)
    st.pyplot(figure4)

# I want a main section that shows and allows for the dataframe to be downloaded
st.title("Sims 4 Subreddit Data")
st.dataframe(sentiment_data)
csv = sentiment_data.to_csv(index=False).encode('utf-8')
st.download_button(label="Download CSV file", data=csv, file_name='sims4_sentiment_data.csv', mime='text/csv',
)