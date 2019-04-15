from newsapi.articles import Articles
import pandas as pd

apikey = '455e01c84ca44ff387187f10f202bed3'
a = Articles(API_KEY = apikey)
data = a.get(source = "the-new-york-times", sort_by = 'top')

#print (data) ## raw news data

## -----------------------------------------------------------
data = pd.DataFrame.from_dict(data)
data = pd.concat([data.drop(['articles'], axis=1), data['articles'].apply(pd.Series)], axis=1)

data.head()

print(data.drop(columns=['status', 'source', 'sortBy', 'author', 'url', 'urlToImage', 'publishedAt']))

