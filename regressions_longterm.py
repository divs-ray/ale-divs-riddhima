
import pandas as pd
import numpy as np
import statsmodels.api as sm


#read investment data
investments = pd.DataFrame(pd.read_stata("investments_data.dta", convert_categoricals=False))

#mask wave 7 to get 2003 data and drop obvs with no consumption data
investments = investments.loc[(investments['wave']==7) & (investments['consumo']!=0)]
investments.dropna(subset=['consumo'], inplace = True)

#mask out 1 (poorest hh) ntile and 200 (richest hh) ntile of consumption
investments =  investments.loc[(investments['consumo_pp_ae2'] > 22.2066) & (investments['consumo_pp_ae2'] < 1118.53)]

#dropping na of outcome vars and regressors
investments.dropna(subset=['consumo_pp_ae2','t2_c1_op', 'hhsize_ae2_97', 'nbani197', 'nbani297', 'ha97', 'no497',
'big497', 'age_hh', 'age_hh2', 'female_hh', 'educ1_hh', 'ethnicity_hh', 'age_sp', 'age_sp2', 'educ1_sp', 'dage0_7_97',
'dage8_17_97', 'dage18_54_97', 'homeown97', 'dirtfloor97', 'electricity97','lnup_cwagepm', 'up2_mcwagepm',
'dummy_age_hh', 'dummy_educ_hh', 'dummy_ethnicity_hh', 'dummy_age_sp', 'dummy_educ_sp',
'dummy_dage0_7_97', 'dummy_dirtfloor97', 'dummy_electricity97'], inplace=True)

#regression
x = investments[['t2_c1_op', 'hhsize_ae2_97', 'nbani197', 'nbani297', 'ha97', 'no497',
'big497', 'age_hh', 'age_hh2', 'female_hh', 'educ1_hh', 'ethnicity_hh', 'age_sp', 'age_sp2', 'educ1_sp', 'dage0_7_97',
'dage8_17_97', 'dage18_54_97', 'homeown97', 'dirtfloor97', 'electricity97','lnup_cwagepm', 'up2_mcwagepm',
'dummy_age_hh', 'dummy_educ_hh', 'dummy_ethnicity_hh', 'dummy_age_sp', 'dummy_educ_sp',
'dummy_dage0_7_97', 'dummy_dirtfloor97', 'dummy_electricity97']]
y= investments[['consumo_pp_ae2']]
x = sm.add_constant(x)
est = sm.OLS(y, x).fit()
print(est.summary())
