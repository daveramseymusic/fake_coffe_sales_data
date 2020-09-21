import pandas as pd
import numpy as np
from sqlalchemy import create_engine


#create random date function

def random_datetimes_or_dates(start='2020-01-01 00:00', end='2020-03-01 00:00', out_format='datetime', n=10):
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

#create randomish coffee box name function
def item_name_randomizer(size, p=None):
    if not p:
        p = (.40, .40, .15, .05)
    names = ['ardi', 'yirgz', 'mexico', 'timor']
    return np.random.choice(names, p=p, size=size)
    
#create df
fake_box = pd.DataFrame()

#create first column with coffee box func
fake_box['item_name'] = item_name_randomizer(15, p=None)

#create second column with dates
# fake_box['created_at'] = random_datetimes_or_dates(start, end, out_format='datetime', n=5)
fake_box['created_at'] =random_datetimes_or_dates(start='2020-01-01 00:00', end='2020-03-01 00:00', out_format='datetime', n=15)
print(fake_box)


#transfer to sqlite
engine = create_engine('sqlite:///save_pandas.db', echo=True)
sqlite_connection = engine.connect()
sqlite_table = "fake_box_sales"
fake_box.to_sql(sqlite_table, sqlite_connection, if_exists='replace')

sqlite_connection.close()

