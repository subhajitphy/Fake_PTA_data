#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pickle, sys, os, glob


# In[29]:


psrs=glob.glob('J*')


# In[33]:


psrnames=[os.path.splitext(psr)[0] for psr in psrs]


# In[40]:


pkl_psrs=[]


# In[41]:


for psr in psrs:
    pkl_psr=pickle.load(open(psr,'rb'))
    pkl_psrs.append(pkl_psr)


# In[42]:


savedir="./"


# In[43]:


pickle_loc=f"./{savedir}/combined_{len(pkl_psrs)}psr.pkl"

with open(pickle_loc, 'wb') as f:
    pickle.dump(pkl_psrs, f)


# In[ ]:




