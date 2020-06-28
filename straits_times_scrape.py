import pandas as pd
from newspaper import Article

df = pd.read_csv('st_scrape.csv')
print(df.head())

for ind in df.index:
    newsurl = df.loc[ind, 'URL']
    print('running for: ' + str(newsurl))
    #preprocssing
    article = Article(newsurl)
    article.download()
    article.parse()
    article.nlp()
    #obtaining info
    authors = article.authors
    pubdate = article.publish_date
    text = article.text
    title = article.title
    #filling df
    df.loc[ind , 'Date'] = pubdate
    df.loc[ind, 'Title'] = title
    df.loc[ind, 'Text'] = text
    print('job done for: ' + str(newsurl))

print(df.head())
df.to_csv('output2806.csv')
