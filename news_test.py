import newsapi

apikey = '455e01c84ca44ff387187f10f202bed3'
from newsapi.articles import Articles
a = Articles(API_KEY = apikey)
data = a.get(source = "the-new-york-times", sort_by = 'top')

#print (data) ## raw news data

## -----------------------------------------------------------
import numpy
import pandas as pd
data = pd.DataFrame.from_dict(data)
data = pd.concat([data.drop(['articles'], axis=1), data['articles'].apply(pd.Series)], axis=1)

data.head()

data.drop(columns=['status', 'source','sortBy','author','url','urlToImage','publishedAt'])
