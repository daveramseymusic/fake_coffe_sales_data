import pandas as pd
import numpy as np
from sqlalchemy import create_engine


#create random date function
num_of_entries = 3900 #13 months(2/1/19-3/1/20) @ 10 wkshp bags per day

def random_datetimes_or_dates(start='2019-01-01 00:00', end='2020-03-01 00:00', out_format='datetime', n=num_of_entries):
    #set start and end to work from a string:
    fixed_start = pd.to_datetime(start)
    fixed_end = pd.to_datetime(end)
    '''set it up so it decides whether your using seconds or days.
    if seconds:
        date.value/10**9<--- this is how you get seconds from a unix timestamp aka date = pd.to_datetime('1936-01-01 00:05')
    if days:  
        date.value/24*60*60*10**9'''
    (divide_by, unit) = (10**9, 's') if out_format == 'datetime' else (24*60*60*10**9,'D')

    start_u = fixed_start.value// divide_by
    end_u = fixed_end.value// divide_by
    
    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit=unit)

# #create randomish coffee box name function withs specific probabilities
# def item_name_randomizer(size, p=None):
#     if not p:
#         p = (.40, .40, .15, .05)
#     names = ['rwanda_kivu', 'burundi_kayanza', 'yirgz' , 'ethiopia_guji', 'colombia_inga', 'colombia_sierra_sur', 'frogtown', 'bucktown']
#     return np.random.choice(names, p=p, size=size)

#create 2nd randomish coffee box name function
def item_name_randomizer2(size):
    # if not p:
    #     p = (.125, .125, .125, .125, .125, .125, .125, .125)
    names = ['el_salvador_el_scorpion', 'rwanda_kivu', 'burundi_kayanza', 'yirgz' , 'ethiopia_guji', 'colombia_inga', 'colombia_sierra_sur', 'frogtown', 'bucktown']
    return np.random.choice(names, size=size)
    
#create df
fake_box = pd.DataFrame()

#create first column with coffee box func
fake_box['item_name'] = item_name_randomizer2(num_of_entries)

#create second column with dates
# fake_box['created_at'] = random_datetimes_or_dates(start, end, out_format='datetime', n=5)
fake_box['created_at'] =random_datetimes_or_dates(start='2019-02-01 00:00', end='2020-03-01 00:00', out_format='datetime', n=num_of_entries)


# #add prices to each coffee item_base_price
# using a list comprehension:
fake_box['item_base_price'] = [15 if (row == 'frogtown' or row == 'bucktown') else 18 for row in fake_box.item_name]


#add random 'quantity'

fake_box['quantity'] = np.random.randint(1,3, num_of_entries)


#add dates where the workshop_batch_brew coffee changed
'''2/3/2020 colombia_inga - start
11/29/19 colombia_sierra_sur
10/04/19 ethiopia_guji
8/02/19 yirgz
6/01/19 el_salvador_el_scorpion
04/01/2019 burundi_kayanza
2/01/2019 rwanda_kivu'''

##add column 'wks_otb'
#create function called 'otb_judge' that will return which wks_otb during each purchase
def otb_judge(x):
    
    if (x >= pd.to_datetime('2019-02-01') and x < pd.to_datetime('2019-04-01')):
        return 'rwanda_kivu'
    elif (x >= pd.to_datetime('2019-04-01') and x <pd.to_datetime('2019-06-01')):
        return 'burundi_kayanza'
    elif (x >= pd.to_datetime('2019-06-01') and x <pd.to_datetime('2019-08-02')):
        return 'el_salvador_el_scorpion'
    elif (x >= pd.to_datetime('2019-08-02') and x <pd.to_datetime('2019-10-04')):
        return 'yirgz'
    elif (x >= pd.to_datetime('2019-10-04') and x < pd.to_datetime('2019-11-29')):
        return 'ethiopia_guji'
    elif (x >= pd.to_datetime('2019-11-29') and x < pd.to_datetime('2020-02-03')):
        return 'colombia_sierra_sur'
    elif (x >= pd.to_datetime('2020-02-03') and x <pd.to_datetime('2020-03-01')):
        return 'colombia_inga'
    else:
        return 'unknown coffee'

#create new column that applies 'otb_judge' to each element in 'created_at'
# df['date'] = df.air_date.apply(lambda x: pd.to_datetime(x))
fake_box['wksp_otb'] = fake_box.created_at.apply(lambda x: otb_judge(x))

fake_box = fake_box.sort_values(by=['created_at'],ascending=True).reset_index()

print(fake_box.iloc[:8,1:6])






# #transfer to sqlite
# engine = create_engine('sqlite:///save_pandas.db', echo=True)
# sqlite_connection = engine.connect()
# sqlite_table = "fake_box_sales"
# fake_box.to_sql(sqlite_table, sqlite_connection, if_exists='replace')

# sqlite_connection.close()

