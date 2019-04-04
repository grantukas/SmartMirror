import newsapi

apikey = '455e01c84ca44ff387187f10f202bed3'
from newsapi.articles import Articles
a = Articles(API_KEY = apikey)
data = a.get(source = "the-new-york-times", sort_by = 'top')

print (data) ## raw news data

## -----------------------------------------------------------
import numpy
import pandas as pd
data = pd.DataFrame.from_dict(data)
data = pd.concat([data.drop(['articles'], axis=1), data['articles'].apply(pd.Series)], axis=1)

data.head()

from newsapi.sources import Sources
s = Sources(API_KEY=apikey)

# return all available sources
sources = s.get()
# convert to dataframe and drop status column
sources = data = pd.DataFrame.from_dict(sources).drop('status', axis=1)
# take the array column 'sources' and spread it across multiple columns
sources = pd.concat([sources.drop(['sources'], axis=1),
                     sources['sources'].apply(pd.Series)], axis=1).drop('urlsToLogos', axis=1)
sources.tail()
