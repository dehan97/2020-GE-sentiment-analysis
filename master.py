import datetime as dt
import pandas as pd
from twitterscraper import query_tweets
import twitterscraper as ts

begin_date = dt.date(2020,5,1)
end_date = dt.date(2020,6,28)

limit = 1000
lang = "english"

tweets = ts.query.query_tweets_from_user("awscloud")
#, begindate=begin_date,enddate=end_date, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df.head())