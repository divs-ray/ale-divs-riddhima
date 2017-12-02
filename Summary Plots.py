# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns



sns.set_style("whitegrid")
sns.set_context('notebook', font_scale=1.45, rc={"lines.linewidth": 3, "figure.figsize" : (7, 10)})

#Plotting first set of Dependent variables

#renaming the columns
inv_2.rename(columns={'ani197':'Drafts animals ownership', 'ani297':'Production animals ownership','land97':'Land use'}, inplace=True)

#First set of dependent variables

agri=['Drafts animals ownership','Production animals ownership','Land use']

for x in agri:
    k=sns.boxplot(data=inv_2, x='t2_c1_op', y=x,width=.5,orient='h')
    k.set_ylabel("Treat Grp(1), Control Grp(1)")
    k.set_xlabel("{}: # of HHs".format(x))
    plt.show()


#Second set of dependent variables
#Reading the data as before

inv_2 = pd.DataFrame(pd.read_stata("investments_data.dta", convert_categoricals=False))

inv_2.rename(columns={'vani197':'Value of draft animals (pesos)','vani297':'Value of prod. animals (pesos)','ha97':'Number of hectares used'}, inplace=True)

#Plotting for value of draft animals (pesos)
inv_val_draft= inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0) & (inv_2['Value of draft animals (pesos)'] >0)]
k=sns.boxplot(data=inv_val_draft, x='t2_c1_op', y='Value of draft animals (pesos)', width=.5)
k.set_ylim(0,10000)
k.set_ylabel("Value of draft animals (pesos)")
k.set_xlabel("Control Grp(0), Treat Grp(1)")
plt.show(k)

#Plotting for value of production animals
inv_val_prod= inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0) & (inv_2['Value of prod. animals (pesos)'] >0)]
k=sns.boxplot(data=inv_val_prod, x='t2_c1_op', y='Value of prod. animals (pesos)', width=.5)
k.set_ylim(0,10000)
k.set_ylabel("Value of draft animals (pesos)")
k.set_xlabel("Control Grp(0), Treat Grp(1)")
plt.show(k)


#Plotting for # of heactare used

inv_ha= inv_2.loc[(inv_2["wave"] == 0) & (inv_2['ineligible']==0) & (inv_2['Number of hectares used'] >0)]
k=sns.boxplot(data=inv_ha, x='t2_c1_op', y='Number of hectares used', width=.5)
k.set_ylabel("Number of hectares used")
k.set_xlabel("Control Grp(0), Treat Grp(1)")
plt.show(k)
