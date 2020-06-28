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

#TEST ########################
#parsing reference:
#https://medium.com/@randerson112358/scrape-summarize-news-articles-using-python-51a48af1b4e2

# test = 'https://www.straitstimes.com/politics/wp-to-reveal-its-election-line-up-only-on-nomination-day'
# article = Article(test)
#
# # Once we have the articles URL, we need to download the URL HTML content, parse the article, download the sentence tokenizer and extract key words.
# # Do some NLP
# article.download() #Downloads the link’s HTML content
# article.parse() #Parse the article
# # nltk.download('punkt')#1 time download of the sentence tokenizer
# article.nlp()#  Keyword extraction wrapper
#
# # 1-time
# # print(article.authors)
# # print(article.publish_date)
# # print(article.text)
# # print(article.summary)