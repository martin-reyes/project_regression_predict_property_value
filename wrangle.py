import pandas as pd

import sys
import os

home_directory_path = os.path.expanduser('~')
sys.path.append(home_directory_path +'/utils')
import env



def get_connection(db, user=env.user, host=env.host, password=env.pwd):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    

def get_sql_data(sql_query, db, filename):
    '''
    If the csv file exists, it is read and returned as a pandas DataFrame
    If not, pandas reads in a SQL query that acquires telco customer data from a MySQL database.
    The query is stored into a DataFrame, saved, and returned.
    '''
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        # Read the SQL query into a dataframe
        df = pd.read_sql(sql_query,
                            get_connection(db))
        # Write that DataFrame for prep
        df.to_csv(filename, index=False)
        # Return the DataFrame
        return df

    
def prep_zillow(df = get_sql_data( '''
                                    SELECT p.parcelid, p.id, p.bathroomcnt, p.bedroomcnt,
                                            p.calculatedfinishedsquarefeet, p.fips,
                                            p.latitude, p.longitude, p.yearbuilt, p.regionidcity,
                                            p.regionidzip, p.taxvaluedollarcnt, pred.transactiondate
                                    FROM zillow.properties_2017 AS p
                                        JOIN zillow.predictions_2017 AS pred USING (parcelid)
                                    WHERE (p.propertylandusetypeid IN (261, 262, 263, 264, 279));
                                    ''',
                                  'zillow',
                                  'data/zillow_raw.csv'),
                filename='data/zillow.csv'):
    '''
        This function takes the raw zillow data and transforms data for exploration and modeling
    '''
    # keep only 2017 transactions
    df = df[df['transactiondate'].str.startswith('2017')]
    
    # drop duplicate home id's. sort by transactiondate to keep most recent transaction date
    df = df.sort_values(by=['transactiondate'], ascending=False)\
           .drop_duplicates(['id'])
    
    # drop duplicate home locations. sort by transactiondate to keep most recent transaction date
    df = df.sort_values(by=['transactiondate'], ascending=False)\
           .drop_duplicates(['latitude','longitude'])

    # rename columns
    df.columns = ['parcelid', 'id', 'bathrooms', 'bedrooms', 'sqft', 'fips', 'latitude',
                   'longitude', 'year_built', 'regionidcity', 'regionidzip',
                   'property_value', 'transaction_date']
    
    # drop rows with missing values
    df = df.dropna()
    
    # change year_built to age
    df['age'] = df['year_built'].max() - df['year_built']
    df = df.drop(columns=['year_built'])
    
    # filter data
    # 2 to 5 bedrooms
    df = df[(df['bedrooms'] >= 2) & (df['bedrooms'] <= 5)]
    # 1 to 4 bathrooms, not including 1.75
    df = df[(df['bathrooms'] >= 1) & (df['bathrooms'] <= 4)]
    # age < 105
    df = df[df['age'] <= 105]
    # sqft < 5000 and > 500
    df = df[(df['sqft'] >= 500) & (df['sqft'] <= 5000)]
    # property_value < 1,500,000 and > 50,000
    df = df[(df['property_value'] >= 50_000) & (df['property_value'] <= 1_500_000)]
    
    # change whole number float columns to integer data types
    for col in df.columns:
        if col == 'transaction_date': continue
        if df[col].apply(lambda x: True if x % 1 == 0 else False).all():
            df[col] = df[col].astype(int)

    # add county name column
    df['county'] = df['fips'].replace({6037:'LA',
                                  6059:'Orange',
                                  6111:'Ventura'})
    
    # save csv
    df.to_csv(filename, index=False)
    
    return df

    

    
