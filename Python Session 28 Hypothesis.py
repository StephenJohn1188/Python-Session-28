#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import scipy.stats as stats
ds=pd.read_csv("role_website.csv")


# In[5]:


ds


# In[7]:


ds.describe()


# In[8]:


ds.info()


# In[12]:


ds.dtypes


# In[18]:


ds_crosstab=pd.crosstab(ds['role'],ds['website'],margins=True)


# In[ ]:





# In[19]:


print(ds_crosstab)


# In[20]:


ds_crosstab.columns=['facebook','linkedin','row_totals']
ds_crosstab.index=['Student','Teacher',"col_totals"]
ds_crosstab


# In[22]:


observed=ds_crosstab.iloc[0:2,0:2]


# In[23]:


observed


# In[29]:


chi2,p,dof,expected=stats.chi2_contingency(observed=observed)
print("Chi square test",chi2)
print('p-value=',p)
print('dof=',dof)
print('expected=',expected)


# In[31]:


alpha=0.05
if p>=alpha:
    print("Variables and not associated and independent(accept H0 - Null Hypothesis)")
else:
    print("Variables and associated and dependent(reject H0 and accept H1")


# In[32]:


from scipy.stats import f_oneway


# In[35]:


Marks_SectionA=[70,40,56,50,60,79]
Marks_SectionB=[95,55,70,80,60,40]
Marks_SectionC=[70,30,80,90,40,100]


# In[36]:


f_oneway(Marks_SectionA,Marks_SectionB,Marks_SectionC)


# In[37]:


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# In[39]:


df=pd.read_csv('President_heights.csv')
df


# In[42]:


plt.boxplot(df.height)


# In[45]:


df['height'].quantile([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.90])


# In[52]:


from scipy.stats import zscore
import numpy as np


# In[53]:


z=np.abs(zscore(hf))
z

