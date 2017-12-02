# IPPP Final Project - Regression Analysis
### Long-term Health Impact ###
# outcome vars are: sick(dummy for person sick), days sick,

import pandas as pd
import numpy as np
import statsmodels.api as sm

#read investment data
investments = pd.DataFrame(pd.read_stata("investments_data.dta", convert_categoricals=False))

#mask wave 7 to get 2003 data and drop obvs with no consumption data
investments = investments.loc[(investments['wave']==7) & (investments['consumo_pp_ae']!=0)]
investments.dropna(subset=['consumo_pp_ae'], inplace = True)

#mask out 1 (poorest hh) ntile and 200 (richest hh) ntile of consumption
iinvestments =  investments.loc[(investments['consumo_pp_ae2'] > 22.2066) & (investments['consumo_pp_ae2'] < 1118.53)]

#read morbidity data
morbidity = pd.DataFrame(pd.read_stata("adults_morbidity_03.dta",convert_categoricals=False))

# create age squared
morbidity['age_sq'] = morbidity['age']**2

#sorting the columns for joining
morbidity.sort_values(by=['folio', 'state', 'muni', 'local', 'wave'], ascending=[True, True, True, True, True])

investments.sort_values(by=['folio', 'state', 'muni', 'local', 'wave'], ascending=[True, True, True, True, True])

#merge investment and morbidity data
invest_morbi=pd.merge(investments, morbidity, on=('folio', 'state', 'muni', 'local', 'wave'), how='inner')
#mask age
invest_morbi = invest_morbi.loc[(invest_morbi['age']<65)]

#dropna from health outcome variables and regressors
invest_morbi.dropna(subset=['t2_c1_op','nbani197', 'nbani297','ha97', 'sick','inactivity', 'days_sick', 'days_inactivity', 'female'], inplace=True)

#regressions loop
health_outcomes= ['sick','days_sick', 'inactivity', 'days_inactivity']
for v in health_outcomes:

    x = invest_morbi[['t2_c1_op', 'nbani197', 'nbani297', 'ha97', 'age','age_sq', 'female']]
    y= invest_morbi[[v]]
    x = sm.add_constant(x)
    est = sm.OLS(y, x).fit()
    print(est.summary())
