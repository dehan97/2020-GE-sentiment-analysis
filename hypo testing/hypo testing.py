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

# ## To create subjectivity (use to tell how subjective or opinionated the tweet is
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity
#
# ## To create polarity (use to tell how positive or negative the tweet is)
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

def getAnalysis(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else :
        return "Positive"
filelist = ['GE2020SG', 'output2806', 'PAP', 'ProgressSgParty', 'ST_GEN', 'ST_PAP', 'ST_PSP', 'ST_WP']
for file in filelist:
    csvfile = file + '.csv'
    red = pd.read_csv(csvfile)
    df = pd.DataFrame(red)
    # ## Create the Subjectivity and Polarity results columns in the df
    df["Subjectivity"] = df["text"].apply(getSubjectivity)
    df["Polarity"] = df["text"].apply(getPolarity)
    df["Analysis"] = df["Polarity"].apply(getAnalysis)
    output = 'hypo_' + file + '.csv'
    print(df.head())
    df.to_csv(output)
