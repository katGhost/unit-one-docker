#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'


# In[3]:


df_zones = pd.read_csv(url)

df_zones.head()


# In[ ]:


taxi_zones

for df_zone in df_zones:
    if first:
        # Create table schema (no data)
        df_zone.head(0).to_sql(
            name=,
            con=engine,
            if_exists="replace"
        )

    # Insert chunk
    df_zone.to_sql(
        name=target_table,
        con=engine,
        if_exists="append"
    )

