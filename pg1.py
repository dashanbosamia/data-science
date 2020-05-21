# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:10:32 2019

@author: dbosami2
"""

import pandas as pd

data=pd.read_csv('airquality.csv')

#to prin first 5 rows
#print(data.head())

data_melt=pd.melt(data, id_vars=['Month','Day'])
print(data_melt.head())
