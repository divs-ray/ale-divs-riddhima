# IPPP Final Project - Regression Analysis
import pandas as pd

import statsmodels.formula.api as smf

import matplotlib.pyplot as plt

inv_2 = pd.DataFrame(pd.read_stata("investments_data.dta", convert_categoricals=False))

#mask waves 2,3, 4
inv_2[inv_2.wave.isin([2,3,4])]

#drop obs with missing ani1, ani2, land or me (relevant outcome vars)
inv_2.dropna(subset=['ani1', 'ani2', 'land', 'me'])
#replace land=. if ha=.

#create dummies for wave 2,3 and 4

#group outcome vars= anil1, anil2, land, vanil1, vanil2, ha

#group basic

#ols=sm.ols(formula'y ~ x1 + x2 + x3 + x4 + x5 + x6 + x7', data=df).fit()
#print(ols.params)
