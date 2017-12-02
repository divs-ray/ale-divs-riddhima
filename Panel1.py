# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import math

#Reading stata files without value labels

inv_2 = pd.DataFrame(pd.read_stata("investments_data.dta", convert_categoricals=False))

#Panel A: Agricultural assets

#Breaking panel A into two parts--Treatment and control

#Masking for treatment group, treatment variable =t2_c1_op, where 1= treatment, 0=control

inv_2_t1 = inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0) & (inv_2["t2_c1_op"] == 1) ]

#Panel A: Treatment group Set 1

agri=['ani197', 'ani297', 'land97']

data_t={'Agricultural_assests':['Drafts animals ownership', 'Production animal ownership', 'Land Use'],
        'N_t':[],
      'Mean_t':[],
      'SD_t':[]}
for var in agri:
    count=(inv_2_t1[var].count())
    data_t['N_t'].append(count)
    mean=(inv_2_t1[var].mean())*100
    data_t['Mean_t'].append(mean)
    std=(inv_2_t1[var].std())
    data_t['SD_t'].append(std)


summ_stats_t1=pd.DataFrame(data_t,columns=['Agricultural_assests','N_t','Mean_t','SD_t'])

#Panel A: Treatment group 2nd set

agri_2=['vani197', 'vani297', 'ha97']

data_t={'Agricultural_assests':['Monetary value of draft animals','Monetary value production animals','Number hectares used'],
        'N_t':[],
      'Mean_t':[],
      'SD_t':[]}

for x in agri_2:
    inv_2_t2 = inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0) & (inv_2[x] >0) &(inv_2["t2_c1_op"] == 1)]
    count=(inv_2_t2[var].count())
    data_t['N_t'].append(count)
    mean=(inv_2_t2[var].mean())*100
    data_t['Mean_t'].append(mean)
    std=(inv_2_t2[var].std())
    data_t['SD_t'].append(std)

summ_stats_t2=pd.DataFrame(data_t,columns=['Agricultural_assests','N_t','Mean_t','SD_t'])

#Joining Panel A treatment group statistics together

panel_a_t=pd.concat([summ_stats_t1, summ_stats_t2], axis=0)


#Panel A: control group
#Masking for control group

inv_2_c = inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0) & (inv_2["t2_c1_op"] == 0) ]

#Panel A: Contol group Set 1


data_c={'N_c':[],
      'Mean_c':[],
      'SD_c':[]}
for var in agri:
    count=(inv_2_c[var].count())
    data_c['N_c'].append(count)
    mean=(inv_2_c[var].mean())*100
    data_c['Mean_c'].append(mean)
    std=(inv_2_c[var].std())
    data_c['SD_c'].append(std)

summ_stats_c1=pd.DataFrame(data_c,columns=['N_c','Mean_c','SD_c'])

#Panel A Contol group Set 2


data_c={'N_c':[],
      'Mean_c':[],
      'SD_c':[]}

for x in agri_2:
    inv_2_c = inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0) & (inv_2[x] >0) &(inv_2["t2_c1_op"] == 0)]
    count=(inv_2_c[var].count())
    data_c['N_c'].append(count)
    mean=(inv_2_c[var].mean())*100
    data_c['Mean_c'].append(mean)
    std=(inv_2_c[var].std())
    data_c['SD_c'].append(std)



summ_stats_c2=pd.DataFrame(data_c,columns=['N_c','Mean_c','SD_c'])


#Getting the control together

panel_a_c=pd.concat([summ_stats_c1, summ_stats_c2], axis=0)

#Getting the treatment and control group together
panel_a=pd.concat([panel_a_t, panel_a_c], axis=1)

print(panel_a)


#Running TTest individually for ani and land as ani297 needs cleaning

agri_subset=['ani197','land97']

for a in agri_subset:
    print(stats.ttest_ind(a=inv_2_t1[a],
                b=inv_2_c[a]))

#Cleaning ani297 to run the TTest

#converting all values to numeric to ignore unwanted values

inv_2_t1['ani297']=pd.to_numeric(inv_2_t1['ani297'], errors='coerce')
inv_2_c['ani297']=pd.to_numeric(inv_2_c['ani297'], errors='coerce')

#removing Na

inv_2_t1.dropna(subset=['ani297'], inplace=True)
inv_2_c.dropna(subset=['ani297'], inplace=True)


print(stats.ttest_ind(a=inv_2_t1['ani297'],
                b=inv_2_c['ani297']))


#Panel A Set 2: TTests
for x in agri_2:
    inv_2_t2 = inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0) & (inv_2[x] >0) &(inv_2["t2_c1_op"] == 1)]
    inv_2_c2 = inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0) & (inv_2[x] >0) &(inv_2["t2_c1_op"] == 0)]
    print(stats.ttest_ind(a=inv_2_t2[x],
                b=inv_2_c2[x]))
