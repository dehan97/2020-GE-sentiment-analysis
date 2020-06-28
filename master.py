import datetime as dt
# import pandas
# from twitterscraper import query_tweets
# import twitterscraper as ts
# import requests

# limit = 1000
# lang = "english"
#
# tweets = ts.query.query_tweets_from_user("awscloud")
# #, begindate=begin_date,enddate=end_date, limit=limit, lang=lang)
#
# df = pd.DataFrame(t.__dict__ for t in tweets)
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(df.head())

import pandas as pd
import numpy as np
import twitterscraper as ts
from twitterscraper import query_tweets
from wordcloud import WordCloud
from textblob import TextBlob
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

## Getting Elon Tweets

begin_date = dt.date(2020,5,1)
end_date = dt.date(2020,6,28)

limit = 1000
user = 'PAPSingapore'

tweets = ts.query.query_tweets_from_user(user)
df = pd.DataFrame(t.__dict__ for t in tweets)
df.to_csv('PAP.csv')