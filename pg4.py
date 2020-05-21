# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:02:37 2019

@author: dbosami2
"""

import pandas as pd

data=pd.read_csv('ebola.csv')
data_melt=pd.melt(data, id_vars=['Date','Day'],var_name='type_country', value_name='counts')
#print(data_melt.head())

data_melt['str_split']= data_melt.type_country.str.split('_')


data_melt['str_split']= data_melt.type_country.str.split('_')

data_melt['type']= data_melt.str_split.str.get(0)
data_melt['country']= data_melt.str_split.str.get(1)


print(data_melt.head())