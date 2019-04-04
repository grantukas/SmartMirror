import newsapi

apikey = '455e01c84ca44ff387187f10f202bed3'
from newsapi.articles import Articles
a = Articles(API_KEY = apikey)
data = a.get(source = "bbc-news", sort_by = 'top')

## print (data) ## raw news data

import pandas

data = pd.DataFrame.from_dict(data)
data = pd.concat
