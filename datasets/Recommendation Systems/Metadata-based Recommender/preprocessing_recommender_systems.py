import pandas as pd
import numpy as np
from ast import literal_eval


#Helper function to convert NaN to 0, if there are any, and all other years to integers.
def convert_int(x):
    try:
        return int(x)
    except:
        return 0


def clean_data(df):
    
    relevant_features = ['title','genres', 'release_date', 'runtime', 'vote_average', 'vote_count', 'overview', 'id']
    df = df[relevant_features]

    #Convert release_date into pandas datetime format
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    
    # Extract year from release_date-column and store the values into a new year-column
    df['year'] = pd.DatetimeIndex(df['release_date']).year

    #Apply convert_int to the year feature
    df['year'] = df['year'].apply(convert_int)

    #Drop the release_date column
    df = df.drop('release_date', axis=1)    
    
    #Convert all NaN into stringified empty lists
    df['genres'] = df['genres'].fillna('[]')

    #Apply literal_eval to convert stringified empty lists to the list object
    df['genres'] = df['genres'].apply(literal_eval)

    #Convert list of dictionaries to a list of strings
    df['genres'] = df['genres'].apply(lambda x: [i['name'].lower() for i in x] if isinstance(x, list) else [])

    
    return df