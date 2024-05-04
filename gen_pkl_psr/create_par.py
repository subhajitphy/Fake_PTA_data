#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


#MPTA directory
dir_path="./DOI_reviewed_data/"


# In[3]:


directories = [name for name in os.listdir(dir_path)]


# In[4]:


psrs=directories


# In[5]:


len(psrs)


# In[6]:


import shutil


# In[7]:


newdir="MPTA_par"

if not os.path.exists(newdir):
    os.mkdir(newdir)


# In[8]:


for psr in psrs:
    target_file=f"{dir_path}/{psr}/clean.par"
    #print(target_file)
    if os.path.exists(target_file):
        #print("yes")
        shutil.copy(target_file,f"{newdir}/{psr}.par")  

