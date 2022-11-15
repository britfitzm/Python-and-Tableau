# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:15:42 2022

@author: spitz
"""

import pandas as pd

df = pd.read_excel('articles.xlsx')
data = df.copy()

data.groupby(['source_id'])['article_id'].count()

data.groupby(['source_id'])['engagement_reaction_count'].sum()

data = data.drop('engagement_comment_plugin_count', axis = 1)

#Creating a keyword flag

keyword = 'crash'
length = len(data)
keyword_flag = []
for x in range(0, length):
    heading = data['title'][x]
    try:
        if keyword in heading:
            flag = 1
        else:
            flag = 0
    except:
        flag = 0        
    keyword_flag.append(flag)
        
#Creating a keyword flag using a fuction

def keywordflag(Keyword):
    length = len(data)
    keyword_flag1 = []
    for x in range(0, length):
        heading = data['title'][x]
        try:
            if Keyword in heading:
                flag1 = 1
            else:
                flag1 = 0
        except:
            flag1 = 0        
        keyword_flag1.append(flag1)
    return keyword_flag1

keywordflag = keywordflag('murder')

data['keyword_flag'] = pd.Series(keywordflag)

import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][15]

sent = sent_int.polarity_scores(text)

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

data['title_neg_sentiment'] = pd.Series(title_neg_sentiment)
data['title_pos_sentiment'] = pd.Series(title_pos_sentiment)
data['title_neu_sentiment'] = pd.Series(title_neu_sentiment)

data.to_excel('blogme_cleaned.xlsx', sheet_name = 'blogmedata', index = False)









