from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2020,6,20)
end_date = dt.date(2020,6,28)

limit = 1000
lang = "english"

# run for #PAP , #wpsg, #ProgressSgParty, #GE2020SG
tweets = query_tweets("#ProgressSgParty", begindate = begin_date, enddate=end_date, limit=limit, lang = lang)

df = pd.DataFrame(t.__dict__ for t in tweets)
df.to_csv('ProgressSgParty.csv')