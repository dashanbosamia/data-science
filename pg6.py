# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:06:08 2019

@author: dbosami2
"""

import pandas as pd

import numpy as np

data=pd.read_csv('tips.csv')

def record_gender(gender):
    
    if gender == 'Female':
        return 0
    elif gender == 'Male':
        return 1
    else:
        return np.nan
    
    
data['recode']= data.sex.apply(record_gender)

print(data.head())