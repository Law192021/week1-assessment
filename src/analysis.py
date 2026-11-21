#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## 1. Introduction
# 
# This notebook analyzes employee data using Pandas.
# 
# ## 2. Data Loading

# In[2]:


import pandas as pd
import time
df = pd.read_csv("../data/employees.csv")
print("Employee Dataset:")
display(df.head())
print("Dataset Information:")
print(df.info())
print("Total Employees:", len(df))
chennai_employees = df[df["city"] == "Chennai"]
print("Chennai Employees:")
display(chennai_employees)
print("Department-wise Count:")
print(df["department"].value_counts())
print("Average Salary:", df["salary"].mean())


# In[3]:


import os

print("Current Directory:", os.getcwd())
print("Files:", os.listdir())


# In[4]:


df = pd.read_csv("data/employees.csv")


# In[5]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# In[ ]:




