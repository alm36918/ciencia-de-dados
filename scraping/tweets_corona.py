#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pygsheets


# In[ ]:


#bibliotecas utilizadas
import datetime 
import tweepy
import csv
import pytz
import pandas as pd
import matplotlib.pyplot as plt
from tweepy import OAuthHandler, Stream, Cursor, API
import pickle
import os
import pygsheets


# In[ ]:


#autenticação api twitter
consumer_key= "SUACHAVE"
consumer_secret= "SEUSDADOS"
access_token= "SEUSDADOS"
access_token_secret= "SEUS DADOS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


# In[6]:


#autorização google drive
gc = pygsheets.authorize(service_file="/Users/andreluiz/Desktop/python/corona-twitter/corona-tw-db411a6c3082.json")


# In[ ]:


#definição da busca
search_words = "coronavirus" + " -filter:retweets"
date_since = "2020-01-23"

#puxando os tweets
tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="pt-br",
              since=date_since).items(500)
handle = "followers_id"
user = api.get_user(handle)

#imprimindo os tweets
users_locs = [[tweet.user.screen_name, tweet.user.followers_count, tweet.user.location, tweet.text] for tweet in tweets]
users_locs


# In[ ]:


#criando um dataframe com Pandas
tweet_text = pd.DataFrame(data=users_locs, 
                    columns=["user", "friends", "location", "text"])
tweet_text

#export_csv = tweet_text.to_csv ("/Users/andreluiz/Desktop/python/corona-twitter/corona-twitter.csv", index = None, header=True)

#tweet_text


# In[ ]:


import wordcloud


# In[ ]:


# Novas bibliotecas necessárias
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


# In[ ]:


conda install -c conda-forge wordcloud 


# In[ ]:


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
users_locs = [[tweet.text] for tweet in tweets]
text = user_locs
wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    background_color = 'black',
    stopwords = STOPWORDS).generate(str(tweet_text))
fig = plt.figure(
    figsize = (40, 30),
    facecolor = 'k',
    edgecolor = 'k')
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


# In[ ]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
stopwords = set(stopwords.words('portuguese'))


# In[ ]:


print(stopwords)


# In[ ]:


import nltk
nltk.download('punkt')


# In[ ]:


conda install -c conda-forge google-cloud-bigquery 


# In[ ]:




