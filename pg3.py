# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:28:41 2019

@author: dbosami2
"""


import pandas as pd

data=pd.read_csv('tb.csv')
data_melt=pd.melt(data, id_vars=['country','year'])
#print(data_melt)

data_melt['gender']=data_melt.variable.str[0]

print(data_melt['gender'].head())

data_melt['age_group']=data_melt.variable.str[1:2]

print(data_melt['age_group'].head())
data_melt['age_group_end']=data_melt.variable.str[2:4]
print(data_melt['age_group_end'].head())