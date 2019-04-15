import newsapi
import numpy
import pandas as pd
from newsapi.articles import Articles

apikey = '455e01c84ca44ff387187f10f202bed3'
a = Articles(API_KEY = apikey)
data = a.get(source = "the-new-york-times", sort_by = 'top')

#print (data) ## raw news data

## -----------------------------------------------------------

data = pd.DataFrame.from_dict(data)
data = pd.concat([data.drop(['articles'], axis=1), data['articles'].apply(pd.Series)], axis=1)

#data.head()

# drop unused columns
# display only title and discription

news_df = data.drop(columns=['status', 'source','sortBy','author','url','urlToImage','publishedAt'])

#print(news_df)



print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")

# separate each row into lists of strings


## Lists of the two columns
title_list = news_df["title"].tolist()
desc_list = news_df["description"].tolist()

#print(title_list)

#print (desc_list)

## Separate lists for each title description pair
head1 = [title_list[0],desc_list[0]]
head2 = [title_list[1],desc_list[1]]
head3 = [title_list[2],desc_list[2]]
head4 = [title_list[3],desc_list[3]]
head5 = [title_list[4],desc_list[4]]
head6 = [title_list[5],desc_list[5]]
head7 = [title_list[6],desc_list[6]]

print (head1)
print (head2)
print (head3)
print (head4)
print (head5)
print (head6)
print (head7)
