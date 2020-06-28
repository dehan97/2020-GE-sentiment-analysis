# CHANGE LINE 18

import pandas as pd
import numpy as np
import twitterscraper as ts
from wordcloud import WordCloud
from textblob import TextBlob
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.rc('xtick', labelsize=5)

font = {'weight' : 'bold',
        'size'   : 5}

plt.rc('font', **font)

file = pd.read_csv("wpsg.csv")
df = pd.DataFrame(file)

# ## To create subjectivity (use to tell how subjective or opinionated the tweet is
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity
#
# ## To create polarity (use to tell how positive or negative the tweet is)
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# ## Create the Subjectivity and Polarity results columns in the df
df["Subjectivity"] = df["text"].apply(getSubjectivity)
df["Polarity"] = df["text"].apply(getPolarity)

# ## Plotting a Word/Text Cloud
allWords = " ".join( [twts for twts in df['text']])
wordCloud = WordCloud(width = 500, height=300, random_state = 21, max_font_size = 119).generate(allWords)
#
plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
plt.show()

# # Create a function that computes the negative, neutral and positive analysis
def getAnalysis(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else :
        return "Positive"
#
df["Analysis"] = df["Polarity"].apply(getAnalysis)

# ## Plotting the sentimental analysis by plotting the polarity (x-axis) and subjectivity (y-axis)
plt.figure(figsize=(8,6))
for i in range(0, df.shape[0]): # in range from 0 to the no. of rows in our df
  plt.scatter(df["Polarity"][i], df["Subjectivity"][i], color='Blue')
plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()

# ## Getting the % of positive/negative tweets
ptweets = df[df.Analysis == "Positive"]
percentage_positive = ptweets.shape[0] / df.shape[0]
print(percentage_positive)

ntweets = df[df.Analysis == "Negative"]
percentage_negative = ntweets.shape[0] / df.shape[0]
print(percentage_negative)

## Plotting and visualizing the counts
plt.title('Positive, Negative and Neutral Count')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind = 'bar')
plt.show()