# -*- coding: utf-8 -*-
#PAnel B: Head of HH characteristics

# Masking for wave and eligibility
inv_2 = inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0)]

#Taking care of any missing values
inv_2.dropna(subset=['age_hh', 'female_hh', 'ethnicity_hh', 'educ_hh'], inplace=True)

#Creating new dummy variables for education

import numpy as np
inv_2['educ_0']=np.where(inv_2['educ_hh'] <=0.5, 1, 0)
inv_2['educ_1']=np.where((inv_2['educ_hh'] >=0.5) & (inv_2['educ_hh'] <=5), 1, 0)
inv_2['educ_2']=np.where(inv_2['educ_hh'] ==6, 1, 0)
inv_2['educ_3']=np.where((inv_2['educ_hh'] >=7) & (inv_2['educ_hh'] <=18), 1, 0)


hh_char=['age_hh', 'female_hh', 'ethnicity_hh', 'educ_0', 'educ_1', 'educ_2', 'educ_3']

#Treatment group


#Creating a seperate dataframe for the treatment group
inv_2_t=inv_2.loc[inv_2["t2_c1_op"] == 1]

data_t={'Head of HH characteristics':['Age', 'Female','Indigenous','Never attended school','Primary school not completed','Primary school completed','More than Primary School'],
        'N_t':[],
        'Mean_t':[],
        'SD_t':[]}
for var in hh_char:
    count=(inv_2_t[var].count())
    data_t['N_t'].append(count)
    mean=(inv_2_t[var].mean())*100
    data_t['Mean_t'].append(mean)
    std=(inv_2_t[var].std())
    data_t['SD_t'].append(std)


summ_stats_t=pd.DataFrame(data_t,columns=['Head of HH characteristics','N_t','Mean_t','SD_t'])


#control group
inv_2_c=inv_2.loc[inv_2["t2_c1_op"] == 0]

data_c={'N_c':[],
      'Mean_c':[],
      'SD_c':[]}
for var in hh_char:
    count=(inv_2_c[var].count())
    data_c['N_c'].append(count)
    mean=(inv_2_c[var].mean())*100
    data_c['Mean_c'].append(mean)
    std=(inv_2_c[var].std())
    data_c['SD_c'].append(std)

summ_stats_c=pd.DataFrame(data_c,columns=['N_c','Mean_c','SD_c'])

panel_b=pd.concat([summ_stats_t, summ_stats_c], axis=1)
print(panel_b)

for x in hh_char:
    print(stats.ttest_ind(a=inv_2_t[x],
                b=inv_2_c[x]))
