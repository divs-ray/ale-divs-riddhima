# IPPP Final Project - Regression Analysis
### IMPACT of CCT Program on agricultural productivity variables ###
# outcome vars are: ani1(owns farm animals), ani2(owns other animals), land(uses land)

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#read data
inv_2 = pd.DataFrame(pd.read_stata("investments_data.dta", convert_categoricals=False))

#mask waves 2,3, 4
inv_2 = inv_2.loc[inv_2['wave'].isin([2,3,4])]

#drop obs with missing ani1, ani2, land, ha, me (relevant outcome vars)
inv_2.dropna(subset=['ani1', 'vani1', 'ani2', 'vani2', 'land', 'ha''t2_c1_op','nbani197', 'nbani297',
'ha97', 'nbani197', 'nbani297', 'ha97', 'no497', 'big497', 'age_hh',
'age_hh2', 'female_hh', 'educ1_hh', 'ethnicity_hh', 'age_sp', 'age_sp2',
'educ1_sp', 'dage0_7_97', 'dage8_17_97', 'dage18_54_97', 'hhsize97',
'homeown97', 'dirtfloor97', 'electricity97', 'org_faenas', 'min_dist', 'lnup_cwagepm',
'up2_mcwagepm', 'dummy_age_hh', 'dummy_educ_hh', 'dummy_ethnicity_hh', 'dummy_age_sp',
'dummy_educ_sp', 'dummy_dage0_7_97', 'dummy_dirtfloor97', 'dummy_electricity97'], inplace=True)

#create dummies for waves 2,3,4
inv_2_waves = pd.get_dummies(inv_2['wave'])
inv_2_waves.rename(columns={2: 'wave2', 3: 'wave3', 4: 'wave4'}, inplace=True)
inv_2 = pd.concat([inv_2, inv_2_waves], axis=1)
#we will also need these for the regression
inv_2.dropna(subset=['wave3', 'wave4'], inplace=True)

#group outcome vars= anil1, anil2, land, vanil1, vanil2, ha
outcome_vars= ['land', 'me', 'ha']
# Impact of treatment on draft animal ownership

x = inv_2[['t2_c1_op', 'nbani197', 'nbani297', 'ha97', 'ha97', 'nbani197', 'nbani297', 'ha97', 'no497', 'big497', 'age_hh',
                     'age_hh2', 'female_hh', 'educ1_hh', 'ethnicity_hh', 'age_sp', 'age_sp2',
                     'educ1_sp', 'dage0_7_97', 'dage8_17_97', 'dage18_54_97', 'hhsize97',
                     'homeown97', 'dirtfloor97', 'electricity97', 'org_faenas', 'min_dist', 'lnup_cwagepm',
                     'up2_mcwagepm', 'dummy_age_hh', 'dummy_educ_hh', 'dummy_ethnicity_hh', 'dummy_age_sp',
                     'dummy_educ_sp', 'dummy_dage0_7_97', 'dummy_dirtfloor97', 'dummy_electricity97']]
y= inv_2[['ani1']]
x = sm.add_constant(x)
est = sm.OLS(y, x).fit()
print(est.summary())

# Impact of treatment on animal ownership value

x = inv_2[['t2_c1_op', 'wave3','wave4', 'nbani197', 'nbani297', 'ha97', 'nbani197', 'nbani297', 'ha97', 'no497', 'big497', 'age_hh',
                     'age_hh2', 'female_hh', 'educ1_hh', 'ethnicity_hh', 'age_sp', 'age_sp2',
                     'educ1_sp', 'dage0_7_97', 'dage8_17_97', 'dage18_54_97', 'hhsize97',
                     'homeown97', 'dirtfloor97', 'electricity97', 'org_faenas', 'min_dist', 'lnup_cwagepm',
                     'up2_mcwagepm', 'dummy_age_hh', 'dummy_educ_hh', 'dummy_ethnicity_hh', 'dummy_age_sp',
                     'dummy_educ_sp', 'dummy_dage0_7_97', 'dummy_dirtfloor97', 'dummy_electricity97']]
y= inv_2[['vani1']]
x = sm.add_constant(x)
est = sm.OLS(y, x).fit()
print(est.summary())
