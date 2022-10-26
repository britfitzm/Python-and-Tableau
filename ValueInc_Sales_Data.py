# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:07:37 2022

@author: spitz
"""

import pandas as pd

df = pd.read_csv('transactions.csv', sep = ';')
season = pd.read_csv('value_inc_seasons.csv', sep = ';')

data = df.copy()

ssn = season.copy()

print(ssn)

length = len(data)
seasons = []

for x in range(0, length):
    month = data['Month'][x]
    try:
        if month == 'Jan':
            sn = 'High'
        elif month == 'Feb':
            sn = 'Mid'
        elif month == 'Mar':
            sn = 'Low'
        elif month == 'Apr':
            sn = 'Low'
        elif month == 'May':
            sn = 'Low'
        elif month == 'Jun':
            sn = 'High'
        elif month == 'Jul':
            sn = 'High'
        elif month == 'Aug':
            sn = 'High'
        elif month == 'Sep':
            sn = 'Mid'
        elif month == 'Oct':
            sn = 'Low'
        elif month == 'Nov':
            sn = 'Low'
        elif month == 'Dec':
            sn = 'High'
        else:
            sn = 'Unknown'
    except:
        sn = 'Error'
    seasons.append(sn)
            
seasons = pd.Series(seasons)
seasons.name = "Seasons"

data['Seasons'] = seasons      
            
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTRansaction = CostPerItem * NumberOfItemsPurchased

data['CostPerTransaction'] = CostPerTRansaction

SalesPerTransaction = data['SellingPricePerItem']* data['NumberOfItemsPurchased']

data['SalesPerTransaction'] = SalesPerTransaction

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']

roundmarkup = round(data['Markup'],2)
data['Markup'] = round(data['Markup'], 2)

day = data['Day'].astype(str)
year = data['Year'].astype(str)

date = day + '-' + data['Month'] + '-' + year

data['Date'] = date

split_cos = data['ClientKeywords'].str.split(',', expand = True)

data['ClientAge'] = split_cos[0]
data['ClientType'] = split_cos[1]
data['LengthOfContract'] = split_cos[2]

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

data['ItemDescription'] = data['ItemDescription'].str.lower()           
            
data.columns.values          
            
col_names = ['UserId', 'TransactionId', 'Year', 'Month', 'Day', 'Time',
       'ItemCode', 'ItemDescription', 'NumberOfItemsPurchased',
       'CostPerItem', 'SellingPricePerItem', 'Country', 'ClientKeywords',
       'Seasons', 'CostPerTransaction', 'SalesPerTransaction',
       'ProfitPerTransaction', 'Markup', 'Date', 'ClientAge',
       'ClientType', 'LengthOfContract']            
            
data.columns = col_names

col_names_reorder = ['UserId', 'TransactionId', 'Date', 'Year', 'Month', 'Day', 'Time',
       'Seasons', 'ItemCode', 'ItemDescription', 'NumberOfItemsPurchased',
       'CostPerItem', 'SellingPricePerItem', 'ClientKeywords',
       'CostPerTransaction', 'SalesPerTransaction',
       'ProfitPerTransaction', 'Markup', 'Country', 'ClientAge',
       'ClientType', 'LengthOfContract']   

data = data[col_names_reorder]   
data.head()     
   
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop('Month', axis = 1)
data = data.drop('Year', axis = 1)

data.to_csv('ValueInc_Clean.csv', index = False)

















         