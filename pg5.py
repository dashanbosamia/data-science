# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:57:09 2019

@author: dbosami2
"""

import pandas as pd

data=pd.read_csv('airquality.csv')
ozone_mean= data.Ozone.mean()

#replace missing valueswith mean

data['Ozone']= data.Ozone.fillna(ozone_mean)

print(data)