# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:20:22 2019

@author: dbosami2
"""


import pandas as pd

data=pd.read_csv('airquality.csv')
data_melt=pd.melt(data, id_vars=['Month','Day'],var_name='measurement', value_name='reading')
#print(data_melt)


data_pivot=data_melt.pivot_table(index=['Month','Day'], columns='measurement',values='reading')

print(data_pivot.head())