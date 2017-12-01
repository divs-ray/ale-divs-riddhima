
# coding: utf-8

# In[216]:


# IPPP Final Project - Regression Analysis
### IMPACT of CCT Program on agricultural productivity variables ###
# outcome vars are: ani1(owns farm animals), ani2(owns other animals), land(uses land)

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#read data
inv_1 = pd.DataFrame(pd.read_stata("investments_data.dta", convert_categoricals=False))
muni_data=pd.DataFrame(pd.read_csv("muni_manu_data.csv"))

#Merge inv_1 with muni data on st_muni and convert 1998 data into integer for regression
inv_1['st_muni']=(inv_1['state'].astype(str).str.cat(inv_1['muni'].astype(str).str.zfill(3)))
inv_1['st_muni']=inv_1['st_muni'].astype(int)


muni_data=muni_data.rename(columns = {'code':'st_muni'})

#replace , and trailing characters
muni_data['1998']=muni_data['1998'].str.replace(',', '')
muni_data['1998']=muni_data['1998'].str.strip('.00')

muni_data['2003']=muni_data['2003'].str.replace(',', '')
muni_data['2003']=muni_data['2003'].str.strip('.00')

inv_2=pd.merge(inv_1, muni_data, on=('st_muni'), how='inner')

#drop nas and convert to int
inv_2 = inv_2.dropna(subset = ['1998'])
inv_2['1998']=inv_2['1998'].astype(int)

#mask waves 2,3, 4
inv_2 = inv_2.loc[inv_2['wave'].isin([2,3,4])]

#drop obs with missing ani1, ani2, land, ha, me (relevant outcome vars)
inv_2.dropna(subset=['ani1', 'ani2', 'land', 'me', 'ha'], inplace=True)

#create dummies for waves 2,3,4
inv_2_waves = pd.get_dummies(inv_2['wave'])
inv_2_waves.rename(columns={2: 'wave2', 3: 'wave3', 4: 'wave4'}, inplace=True)
inv_2 = pd.concat([inv_2, inv_2_waves], axis=1)

#group outcome vars= anil1, anil2, land, vanil1, vanil2, ha
outcome_vars= ['ani1', 'ani2', 'land', 'vani1', 'vani2', 'ha']
for i in outcome_vars:

    x = inv_2[['t2_c1_op', 'nbani197', 'nbani297', 'ha97', '1998', 'age_hh', 'age_hh2', 'female_hh', 'educ1_hh', 
               'ethnicity_hh','age_sp', 'age_sp2', 'educ1_sp', 'dage0_7_97', 'dage8_17_97', 'dage18_54_97', 'dage55p_97',
               'hhsize97', 'homeown97', 'dirtfloor97', 'electricity97', 'org_faenas', 'min_dist', 'lnup_cwagepm', 
               'up2_mcwagepm', 'dummy_age_hh', 'dummy_educ_hh', 'dummy_ethnicity_hh', 'dummy_age_sp', 'dummy_educ_sp', 
               'dummy_dage0_7_97', 'dummy_dirtfloor97', 'dummy_electricity97']]
    y= inv_2[[i]]
    x = sm.add_constant(x)
    est = sm.OLS(y, x,missing='drop').fit()
    print(est.summary())


# In[200]:


inv_2['1998'].isnull().sum()

