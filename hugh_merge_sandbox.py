import pandas as pd
import numpy as np
from dateutil.parser import parse
import datetime

sand = pd.read_csv('frogtown_sample_three_hundo.csv',parse_dates=['created_at']) 
otb = pd.read_csv('Workshop Cafe Beverage - Workshop Cafe Beverage.csv')


#clean future column names columns
otb.iloc[0] = otb.iloc[0].str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

#grab row 0 for the new_column_names
new_column_names = otb.iloc[0] 
#reset index on 'new_column_names'
new_column_names = new_column_names.reset_index(drop=True)


#cut off evereything except the data you want and save as df
otb = otb[1:] 


#reset the index and drop the old index
otb = otb.reset_index(drop=True)


#add new column names to freshely clipped df
otb.columns = new_column_names


# ## Now turn month strings in to time parse  
#convert to just year and month:
otb['month/year'] = pd.to_datetime(otb['month/year'])


#Merge otb and sand so that each entry shows which box was used that month.
#sort 'sand' by created_at:
#df.sort_values(by=['col1'])
sand = sand.sort_values(by=['created_at'])


#merge sand with otb
otbsand = pd.merge_asof(
    sand,
    otb,
    left_on='created_at',
    right_on='month/year')


#select which columns from otbsand to compare to check that your merge_asof worked properly using code below
# print(df2[['col1', 'col2', 'col3']].head(10))


print(otbsand[['variant_name','created_at','year', 'month', 'month/year', 'batch_brew']])
print(otbsand.columns)















