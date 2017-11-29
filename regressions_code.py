# IPPP Final Project - Regression Analysis
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
#Impact of CCT Program on agricultural productivity variables  ani1(owns farm animals), ani2(owns other animals), land(uses land) 
#read data
inv_2 = pd.DataFrame(pd.read_stata("investments_data.dta", convert_categoricals=False))

#mask waves 2,3, 4
inv_2 = inv_2.loc[inv_2['wave'].isin([2,3,4])]

#drop obs with missing ani1, ani2, land, ha, me (relevant outcome vars)
inv_2.dropna(subset=['ani1', 'ani2', 'land', 'me', 'ha'], inplace=True)

#create dummies for waves 2,3,4
inv_2_waves = pd.get_dummies(inv_2['wave'])
inv_2_waves.rename(columns={2: 'wave2', 3: 'wave3', 4: 'wave4'}, inplace=True)
inv_2 = pd.concat([inv_2, inv_2_waves], axis=1)

#group outcome vars= anil1, anil2, land, vanil1, vanil2, ha
outcome_vars= ['ani1', 'ani2', 'land', 'me', 'ha']
for i in outcome_vars:

    x = inv_2[['t2_c1_op', 'nbani197', 'nbani297', 'ha97']]
    y= inv_2[[i]]
    x = sm.add_constant(x)
    est = sm.OLS(y, x).fit()
    print(est.summary())
