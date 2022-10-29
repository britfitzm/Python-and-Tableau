# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:55:15 2022

@author: spitz
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

json_file = open('Loan_Data.json')
df = json.load(json_file)

data = df.copy()

loandata = pd.DataFrame(data)

loandata['fico'].describe()

income = np.exp(loandata['log.annual.inc'])
loandata['annual.income'] = income

length = len(loandata)

ficocat = []

for x in range(0, length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'unknown'
    except:
        cat = 'error'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

loandata.columns.values 

col_names = ['credit.policy', 'purpose', 'int.rate', 'installment',
       'log.annual.inc', 'dti', 'fico', 'days.with.cr.line', 'revol.bal',
       'revol.util', 'inq.last.6mths', 'delinq.2yrs', 'pub.rec',
       'not.fully.paid', 'annual.income', 'fico.category',
       'int.rate.type']

loandata.columns = col_names

col_names_reorder = ['credit.policy', 'purpose', 'int.rate','int.rate.type',
                     'installment','log.annual.inc', 'annual.income', 'dti', 
                     'fico', 'fico.category', 'days.with.cr.line', 'revol.bal',
                     'revol.util', 'inq.last.6mths', 'delinq.2yrs', 'pub.rec',
                     'not.fully.paid']

loandata = loandata[col_names_reorder] 

catplot = loandata.groupby(['fico.category']).size()
purposeplot = loandata.groupby(['purpose']).size()

catplot.plot.bar()
plt.show()

purposeplot.plot.bar(color = 'green', width = 0.65)
plt.show()

xpoint = loandata['annual.income']
ypoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

ypoint = loandata['annual.income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'red')
plt.show()

loandata.to_csv('BlueBank_Loandata_Cleaned.csv', index = True)













